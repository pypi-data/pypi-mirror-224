from .file import HzFileExportTools


def export_excel(data: None, data_type=1, file_name='默认名称.xlsx', rules=None, freeze=None):
    """
    根据参数导出对应excel

    入参：
        data: 数据
        data_type: 可选值（1,2），为1是每一行是一条数据    为2时dataframe 这种数据格式
        file_name： 文件名称
        hz_rules: 导出的规则： {}
    返回 excel 文件
    """

    file_export_util = HzFileExportTools(data, data_type, file_name, rules, freeze)

    return file_export_util.exportResponse()


