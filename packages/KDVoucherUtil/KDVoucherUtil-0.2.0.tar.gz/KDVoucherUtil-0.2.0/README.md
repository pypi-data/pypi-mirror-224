# 金蝶云平台凭证批量处理封装工具。
### 因为依赖包古老，因此需要注意降级pip和setuptools版本，建议降级到pip-20.1.1, setuptools-57.5.0
### 首个版本仅提供基本的登录、导入凭证、删除凭证、查询余额表等功能，后期陆续加上常用财务凭证处理工具。

快速入门：

推送凭证：
````
from Worker import KDUser

voucher_list = [#你的凭证列表]
worker = KDUser(user='0001',  # 用户名
                pwd='123',  # 密码
                domain='https://192.168.0.1:8000',  # 金蝶云远程地址
                sln_name='eas',  # 金蝶数据库配置，可查看客户端登录页面或者咨询DBA
                dc_name='2023',
                language='L2',
                db_type=0,
                auth_pattern='BaseDB')
result = worker.import_vocher(voucher_list)
````

获取科目余额表:
````
trial_balance = worker.get_account_balance('1.01', '2023', '8')
````