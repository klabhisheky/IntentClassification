import nltk


# Utility like class for nltk kind preprocessing for dataset easy to searching
class PreProcessor:

	# remove stop words from the query, words like {Me , I , You , would , should} will not contricute towards intent classification
	# input 	- string: input_string
	# output - string: without stopwords 
	@staticmethod
	def removeStopWords(input_string=""):
		input_tokens = input_string.split()
		processed_string = str()
		for token in input_tokens:
			if token not in (nltk.corpus.stopwords.words('english')):
				processed_string += " " + token
		return processed_string

	# Combine multiple orientation of similar words into one , for better classification, {transplant, transplated, trasplatation, transplant => transplant}
	# input 	- string: query
	# output - string: stemmed string of input
	@staticmethod
	def fetchStemmedQuery(query=""):
		query_tokens = query.split()
		stemmed_query = str()
		for token in stemmed_query:
			stemmed_query += " " + nltk.stem.PorterStemmer().stem(token)
		return stemmed_query

	# Stemmed representation for a single word
	# input 	- string: word
	# output - string: stemmed word
	@staticmethod
	def getStemmedToken(token):
		return nltk.stem.PorterStemmer().stem(token)

