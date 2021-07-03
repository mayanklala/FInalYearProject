import os, pathlib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

student_files = [doc for doc in pathlib.Path("docs").iterdir() if doc.is_file()]
student_notes = [open(File).read() for File in student_files]

vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()
similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])

vectors = vectorize(student_notes)
s_vectors = list(zip(student_files, vectors))

def check_plagiarism():
    plagiarism_results = set()
    global s_vectorss
    for student_a, text_vector_a in s_vectors:
        new_vectors = s_vectors.copy()
        current_index = new_vectors.index((student_a, text_vector_a))
        del new_vectors[current_index]
        for student_b, text_vector_b in new_vectors:
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            student_pair = sorted((student_a, student_b))
            score = (student_pair[0], student_pair[1], sim_score)
            plagiarism_results.add(score)
    plag_res_str=[]
    for data in plagiarism_results:
        dat1 = str(data[0])
        dat1_f = dat1[5::]
        dat2 = str(data[1])
        dat2_f = dat2[5::]
        plag_res_str.append("Similarity between "+dat1_f+" and "+dat2_f+" : "+str(round(data[2]*100,3)))
    return plag_res_str

for data in check_plagiarism():
    print(data)