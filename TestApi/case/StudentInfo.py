import unittest
import json
from TestApi.config.TEconfig import host_test
from TestApi.common.SendReq import SendReq
from TestApi.common.ReadExcel import readExcel

url = host_test + '/api/user/stu_info'
method = readExcel().get_xls('testfile.xlsx', '获取学生信息接口')[0][0]
class StudentInfo(unittest.TestCase):
    def setUp(self):
        print('---------------------测试开始--------------------')

    def test01_getinfo(self):
        #sql='SELECT * FROM `main`.`app_student` WHERE `name` LIKE ''%白瑞峰%'' LIMIT 0, 1000'
        try:
            par = readExcel().get_xls('testfile.xlsx', '获取学生信息接口')[0][2]
        except:
            print('数据获取失败')
        else:
            result = SendReq().input_method(url,method=method,par=par)
            res = json.loads(result)
            print(res)
            self.assertEqual(res['error_code'],0,msg='成功')

    def test02_getinfo(self):
        # sql='SELECT * FROM `main`.`app_student` WHERE `name` LIKE ''%白瑞峰%'' LIMIT 0, 1000'
        try:
            par = readExcel().get_xls('testfile.xlsx', '获取学生信息接口')[1][2]
        except:
            print('数据获取失败')
        else:
            result = SendReq().input_method(url, method=method, par=par)
            res = json.loads(result)
            print(res)
            self.assertEqual(res['error_code'], 0,msg='失败')

    def test03_getinfo(self):
        # sql='SELECT * FROM `main`.`app_student` WHERE `name` LIKE ''%白瑞峰%'' LIMIT 0, 1000'
        try:
            par = readExcel().get_xls('testfile.xlsx', '获取学生信息接口')[2][2]
        except:
            print('数据获取失败')
        else:
            result = SendReq().input_method(url, method=method, par=par)
            res = json.loads(result)
            print(res)
            self.assertEqual(res['error_code'], 3001,'成功')
    def tearDown(self):
        print('---------------------测试结束--------------------')



