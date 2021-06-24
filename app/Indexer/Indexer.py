from PreProcessor import PreProcessor
from constants import MAP_TABLE
import csv
import json

# Indexer Module indexes CSV data to make efficient and faster execution of a QUERY, It makes use of Inverted Index Tables.

# Inverted Index table Structure : { token : posting_list  }
# It stores for every token that appear in the dataset(CSV) list of Item_id it appears into 

# Input Table Structure : { item_id : [ token_list : Item_class  ] }
# Item is each entry that has been already identified to one of the Intent Classes
# Token list is the list of words inside that item and Item_class is the matched Intent Class 


class Indexer:
	def __init__(self, path_to_csv ='train.csv',  path_to_save_input_table = 'inputTable.json', path_to_save_index_table = 'dataset.json'):
		self.__path_to_csv = path_to_csv
		self.__path_to_save_input_table = path_to_save_input_table
		self.__path_to_save_index_table = path_to_save_index_table
		self.__input_table = dict()
		self.__index_table = dict()

	# createInputTable
	def createInputTable(self):
		try:
			with open(self.__path_to_csv, 'rt', encoding='utf-8-sig') as csv_file:
				csv_reader_obj = csv.reader(csv_file, delimiter=',', quotechar='|')
				index = int(1)
				for row in csv_reader_obj:
					self.__input_table.update( {index : {} } )
					tokens_list = PreProcessor.removeStopWords(row[0]).split()
					self.__input_table[index].update({ 'tokens' : tokens_list, 'class' : MAP_TABLE[row[1]] })
					index += 1
		except IOError :
			print("\nLOG: IOError, Invalid train.csv location")
			exit()

		try:
			with open(self.__path_to_save_input_table, 'w') as out_file:
				if self.__input_table is not {}:
					json.dump(self.__input_table, out_file)
					print("LOG:[MESSAGE] Input Table created.")
				else : print("LOG:[MESSAGE] Empty Input table created.")
		except IOError :
			print("\nLOG: IOError, Unable to open file at " , self.__path_to_save_input_table)
			exit() 

	# createIndexTable
	def createIndexTable(self):
		if self.__input_table == {}:
			print("LOG:[ERROR]Index Table can't be created before input table.")
			return		
		for item_id in self.__input_table:
			stemmed_tokens_list = list()
			for stemmedtoken in  [ PreProcessor.getStemmedToken(token) for token in self.__input_table[item_id]['tokens'] ]:
				# remove duplicates
				if stemmedtoken not in stemmed_tokens_list:
					stemmed_tokens_list.append(stemmedtoken)
			for stemmedtoken in stemmed_tokens_list:
				if stemmedtoken in self.__index_table:
					self.__index_table[stemmedtoken].append(item_id)
				else : self.__index_table[stemmedtoken] = [item_id]
		try:
			with open(self.__path_to_save_index_table, 'w') as out_index_file:
				if self.__index_table is not {}:
					json.dump(self.__index_table, out_index_file)
					print("LOG:[MESSAGE] Index Table created.")
				else : print("LOG:[MESSAGE] Empty Index Table created.")
		except IOError :
			print("\nLOG: IOError, Unable to open file at " , self.__path_to_save_index_table)
			exit()



def main():
	obj_indexer = Indexer()
	obj_indexer.createInputTable()
	obj_indexer.createIndexTable()


if __name__ == "__main__":
	main()