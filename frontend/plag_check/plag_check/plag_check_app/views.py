from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.urls import reverse
import os, pathlib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

student_files = [doc for doc in pathlib.Path("DOCS").iterdir() if doc.is_file()]
student_notes = [open(File).read() for File in student_files]

vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()
similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])

vectors = vectorize(student_notes)
s_vectors = list(zip(student_files, vectors))

def home(request):
    return render(request, 'home.html')

def check_plag(request):
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
    plag_res=[]
    for data in plagiarism_results:
        dat1 = str(data[0])
        dat1_f = dat1[5::]
        dat2 = str(data[1])
        dat2_f = dat2[5::]
        if (data[2]*100)>50:
            plag_res.append([dat1_f, dat2_f, round(data[2]*100,3)])
    if len(plag_res)!=0:
        return render(request, 'res.html',{'plag_res' : plag_res})
    else:
        return render(request, 'res_no.html',{'plag_res_str' : 'No major plagiarism Found'})