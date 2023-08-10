## **1概述**

**1.1可根据配置、参数提供校验和导入导出excel功能**

# **1.2贡献者：深圳市汉卓软件**

# 2.功能详细说明(API列表)：
# (1)export_excel(data, data_type{可选},file_name{可选} , rules{可选}, freeze{可选})
导出excel 。	   返回参数：成功时：返回excel 文件；失败时状态码为非200，返回错误信息。

# (2)import_excel(file, check_dict{可选},type_dict{可选})
导入excel并根据规则校验。返回参数：成功时：返回{"status":200,"msg":"校验成功！","data":[{"Name":"Alice","Age":25,"City":"New York"},{"Name":"Bob","Age":32,"City":"Los Angeles"},{"Name":"Charlie","Age":22,"City":"London"}]}；失败时，返回的状态码为非200，错误信息例子如下："缺少列名： 'City';<br>"


### 2.应用说明：
#### (1)export_excel参数说明
data:必选数据，有两种不同的数据结构可选，一种是每一行是一条数据，如：{'测试':['Alice','Bob','Charlie'],'Name':['Alice','Bob','Charlie'],'Age':[25,32,22],'City':['New York','Los Angeles','London']}
另一种是类似 DataFrame 的数据格式，比如：data:{"data":[['Alice',25,'New York'],['Bob',32,'Los Angeles'],['Charlie',22,'London']],"columns":['Name','Age','City']}

data_type: 可选参数，默认为1。可选值为 1 或 2。当值为 1 时，表示每一行是一条数据；当值为 2 时，表示使用 DataFrame 类型的数据格式。
file_name: 可选参数，文件名称，比如 '默认名称.xlsx'。

rules: 可选参数，导出规则，包括表头设置和数据验证下拉列表等。

freeze：可选参数，表示从第几行第几列开始冻结，比如值为”A2 ”其中2表示第从第2行（行索引从1开始）， A 表示第一列。

#### (2)import_excel参数说明

file :必选参数，二进制excel文件，一般从前端传来的 self.request.FILES['file'] 中获取
check_dict:可选参数，校验的对象 ，其中header表示必须必须有那些列，content表示那些列 必填、而且指定类型，

type_dict:可选参数，
判断非表头的数据类型，可传入配置设置可校验类型，不传时默认值如下{
            "str": str,
            "int": int,
            "float": float,
            "bool": bool,
            "datetime": pd.to_datetime,
        }

## 3.应用实例
### （1）export_excel例子：
from hzexcel import export_excel
rules = {
    "head": {"Font": {"bold": True, "color": "FF0000", "size": 14}},
    "validation": [
        {
            "column_name": "Name",
            "type": "list",
            "formula1": '"$ 价格,A 可获得性,P 包装,P 性能,E 易用性,A 保证,L 生命周期成本,S 社会影响力"',
            "showDropDown": False,
        }
    ],
}
data = {
    '测试': ['Alice', 'Bob', 'Charlie'],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 32, 22],
    'City': ['New York', 'Los Angeles', 'London']
}
return export_excel(data, 2, '默认名称.xlsx', rules, "A2")


## （2）export_excel例子：
from hzexcel import import_excel
self.request = request
file = self.request.FILES['file']
check_dict = {
    "header": ['Name', 'Age', 'City'],
    "content": {'Name': 'str', 'City': 'str'}
}

rs0 = import_excel(file, check_dict)
rs = json.loads(rs0)
if rs['status']:
    #  通过验证
    # 将文件中的数据转为数据 ，批量插入到数据库
    if rs['status'] == 200:
        return Response(rs, status=status.HTTP_200_OK)
    else:
        return Response(f"{rs['msg']}", status=status.HTTP_400_BAD_REQUEST)
else:
    return Response(f"校验数据时出错", status=status.HTTP_400_BAD_REQUEST)
