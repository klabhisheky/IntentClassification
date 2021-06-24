
# Dataset : Contains Singleton classes related to Input data and Indexed data (by indexer for faster query execution)
import json
from app.PreProcessor import PreProcessor


""" Index Table (Singleton):  is the output from Indexer module, that indexes information already known about intents 
                              in a certain way to help faster query execution (more in INDEXER module) """

class IndexTable:
   __instance = None
   __data = None

# getTable() : static method to provide access to IndexTable
# returns : reference to Object of IndexTable
   @staticmethod 
   def getTable():
      # Static access method.
      if IndexTable.__instance == None:
         IndexTable()
      return IndexTable.__instance

# isValidToken : check if token is valid (present in dataset:bool)
# returns bool 
   def isValidToken(self, token):
      if self.__data is None: return False
      try:
         self.__data[token]
         return True
      except: return False

# getPosting() 
# input : token 
# returns posting list : for input token
   def getPosting(self,token):
      return self.__data[token]

# Filter Invalid words to out dataset, which will not account to intent classification and might raise exception when accessing dictionary
# input  - string: query
# output - string: string of only vaild words
   def filterInvalidWords(self,query=""):
      query_list = query.split()
      invalid_words_list = list()
      valid_words = str()
      for token in query_list:
         if not self.isValidToken(PreProcessor.getStemmedToken(token)):
            invalid_words_list.append(token)
      for token in invalid_words_list:
         query_list.remove(token)
      for token in query_list:
         valid_words += " " + token
      return valid_words   

# construtor()
   def __init__(self):
      """ Virtually private constructor. """
      if IndexTable.__instance != None:
         raise Exception("ObjCreation")
      else:
         try:
            with open('app/dataset.json', 'r') as file:
               json_data = file.read()
            IndexTable.__data = json.loads(json_data)
            IndexTable.__instance = self
         except IOError : print("LOG:[ERROR] Unable to locate dataset.json!")



""" Input Table (Singleton):  stores data from CSV into more manageable way (JSON) """
class InputTable:
   __instance = None
   __data = None

   # getTable() : static method to provide access to InputTable
   # returns : reference to Object of InputTable  
   @staticmethod 
   def getTable():
      """ Static access method. """
      if InputTable.__instance == None:
         InputTable()
      return InputTable.__instance

   # getClass() : provides the class on document_id
   # returns : class [Prodecude , Cost , Hospital etc.]    
   def getClass(self, document_id):
      return self.__data[document_id]['class']

   # constructor
   def __init__(self):
      """ Virtually private constructor. """
      if InputTable.__instance != None:
         raise Exception("ObjCreation")
      else:
         try:
            with open('app/inputTable.json', 'r') as file:
               json_data = file.read()
            InputTable.__data = json.loads(json_data)
            InputTable.__instance = self
         except IOError : print("LOG:[ERROR] Unable to locate inputTable.json!") 