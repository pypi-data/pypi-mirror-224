class LoginException(Exception):
    def __init__(self, e_str):
        Exception.__init__(self, 'Login failed, the original exception message: \n' + e_str)


class ObjInitException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Object initializing error! Please check input.')


class NotLoginException(Exception):
    def __init__(self):
        Exception.__init__(self, 'You have not login yet. Please use login function to get an ssid')
