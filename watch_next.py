""" Function to return which movies a user would watch next taking in consideration the last watched movie"""

import spacy  

# Load a pre-trained model with the English language for text similarity.
nlp = spacy.load('en_core_web_md') 


""" Open the file containing movie titles and descriptions. The relative path 'movies.txt' is used as the current working directory
contains the necessary information to locate the file """ 
with open('movies.txt', 'r') as file:
    doc_text = file.readlines()
   
# Description of the last movie the user watched, used as a parameter to find similarities with movie descriptions in the file
description = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,
the Illuminati trick hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace.
Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator'''

# Process the description using the spaCy natural language processing model to check for similarities with movie descriptions
description_doc = nlp(description)  

# Variables to store the maximum similarity value and the name of the movie with the highest similarity 
max_similarity = 0.0
best_movie = ''

# Iterate through the file to identify similarities with the description/parameter
for movie in doc_text:
    # Remove leading/trailing whitespaces using .strip()
    movie_doc = nlp(movie.strip())
    # Compute similarity between each movie description and the provided description/parameter
    similarity = movie_doc.similarity(description_doc)
    
    # Update the movie with the highest similarity
    if similarity > max_similarity:
        max_similarity = similarity
        best_movie = movie.strip()
   
print("\nBecause you watched 'Planet Hulk', have a look at:")    

# Separate the movie title from the description and print only the movie title.
# Split the sentence at the ':' sign and take the first part [0]
print('\n *** ' + best_movie.split(":")[0] + '***')
    



