import unittest
from HTMLTestReportCN import HTMLTestRunner

path = 'D:\\new-onedrive\\OneDrive - hqu.edu.cn(1)\\Workspace\\study-notes\\python-api-automation\\api_test_framework'
suite = unittest.defaultTestLoader.discover("./")
suite = unittest.defaultTestLoader.discover(path, pattern='test_*.py')

f = open("report.html", 'wb')  # 二进制写格式打开要生成的报告文件
HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="卡卡").run(suite)
f.close()
