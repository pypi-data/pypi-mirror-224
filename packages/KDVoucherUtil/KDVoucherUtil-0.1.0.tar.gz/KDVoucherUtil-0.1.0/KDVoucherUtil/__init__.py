class NotLoginException(Exception):
    def __init__(self):
        Exception.__init__(self, 'You have not login yet. Please use login function to get an ssid')
