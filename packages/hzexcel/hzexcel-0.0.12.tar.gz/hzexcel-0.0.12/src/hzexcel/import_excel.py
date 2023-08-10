import json

import pandas as pd
from .file import HzFileImportTools


def import_excel(file, check_dict=None, type_dict={
    "str": str,
    "int": int,
    "float": float,
    "bool": bool,
    "datetime": pd.to_datetime,
}):
    """
         1、校验表中是否缺少某列
         2、校验内容类型是否正确
         入参：
         file 二进制excel文件，一般从前端传来的 self.request.FILES['file'] 中获取
         check_dict 校验的对象 ，其中header表示必须必须有那些列，content表示那些列 必填、而且指定类型，
        type_dict 判断非表头的数据类型，可选参数，可传入配置设置可校验类型，不传时默认值如下{
            "str": str,
            "int": int,
            "float": float,
            "bool": bool,
            "datetime": pd.to_datetime,
        }
    """

    file_import_util = HzFileImportTools(file, check_dict, type_dict)
    rs = json.loads(file_import_util.check_validity())
    if rs['status']:
        if 'data' in rs and rs['data']:
            rs['data'] = json.loads(rs['data'], encoding='utf-8')
        if 'msg' in rs:  # 手动矫正msg
            if rs['msg'] == '。':
                rs['msg'] = '校验成功！'
        return json.dumps(rs, ensure_ascii=False).encode('utf-8')
    else:
        rs = {'status': 500}
        rs['msg'] = f"导出出错，错误信息可能为：{json.dumps(rs, ensure_ascii=False).encode('utf-8')}"
        return json.dumps(rs, ensure_ascii=False).encode('utf-8')

