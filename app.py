import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        extracted_text = page.extract_text()
        if extracted_text:  # Avoid NoneType issues
            text += extracted_text + "\n"
    return text if text else "No extractable text found"

# Function to rank resumes based on job description
def rank_resumes(job_description, resumes):
    # Combine job description with resumes
    documents = [job_description] + resumes  # Fixed list assignment

    # Convert text to TF-IDF vectors
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()

    # Calculate cosine similarity
    job_description_vector = vectors[0]  # First vector is job description
    resume_vectors = vectors[1:]  # Rest are resumes
    cosine_similarities = cosine_similarity([job_description_vector], resume_vectors).flatten()  

    return cosine_similarities

# Streamlit app
st.title("AI Resume Screening & Candidate Ranking System")

# Job Description Input
st.header("Job Description")
job_description = st.text_area("Enter the Job Description")

uploaded_files = st.file_uploader("Upload PDF Files", type=["pdf"], accept_multiple_files=True)

if uploaded_files and job_description:
    st.header("Ranking Resumes")

    resumes = []
    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        resumes.append(text)

    # Rank Resumes
    scores = rank_resumes(job_description, resumes)

    # Display Scores
    results = pd.DataFrame({"Resume": [file.name for file in uploaded_files], "Score": scores})
    results = results.sort_values(by="Score", ascending=False)

    # Format the output
    results["Score"] = results["Score"].apply(lambda x: round(x, 4))  

    st.write(results)