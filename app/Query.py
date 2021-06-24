from app.PreProcessor import PreProcessor
from app.dataset import IndexTable, InputTable

# Query keeps track of all the information user is trying to make and provides functions to execute query
class Query:
	def __init__(self, query_string=""):
		self.__query_string 	= query_string
		self.__query_token_list = IndexTable.getTable().filterInvalidWords(PreProcessor.removeStopWords(query_string)).split()
		self.__query_posting_list = [IndexTable.getTable().getPosting(PreProcessor.getStemmedToken(token)) for token in self.__query_token_list]

	# getQueryString()
	# input 	- void
	# output - string: query of user
	def getQueryString(self):
		return self.__query_string


	# getQueryTokenList()
	# input 	- void
	# output - string: returns list of tokens (words) from query input
	def getQueryTokenList(self):
		return self.__query_token_list

	# getQueryPostingList()
	# input 	- void
	# output - string: returns list of all the locations(ids) of respective token in order of their appearance in dataset (made from input CSV by Indexer Module)	
	def getQueryPostingList(self):
		return self.__query_posting_list

	# andPosting()
	# input 	- posting_l , posting_r : List of row_ids from dataset for two tokens to perform AND query - eg. EXECUTE(token_left AND token_right)
	# output - resultant posting : return list, after performing AND	
	def andPosting(self, posting_l, posting_r):
		position_l = int(0)
		position_r = int(0)
		resultant_posting = list()
		while(position_l < len(posting_l) and position_r < len(posting_r)):
			if(posting_l[position_l] == posting_r[position_r]):
				resultant_posting.append(posting_l[position_l])
				position_l += 1
				position_r += 1
			elif posting_l[position_l] < posting_r[position_r]:
				position_l += 1
			else:
				position_r += 1
		return resultant_posting 


	# AND() : Perform multi-level AND operation , eg EXECUTE(token1 AND token2 AND token3 AND token4)
	# input 	- low , high : index of subarray [low, high) to perform AND, 
	# output - resultant posting : return list, after performing multi-AND
	def AND(self, low, high):
		partial_result = self.__query_posting_list[low]
		partial_looked_query = self.__query_token_list[low]
		for index in range(low+1 , high):
			partial_result = self.andPosting(partial_result, self.__query_posting_list[index])
			if not partial_result: return None
			partial_looked_query += " " + self.__query_token_list[index]
		unique_class_set = set()
		for document_id in partial_result:
			unique_class_set.add(InputTable.getTable().getClass(str(document_id)))
		return { partial_looked_query : [ uclass for uclass in unique_class_set ] }




