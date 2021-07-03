# // Importing required Libraries

import os 
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity 

# // Importing values in the required variables 

student_files = [doc for doc in os.listdir() if doc.endswith('.txt')]
student_notes =[open(File).read() for File in  student_files]

# // Calling Functions and Storing results

vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()
similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])

# // Vectorizing the imported values and zipping them into a list

vectors = vectorize(student_notes)
s_vectors = list(zip(student_files, vectors))

# // Function to check Plagiarism

def check_plagiarism():
    plagiarism_results = set()      # // Initializing the empty set
    global s_vectors        # // Declaring the global variable s_vector
    for student_a, text_vector_a in s_vectors:      # // Iterative loop 
        new_vectors =s_vectors.copy()       # // Creating a copy variable
        current_index = new_vectors.index((student_a, text_vector_a))   # // Finding index of the value from list
        del new_vectors[current_index]      # // Deleting the value at current_index in new_vector
        for student_b , text_vector_b in new_vectors:       # // Iterative loop
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]      # // Checking similarity
            student_pair = sorted((student_a, student_b))       # // Sorting the values
            score = (student_pair[0], student_pair[1],sim_score)        # // Storing the values in desired manner
            plagiarism_results.add(score)       # // Adding the score to plagiarism_results set
    return plagiarism_results       # // Returing the result

# // Printing the final result

for data in check_plagiarism():
    print("Similarity between",data[0],"and",data[1],":",round(data[2]*100,3))