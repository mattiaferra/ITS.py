class Film:
    def __init__(self,id : int ,title : str):
        
        self.__id = id
        self.__title = title

    def setID(self,id):

        self.__id = id


    def setTitle(self,title):

        self.__title = title

    def getID(self,id):

        return self.__id
    
    def getTitle(self,title):

        return self.__title
    
    def isEqual(self,otherFilm):

        if not isinstance(otherFilm,Film):
            return False

        return self.__id == otherFilm.getID() 

        