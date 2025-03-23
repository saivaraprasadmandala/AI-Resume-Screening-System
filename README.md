# AI Resume Screening & Candidate Ranking System

## 📌 Overview
The **AI Resume Screening & Candidate Ranking System** automates the recruitment process by analyzing resumes and ranking candidates based on job descriptions. The system leverages **TF-IDF (Term Frequency-Inverse Document Frequency)** and **Cosine Similarity** to assess how well a candidate's resume matches a given job role. It extracts text from PDFs, processes it using **Natural Language Processing (NLP)** techniques, and provides recruiters with a ranked list of candidates.

## 🚀 Features
- **Automated Resume Parsing**: Extracts text from PDF resumes using `PyPDF2`.
- **Intelligent Candidate Ranking**: Uses TF-IDF and Cosine Similarity to evaluate resumes against job descriptions.
- **User-Friendly Interface**: Built with `Streamlit` for an interactive and easy-to-use UI.
- **Data Preprocessing**: Cleans and normalizes text for better comparison.
- **Customizable Matching Criteria**: Allows recruiters to fine-tune keyword importance.
- **Secure & Fast Processing**: Handles multiple resumes efficiently.

## 🛠️ Tech Stack
- **Programming Language**: Python 🐍
- **Frontend Framework**: Streamlit 🎨
- **Backend Libraries**: 
  - `scikit-learn` (TF-IDF & Cosine Similarity)
  - `PyPDF2` (PDF Text Extraction)
  - `NLTK` (Natural Language Processing)
  - `Pandas` (Data Handling)

## 🎯 How It Works
1. **Upload Resumes**: The recruiter uploads multiple PDF resumes.
2. **Enter Job Description**: The system takes a job description as input.
3. **Preprocessing**: 
   - Extracts text from PDFs.
   - Cleans and tokenizes text using NLP.
   - Applies TF-IDF vectorization.
4. **Resume Scoring**: 
   - Computes Cosine Similarity scores between each resume and the job description.
   - Generates a ranked list based on relevance.
5. **Display Results**: The top-ranked resumes are shown to the recruiter with their similarity scores.

## 📂 Project Structure
```
📁 AI-Resume-Screening-System
│── 📄 app.py               # Main application file (Streamlit UI)
│── 📄 requirements.txt     # Required Python libraries
│── 📄 README.md            # Project documentation
```

## 🔧 Installation & Setup
### Step 1: Clone the Repository
```bash
git clone https://github.com/saivaraprasadmandala/AI-Resume-Screening-System.git
cd AI-Resume-Screening-System
```

### Step 2: Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
streamlit run app.py
```

## 📸 Screenshots
### ✅ Uploading Resumes & Job Description
![Upload](https://github.com/user-attachments/assets/c1600fa2-40c8-4da7-a88f-c65f13c1e0da)

### ✅ Ranked Candidate List
![Ranking](https://github.com/user-attachments/assets/e9f61b76-24b2-469c-b04a-c3e790ccf771)

## 🤝 Contributing
Contributions are welcome! Feel free to submit an issue or a pull request.

## 📬 Contact
**Sai Vara Prasad Mandala**  
🔗 [GitHub](https://github.com/saivaraprasadmandala)  
🔗 [LinkedIn](https://linkedin.com/in/saivaraprasadmandala)  
🔗 [Email](mailto:mandalasaivaraprasad@gmail.com)


---

⭐ If you found this project useful, consider giving it a **star** on GitHub!
