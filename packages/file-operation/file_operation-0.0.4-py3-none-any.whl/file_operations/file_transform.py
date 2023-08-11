# -*- coding: utf-8 -*-
"""
@Time : 2023/8/10 14:54 
@Author : skyoceanchen
@TEL: 18916403796
@项目：文件使用
@File : file_transform.by
@PRODUCT_NAME :PyCharm
"""
from config import *


class PandocOperations(object):

    def md_pdf(self, md_path, pdf_path):
        system = f'{PANDOC}  {md_path} -o {pdf_path}'
        print(system)
        os.system(system)

    def md_doc(self, md_path, pdf_path):
        system = f'{PANDOC}  {md_path} -o {pdf_path}'
        print(system)
        os.system(system)


if __name__ == '__main__':
    PandocOperations().md_doc(r"F:\StudyContent\PythonPro\mytestpy10\智能决策\使用说明\readme.md", "1.DOCX")
