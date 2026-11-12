# AI Resume Analyzer (Minor Project)

A beginner-friendly Python web application that reads a resume and produces a role-based skill match report, a simple score, a section checklist, and improvement suggestions.

## Features
- Upload a PDF, DOCX, or TXT resume.
- Select a target role.
- Extract resume text locally.
- Compare resume text with a small role-based skill list.
- Show a match score, missing skills, section checklist, and suggestions.
- Download the analysis as a TXT file.

## Requirements
- Python 3.9 or newer
- Internet connection for the first-time package installation

## Run on Windows
1. Extract the ZIP file.
2. Open the extracted `AI_Resume_Analyzer` folder.
3. Open Command Prompt or PowerShell in that folder.
4. Create a virtual environment:

   ```bash
   py -m venv venv
   ```

5. Activate it:

   ```bash
   venv\Scripts\activate
   ```

6. Install packages:

   ```bash
   pip install -r requirements.txt
   ```

7. Start the application:

   ```bash
   streamlit run app.py
   ```

8. The app will open in your browser. If it does not, open the local URL shown in the terminal (usually `http://localhost:8501`).

## Run on macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Test it
Upload the included `sample_resume.txt` file and select `Python Developer` or `General Software Intern`.

## Important project note
This is an educational, rule-based prototype. The score is a simple keyword match against the built-in skill list; it is not a professional hiring score and does not use a live LLM. You can later extend it with Prompt Engineering and an LLM API if your guide requires a genuine generative-AI integration.

## Main files
- `app.py` — complete application code
- `requirements.txt` — Python dependencies
- `sample_resume.txt` — sample file for testing
