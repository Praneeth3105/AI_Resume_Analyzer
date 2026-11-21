import re
import streamlit as st
from pypdf import PdfReader
from docx import Document

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")

ROLE_SKILLS = {
    "Python Developer": ["python", "oops", "sql", "git", "flask", "django", "api", " problem solving"],
    "Web Developer": ["html", "css", "javascript", "react", "node.js", "sql", "git", "api"],
    "Data Analyst": ["python", "sql", "excel", "power bi", "tableau", "statistics", "pandas", "data visualization"],
    "AI / ML Intern": ["python", "machine learning", "deep learning", "pandas", "numpy", "nlp", "tensorflow", "prompt engineering"],
    "General Software Intern": ["python", "java", "c++", "sql", "html", "css", "javascript", "git"]
}

def extract_text(uploaded_file):
    name = uploaded_file.name.lower()
    if name.endswith(".txt"):
        return uploaded_file.getvalue().decode("utf-8", errors="ignore")
    if name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    if name.endswith(".docx"):
        doc = Document(uploaded_file)
        return "\n".join(p.text for p in doc.paragraphs)
    return ""

def analyze_resume(text, role):
    normalized = re.sub(r"\s+", " ", text.lower())
    skills = ROLE_SKILLS[role]
    found = [skill.strip() for skill in skills if skill.strip() in normalized]
    missing = [skill.strip() for skill in skills if skill.strip() not in normalized]
    score = round((len(found) / len(skills)) * 100) if skills else 0

    sections = {
        "Email address": bool(re.search(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)),
        "Phone number": bool(re.search(r"(?:\+?\d[\d\s()-]{8,}\d)", text)),
        "Education section": "education" in normalized,
        "Projects section": "project" in normalized,
        "Experience section": "experience" in normalized or "internship" in normalized,
    }
    
    suggestions = []
    if not sections["Email address"]: suggestions.append("Add a professional email address.")
    if not sections["Phone number"]: suggestions.append("Add a contact phone number.")
    if not sections["Education section"]: suggestions.append("Include a clearly labelled Education section.")
    if not sections["Projects section"]: suggestions.append("Add 1–2 projects and explain your contribution and technologies.")
    if not sections["Experience section"]: suggestions.append("Add internship, volunteering, or practical experience if available.")
    if missing: suggestions.append("Consider learning or highlighting these role-related skills: " + ", ".join(missing) + ".")
    if len(text.split()) < 100: suggestions.append("Your resume looks very short. Add relevant details, projects, coursework, and achievements.")
    if not suggestions: suggestions.append("Good start! Keep your resume concise and tailor it to each job description.")
    return score, found, missing, sections, suggestions


st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get a simple skill match report for your chosen job role.")
st.info("This beginner-friendly demo uses text extraction and rule-based analysis. It does not send your resume to an external AI service.")

col1, col2 = st.columns([1, 1])
with col1:
    role = st.selectbox("Choose your target job role", list(ROLE_SKILLS.keys()))
with col2:
    uploaded = st.file_uploader("Upload resume (PDF, DOCX or TXT)", type=["pdf", "docx", "txt"])

if uploaded:
    try:
        resume_text = extract_text(uploaded)
        if not resume_text.strip():
            st.error("No readable text was found. Try a text-based PDF, DOCX or TXT file.")
        else:
            score, found, missing, sections, suggestions = analyze_resume(resume_text, role)
            st.divider()
            st.subheader("Analysis Result")
            a, b, c = st.columns(3)
            a.metric("Role match score", f"{score}%")
            b.metric("Matching skills", len(found))
            c.metric("Skills to add", len(missing))
            st.progress(score / 100)

            left, right = st.columns(2)
            with left:
                st.markdown("### ✅ Skills found")
                if found:
                    st.success(" • ".join(found))
                else:
                    st.write("No matching skills detected yet.")
            with right:
                st.markdown("### 📌 Skills not found")
                if missing:
                    st.warning(" • ".join(missing))
                else:
                    st.success("All listed role skills were found.")

            st.markdown("### Resume section checklist")
            for section, present in sections.items():
                st.write(("✅ " if present else "❌ ") + section)

            st.markdown("### Suggestions to improve your resume")
            for item in suggestions:
                st.write("- " + item)

            st.download_button("Download analysis as TXT", "AI RESUME ANALYSIS\n\nTarget role: " + role + f"\nMatch score: {score}%\n\nSkills found: {', '.join(found)}\nSkills not found: {', '.join(missing)}\n\nSuggestions:\n" + "\n".join("- " + s for s in suggestions), file_name="resume_analysis.txt")
            with st.expander("View extracted resume text"):
                st.text(resume_text[:12000])
    except Exception as exc:
        st.error(f"Could not read this file: {exc}")
else:
    st.caption("Choose a job role and upload a resume to begin.")

st.divider()
st.caption("Minor Project Demo | Python + Streamlit")