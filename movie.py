import spacy
import operator

def get_next(strinput):
	#Load Spacy
	#nlp = spacy.load("en") 
	nlp = spacy.load("en_core_web_md")
	#Initialize filename
	filename = "movies.txt"

	#Initialize dictionaries
	title_text = {}
	simranking = {}

	#Read file into 1st dictionary
	with open(filename) as f:
	    for line in f:
	       (key, val) = line.split(":")
	       title_text[str(key)] = val

	#Compare input text with text value of description from file
	for keys,values in title_text.items():
	    main_txt = nlp(strinput)
	    search_txt = nlp(str(values))
	    simranking.update( {str(keys) : main_txt.similarity(search_txt)} )


	# for keys,values in simranking.items():
	# 	print(keys)
	# 	print(values)    

	#Return the Key (Movie name) with the highest similarity score   
	return max(simranking.items(), key=operator.itemgetter(1))[0]



#Pass in input text
strinput = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator"
print(get_next(strinput))