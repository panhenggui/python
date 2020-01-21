# 配置
## 在使用前，需要先修改swagger_client目录下的configuration.py文件，修改url、api_key、api_secret和代理服务器
    # Default Base url
    # added by chaiyu 2019-04-01 test url
    self.host = "https://testnet.bitmex.com/api/v1"
    # Temp file folder for downloading files
    self.temp_folder_path = None

    # Authentication Settings
    # dict to store API key(s)
    # self.api_key = {}
    # added by chaiyu 2019-04-01 test api_key and secret
    self.api_key = "DGx77wCrTaUuZSudNjoQKJ7F"
    # API secret
    self.api_secret = "jq6H_z4ZBUlLLcfyIXzf_pkGr0j06-bejAKJaHcNM-LYwUGf"
    # dict to store API prefix (e.g. Bearer)
    self.api_key_prefix = {}
    
    # Proxy URL 这里配置代理服务器 added by chaiyu 2019-04-01
    self.proxy = "http://127.0.0.1:1087"
    # Safe chars for path_param
    self.safe_chars_for_path_param = ''
# 安装
## 然后在本目录下执行，安装swagger_client
    python setup.py install
    
## 安装bravado（验签器的依赖）
    pip install bravado
      
# 测试代码
## 位于test目录下，测试代码采用的是unittext，test_order_api.py里面有我写的一个样例代码
    def test_order_new(self):
    """Test case for order_new

    Create a new order.  # noqa: E501
    """

    # 这里可以使用pandas去读取excel作为配置文件 added by chaiyu 2019-04-01
    kwargs = {"symbol": "XBTUSD", "async": "false", "order_qty": 1}
    result = self.api.order_new(**kwargs)
    print("result: " + result.ord_status)

    # 下面写预期值 added by chaiyu 2019-04-01
    assert(result.ord_status == "Filled")
    pass

# 执行
## 在test目录下使用python2去执行，因为代码里面的语法是python2的，python3执行会报告错误
    python test_order_api.py
    
    得到了类似下面的结果：
    ......
    result: Filled
    ..
    ----------------------------------------------------------------------
    Ran 9 tests in 3.227s

    OK
看到OK，表示测试通过


附录：
在执行过程中遇到问题：
在执行脚本时，系统报错，错误显示为访问VPN链接时失败。起初认为是使用的vpn问题，但是经过查找错误，并不是因为使用VPN的错误。
错误的造成主要分为两点：
1.导入的脚本目录结构没有设置成sources Root格式。所以在运行脚本时导致在找依赖时，并没有在当前的目录里面去寻找，而是直接访问的是python的根目录里面的内容导致运行失败。
2.添加的APIKey没有委托权限导致运行时报错。
