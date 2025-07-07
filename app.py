import streamlit as st
import fitz  # PyMuPDF

# STEP 1: Job keywords
job_keywords = {
    "Data Analyst": [
        "excel", "sql", "python", "tableau", "power bi",
        "statistics", "data visualization", "data cleaning"
    ],
    "Machine Learning Engineer": [
        "python", "pandas", "tensorflow", "keras", "scikit-learn",
        "deep learning", "nlp", "model deployment"
    ],
    "Frontend Developer": [
        "html", "css", "javascript", "react", "ui/ux",
        "figma", "responsive design", "web development"
    ]
}

# STEP 2: PDF text extractor
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text.lower()

# STEP 3: Keyword matcher
def match_keywords(resume_text, selected_keywords):
    found = [kw for kw in selected_keywords if kw in resume_text]
    missing = [kw for kw in selected_keywords if kw not in resume_text]
    score = int((len(found) / len(selected_keywords)) * 100)
    return found, missing, score

# STEP 4: Streamlit UI
st.set_page_config(page_title="Resume Scanner App", page_icon="📄")
st.title("📄 Resume Keyword Scanner")

uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

job_role = st.selectbox("Select the job role you’re applying for:", list(job_keywords.keys()))

if uploaded_file and job_role:
    resume_text = extract_text_from_pdf(uploaded_file)
    found, missing, score = match_keywords(resume_text, job_keywords[job_role])
    
    st.subheader(f"🎯 Match Score: {score}%")
    st.progress(score)

    st.markdown("✅ **Keywords Found in Resume:**")
    st.write(found)

    st.markdown("❌ **Missing Keywords:**")
    st.write(missing)