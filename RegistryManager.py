import winreg


class RegMan:
    _VERSION = "1.0"

    def __init__(self):
        self.regAccess = None
        self.accessKey = None

    def setRegAccess(self, winregType, name=None):
        """
        The setRegAccess function is used to set the registry access type.


        :param self: Represent the instance of the class
        :param winregType: Specify the type of registry to connect to
        :param name: Specify the name of the host
        :return: True if the connection is successful
        """
        try:
            self.regAccess = winreg.ConnectRegistry(name, winregType)
            return True
        except Exception as e:
            return False

    def setAccessKey(self, regPath):
        """
        The setAccessKey function is used to set the registry key that will be accessed.
            The function takes a single argument, regPath, which is the path of the registry key.
            If successful, it returns True; otherwise it returns False.

        :param self: Represent the instance of the class
        :param regPath: Specify the path to the registry key
        :return: True if key was opened
        """
        if self.regAccess == None:
            return False
        self.accessKey = winreg.OpenKey(self.regAccess, regPath)
        return True

    def readEnumKey(self, index):
        """
        The readEnumKey function is used to enumerate the subkeys of a key.
            The function takes in an index as a parameter and returns the name of
            the subkey at that index. If there are no more keys, it returns False.

        :param self: Represent the instance of the class
        :param index: Specify the index of the key to be read
        :return: The value at the index
        """
        if self.accessKey == None:
            return False
        return winreg.EnumKey(self.accessKey, index)

    def queryValue(self, value):
        """
        The queryValue function takes a value as an argument and returns the value of that key.
        If the accessKey is None, it will return False.

        :param self: Represent the instance of the class
        :param value: Specify the value name to query
        :return: The registry value
        """
        if self.accessKey == None:
            return False
        return winreg.QueryValueEx(self.accessKey, value)

    def closeAccessKey(self):
        """
        The closeAccessKey function closes the registry key that was opened by the openAccessKey function.

        :param self: Represent the instance of the class
        :return: True if closed
        """
        try:
            winreg.CloseKey(self.accessKey)
            return True
        except:
            return False
