class file:
    __path, __mode, __file = "", "r", ""

    def __init__(self, path, mode="r"):
        self.__path = path
        self.__mode = mode
        self.__open()

    def __open(self):
        """
        @param None
        ##Open & assignment the content file in the private attribute __file
        @return None
        """
        try:
            with open(self.__path, self.__mode) as file:
                self.__file = file.read()
                file.close()
        except IOError:
            print("Cannot open: "+self.__path)

    def getExtension(self):
        """
        @param None
        ##Get Extension of file
        @return String
        """
        return (self.__path.partition("."))[-1]

    def getPath(self):
        """
        @param None
        Get the path of file
        @return String
        """
        return self.__path

    def readFile(self):
        """
        @param None
        Return content of file
        @return List
        """
        return self.__file

    def setPath(self, path):
        """
        @param String
        Set a new path
        @return None
        """
        self.__path = path
