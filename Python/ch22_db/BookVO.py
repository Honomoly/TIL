class BookVO:
    def __init__(self, bNo, bName, bAuthor, bPrice, bDate, bStock, pubNo):
        self.__bNo = bNo
        self.__bName = bName
        self.__bAuthor = bAuthor
        self.__bPrice = bPrice
        self.__bDate = bDate
        self.__bStock = bStock
        self.__pubNo = pubNo
    
    # getter
    def get_bNo(self):
        return self.__bNo
    
    def get_bName(self):
        return self.__bName
    
    def get_bAuthor(self):
        return self.__bAuthor
    
    def get_bPrice(self):
        return self.__bPrice
    
    def get_bDate(self):
        return self.__bDate
    
    def get_bStock(self):
        return self.__bStock
    
    def get_pubNo(self):
        return self.__pubNo
    
    def get_all(self):
        return (self.__bNo, self.__bName, self.__bAuthor, self.__bPrice, self.__bDate, self.__bStock, self.__pubNo)
    
    # setter
    def set_bNo(self, bNo):
        self.__bNo = bNo

    def set_bName(self, bName):
        self.__bName = bName
    
    def set_bAuthor(self, bAuthor):
        self.__bAuthor = bAuthor
    
    def set_bPrice(self, bPrice):
        self.__bPrice = bPrice
    
    def set_bDate(self, bDate):
        self.__bDate = bDate
    
    def set_bStock(self, bStock):
        self.__bStock = bStock
    
    def set_pubNo(self, pubNo):
        self.__pubNo = pubNo