"""
AIPD 文件相关工具

author: lmy
created on: 2023/6/18
"""
import json
import traceback

from django.http import HttpResponseServerError
from django.http import HttpResponse

import pandas as pd
from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.styles import Font, Alignment, Color
from io import BytesIO
from urllib.parse import quote


class HzFileImportTools:
    """
    使用了pandas库来处理Excel文件
    文件导入工具

    导入工具包含如下功能：
        1.从 request 中获取文件内容（字典格式的数据）
        2.根据传入的字典检查文件合法性(包括表头和内容)，返回检查结果 {'state': '', 'message': ''}
    """

    def __init__(self, file, check_dict, type_dict={
        "str": str,
        "int": int,
        "float": float,
        "bool": bool,
        "datetime": pd.to_datetime,
    }, content_black=True):
        """
        初始化导入工具对象
            表头可以检查几种类型：
            1、校验表头是否一致
            2、校验内容类型是否正确
            入参：
                1、type_dict = {
                        "str": str,
                        "int": int,
                        "float": float,
                        "bool": bool,
                        "datetime": pd.to_datetime,
                    }
                # 检查数据的配置项
                2、check_dict = {
                    "header": ['列名1','列名2'],
                    "content": {'列名1':'str','列名2':'int',}
                }
                3、content_black excel中非表头能否为空

        """
        self.type_dict = type_dict
        self.check_dict = check_dict
        self.result = {'status': 200, 'msg': 'ok', 'data': None}
        self.filename = None
        self.file = file
        self.content_black = content_black

    def get_file_content(self):
        """
        获取文件内容
        并返回data
        return:
           {
            'Name': ['Alice', 'Bob'],
             'Age': [20, 22],
             'Gender': ['Female', 'Male']
            }
        """

        file = self.file
        # get_file_content
        # self.result = {'status': 200, 'msg': 'ok'}
        try:
            self.filename = file.name
        except KeyError as e:
            self.result['status'] = 500
            self.result['msg'] = '文件名称没有获取到：' + str(e)
            # return json.dumps(self.result)
            return self.result
        data = pd.read_excel(file)
        # 校验数据行数
        try:
            if not self.content_black:
                if data.shape[0] == 0:  # r
                    self.result['status'] = 500
                    self.result['data'] = None
                    self.result['msg'] = '您不能上传空数据：'
                    return self.result
        except Exception:
            self.result['status'] = 500
            self.result['msg'] = '您不能上传空数据：'
            return self.result
        self.result['data'] = data
        return self.result

    @staticmethod
    def get_excel_column_name(index):
        """
            获取到和excel 那种类似于字母的列号
        """
        column_name = ""

        while index > 0:
            index -= 1
            column_name = chr(ord('A') + index % 26) + column_name
            index //= 26

        return column_name

    def check_validity(self):
        """
            根据check_dict检查文件内容是否合法
        """
        rs = self.get_file_content()
        if rs['status'] == 200:
            #  数据
            data_array = rs['data']
            check_dict = self.check_dict
        else:
            return json.dumps(rs, ensure_ascii=False).encode('utf-8')

        if self.check_dict:  # 校验字典不为空

            """
               data_array =  是一个二维数组

                1、遍历数据
                2、校验表头 和检验内容 
                    2、1只校验表头
                    2、2 只校验内容
                    2、3只校验 表头和内容 
            """
            # 2.1 校验表头
            try:
                self.result['msg'] = ''  # msg 将msg设置为空
                # 遍历每个单元格，检查其值是否大于1
                header_if_check = False
                content_if_check = False
                if check_dict.get('header', ''):  # 是否配置了表头校验
                    header_if_check = True
                if check_dict.get('content', ''):  # 是否配置了内容校验
                    content_if_check = True
                if not content_if_check and not header_if_check:  # 都不用校验
                    self.result['msg'] = 'ok'  # msg 将msg设置为空
                    return json.dumps(self.result, ensure_ascii=False).encode('utf-8')

                # 检查表头
                head_error_flag = False
                for need_column_name in check_dict['header']:
                    if need_column_name not in data_array.columns:
                        head_error_flag = True
                        self.result['msg'] += f"缺少列名： '{need_column_name}';<br>"
                if head_error_flag:
                    self.result['status'] = 400
                    self.result['data'] = None
                    return json.dumps(self.result, ensure_ascii=False).encode('utf-8')

                insert_flag = -1  # 判断是否有内容区域的第一个错误
                for i in range(len(data_array)):
                    for j, column_name in enumerate(data_array.columns):
                        if content_if_check:  # 是否配置了内容校验
                            # 获取该列的校验规则
                            content_check_value = check_dict['content'].get(column_name, "")
                            if content_check_value != "":  # 该列内容要校验
                                if pd.isna(data_array.iat[i, j]):  # 是否为空
                                    column_letter = self.get_excel_column_name(j + 1)
                                    insert_flag += 1
                                    if insert_flag == 0:
                                        self.result['msg'] = self.result['msg'].rstrip(';')
                                        self.result['msg'] += f"<br>"
                                        self.result['msg'] += f"内容中:<br>"
                                        self.result['status'] = 500
                                    else:
                                        insert_flag = 1
                                    self.result['msg'] += f"  第{i + 1}行，第{column_letter}列值为空;<br>"
                                else:  # 该单元格值不为空
                                    try:
                                        # 比较校验规则里面的值类型是否存在
                                        check_type = self.type_dict[content_check_value]
                                    except KeyError:
                                        column_letter = self.get_excel_column_name(j + 1)
                                        self.result['status'] = 500
                                        self.result['msg'] = self.result['msg'].rstrip(';')
                                        self.result['msg'] += f"  第{column_letter}列，值校验规则为不合法<br>"
                                        pass
                                    else:  # 值类型存在，接下来校验 单元格类型
                                        try:
                                            check_type(data_array.iat[i, j])  # 判断该单元格类型与校验类型是否一致
                                        except ValueError:
                                            insert_flag = insert_flag + 1
                                            column_letter = self.get_excel_column_name(j + 1)
                                            if insert_flag == 0:
                                                self.result['status'] = 500
                                                self.result['msg'] = self.result['msg'].rstrip(';')
                                                self.result['msg'] += "内容中:"
                                            else:
                                                insert_flag = 1
                                            self.result[
                                                'msg'] += f"  第{i + 1}行，第{column_letter}列的值类型不等于{content_check_value};<br>"

                            else:  # 该表头列不校验
                                continue
                    if insert_flag == 1:
                        self.result['msg'] += "<br>"
                self.result['msg'] = self.result['msg'][:-1]  # 去掉最后一个<br>
                self.result['msg'] = self.result['msg'].rstrip(';')  # 去掉最后一个;
                self.result['msg'] += '。'  # 加。
            except KeyError or Exception as e:
                self.result['status'] = 500
                self.result['msg'] = '配置文件错误' + e.args[0]
                self.result['data'] = None
                return json.dumps(self.result, ensure_ascii=False).encode('utf-8')

            self.result['data'] = self.result['data'].to_json(orient='records', force_ascii=False)
            if self.result['msg'] == '。':
                self.result['msg'] == 'ok'
            return json.dumps(self.result, ensure_ascii=False).encode('utf-8')
        else:
            # 没有校验规则
            self.result['data'] = self.result['data'].to_json(orient='records', force_ascii=False)
            self.result['status'] = 500
            self.result['msg'] = '校验字典不能为空'
            self.result['data'] = None
            return json.dumps(self.result, ensure_ascii=False).encode('utf-8')


class HzFileExportTools:
    """
        文件导出工具
            导出工具包含如下功能：

                1、传进一个列表，列表里面每一个元素代表一行数据
                "data": {
                    'Name': ['Alice', 'Bob', 'Charlie'],
                    'Age': [25, 32, 22],
                    'City': ['New York', 'Los Angeles', 'London']
                },
                2、将1中传入的列表导出excel 返回，
                3要求规则返回的excel文件

            返回：excel 文件
    """

    def __init__(self, data=None, data_type=None, file_name='默认名称.xlsx', rules=None, freeze=None):
        self.freeze = freeze
        self.data_type = data_type
        self.rules = rules
        self.file_name = file_name
        self.data = data
        self.result = {'status': 200, 'msg': 'ok', 'data': None}

    def exportResponse(self):
        """
            从self.data 中获取data 和 file_name
                返回文件
        """
        # excel_content_data = self.data if self.data_type and self.data_type == 2
        try:
            # if 'data' in self.data and self.data:
            #     # 找到数组长度最大的列
            #     max_length = 0
            #     for key, value in self.data.items():
            #         if isinstance(value, list) and len(value) > max_length:
            #             max_length = len(value)
            #
            #     # 将其他列的长度设置为最大长度
            #     for key, value in self.data.items():
            #         if isinstance(value, list) and len(value) < max_length:
            #             self.data[key] += [''] * (max_length - len(value))
            # else:
            #     # 处理空数据的情况，例如返回特定响应或执行其他逻辑
            #     self.result['status'] = 500
            #     self.result['msg'] = '无数据可导出'
            #     return JsonResponse(self.result)
            if self.data_type and self.data_type == 2:
                # 数据类型为第二种
                df = pd.DataFrame(self.data)
            elif self.data_type and self.data_type == 1:
                df = pd.DataFrame(self.data['data'], columns=self.data['columns'])
            else:
                raise ValueError("data_type为1 或2")

            # 创建一个Workbook对象并禁用自动计算
            wb = Workbook()

            # 选择活动的工作表
            ws = wb.active

            # 直接导出DataFrame
            for row in dataframe_to_rows(df, index=False, header=True):
                ws.append(row)

            # cls_single_requiremen_card = SingleRequirementCard
            # 设置表头样式
            header_row = ws[1]
            for cell in header_row:
                if self.rules and 'head' in self.rules:
                    if 'Font' in self.rules['head']:
                        # 配置字体属性
                        cell.font = Font(bold=self.rules['head']['Font'].get('bold', None),
                                         color=Color(rgb=self.rules['head']['Font'].get('color', '00000000')),
                                         size=self.rules['head']['Font'].get('size', None))
                cell.alignment = Alignment(horizontal='center')

            # 冻结
            if self.freeze:
                ws.freeze_panes = self.freeze

            # 添加数据验证功能
            need_validation = 0
            # 是否添加了规则校验
            if self.rules:
                need_validation = len(self.rules['validation']) if 'validation' in self.rules else 0  # 有几个需要添加数据验证就是几
            for column_letter, column_name in zip(ws.columns, df.columns):
                if need_validation <= 0:
                    # 目前最多有n个需要验证，处理完n个立马结束
                    break
                # 查找该列列名是否在数据验证下拉列表里面
                for item in self.rules['validation']:
                    if column_name == item['column_name']:
                        # 如果列名存在于
                        need_validation -= 1
                        validation = DataValidation(
                            type=item['type'],
                            formula1=item['formula1'],
                            showDropDown=item['showDropDown']
                        )
                        range_str = column_letter[0].column_letter + '2:' + column_letter[0].column_letter + '1048576'
                        validation.add(range_str)  # This is the same as for the whole of column x
                        ws.add_data_validation(validation)

            # 设置列宽 根据列里面的文字长度设置列宽
            for column in ws.columns:
                max_length = 0
                column_letter = column[0].column_letter
                for cell in column:
                    if cell.coordinate in ws.merged_cells:  # 忽略合并单元格
                        continue
                    try:
                        value = str(cell.value)
                        if len(value) > max_length:
                            max_length = len(value)
                    except:
                        pass
                adjusted_width = (max_length + 4) * 1.8
                ws.column_dimensions[column_letter].width = adjusted_width
            #
            # 保存到字节流
            byte_stream = BytesIO()
            wb.save(byte_stream)

            # 设置HttpResponse的参数
            byte_stream.seek(0)

            # 创建一个HttpResponse对象
            response = HttpResponse(byte_stream.getvalue(), content_type='application/vnd.ms-excel')

            # 设置Content-Disposition
            response['Content-Disposition'] = 'attachment; filename="%s"' % quote(self.file_name)

            # 返回response
            return response
        except Exception:
            print(traceback.format_exc())
            return HttpResponseServerError('导出出错，请刷新重试')
