from app.Query import Query
from app.dataset import IndexTable
from app.constants import MAP_TABLE

# Facilitates the intent classification query by server
class Parser:


	# parseIntent() : Server communicates to rest of app through this class
	# input : query_string
	# Output : Dict of intents classified 
	@staticmethod
	def parseIntent(query_string):
		index_table = IndexTable.getTable()
		if index_table is None:
			print("LOG:[ERROR] IndexTalbe returned as None inside" , __name__)
			return None
		user_query = Query(query_string)
		found_intent_range_list = list()
		intent_list = list()
		# perform intent classification over all the sub-araay of query token list
		for i in range(len(user_query.getQueryPostingList()) - 1, -1, -1):
			for j in range(0, len(user_query.getQueryPostingList()) - i):
				# Check if this range has already been classified.
				range_already_classified = False
				for range_ in found_intent_range_list:
					if(range_[0] <= j and range_[1] >= j+i):
						range_already_classified = True
						break
				# If range is not completly classified perform Query AND
				if not range_already_classified:
					intent_for_range = user_query.AND(j , j+i+1)
					if intent_for_range is not None:
						found_intent_range_list.append([j, j+i])
						intent_list.append(intent_for_range)
		# Form respone in order with Server demand
		classified_intent_dict = dict()
		for intent in intent_list:
			for q_string, class_list in intent.items():
				for class_type in class_list:
					classified_intent_dict.update({ q_string : MAP_TABLE[class_type]})
		return classified_intent_dict

