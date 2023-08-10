# -*- coding: utf-8 -*-
"""
@Author: HuangJianYi
@Date: 2021-07-15 11:30:45
@LastEditTime: 2023-08-09 19:01:10
@LastEditors: HuangJianYi
@Description: 
"""
from seven_framework.file import COSHelper
from seven_framework import *
from seven_cloudapp_frame.libs.common import *


class COS2Helper:
    """
    :description: 腾讯云存储帮助类 上传文件、数据导入excel并返回下载地址
    :param {type} 
    :return: 
    :last_editors: HuangJianYi
    """
    logger_error = Logger.get_logger_by_name("log_error")

    @classmethod
    def get_cos_config(self):
        oss_config = share_config.get_value("cos_config", {})
        self.access_key = oss_config.get("access_key", "")
        self.secret_key = oss_config.get("secret_key", "")
        self.bucket = oss_config.get("bucket", "")
        self.end_point = oss_config.get("end_point", "")
        self.domain = oss_config.get("domain", "")
        self.folder = oss_config.get("folder", "")

    @classmethod
    def upload(self, file_name, data=None, is_auto_name=True):
        """
        :description:上传文件
        :param file_name：文件名称
        :param data：需要上传的数据
        :param is_auto_name: 是否生成随机文件名
        :return: 
        :last_editors: HuangJianYi
        """
        self.get_cos_config()
        if is_auto_name == True:
            file_extension = os.path.splitext(file_name)[1]
            file_name = UUIDHelper.get_uuid().replace("-", "") + file_extension
        object_name = self.folder + "/" + file_name
        result = COSHelper(self.access_key, self.secret_key, self.end_point).put_file(self.bucket, object_name, data)
        if result == True:
            return self.domain + "/" + object_name
        else:
            return ""

    @classmethod
    def put_file_from_file_path(self, local_file=''):
        """
        :description:上传文件根据路径
        :param local_file：本地文件地址
        :return: 
        :last_editors: HuangJianYi
        """
        self.get_cos_config()
        file_name = os.path.basename(local_file)
        object_name = self.folder + "/" + file_name
        result = COSHelper(self.access_key, self.secret_key, self.end_point).put_file_from_file_path(self.bucket, object_name, local_file)
        if result == True:
            return self.domain + "/" + object_name
        else:
            return ""

    @classmethod
    def export_excel(self, import_data):
        """
        :description: 把数据导入excel并返回下载地址
        :param import_data:导入数据
        :return excel下载地址
        :last_editors: HuangJianYi
        """
        resource_path = ""
        if import_data:
            try:
                if not os.path.exists("temp"):
                    os.makedirs("temp")
                path = "temp/" + UUIDHelper.get_uuid() + ".xlsx"
                ExcelHelper.export(import_data, path)
                resource_path = self.put_file_from_file_path(path)
                os.remove(path)
            except Exception as ex:
                self.logger_error("【数据导入excel】" + traceback.format_exc())
        return resource_path