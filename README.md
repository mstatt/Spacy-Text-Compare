# Spacy-Text-Compare
 Compare text input to file loaded into a dictionary to return the most similar string using spacy.
 
 THe function is supplied a text srting. Example used is a movie description. 
 
Then function reads in a file with txext seperated by ":".
 Example:
 Movie title : Description text.
 
 Using a loop, it goes through the dictionay values containing the descriptions and compares them to the supplied input description or text.
 
 Using spacy's (.similarity) function it scores the text based on similarity.
 
 THen returns the movie title with the highest score for similarity.
 
 This can be modified for all sorts of uses, this is just the initial fully functional example.
 
 
 #Using Anaconda Python 3+, with spacy installed and (nlp = spacy.load("en_core_web_md")) loaded.
