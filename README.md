# AI Resume Analyzer

An AI Resume Analyzer built using Python and Streamlit that evaluates resumes against selected job roles and generates a role-based skill matching report. It extracts resume content, calculates a skill match score, identifies missing skills, checks important resume sections, and provides suggestions for improvement.

## Features

- **Resume Upload:** Upload resumes in PDF, DOCX, and TXT formats.
- **Role Selection:** Choose a target job role for resume evaluation.
- **Text Extraction:** Extract text from uploaded resumes.
- **Skill Matching:** Compare resume skills against predefined job-role requirements.
- **Match Score:** Generate a simple percentage-based skill matching score.
- **Missing Skills:** Identify skills that are missing from the resume.
- **Resume Section Checklist:** Check important resume sections.
- **Improvement Suggestions:** Provide suggestions to improve the resume.
- **Download Report:** Download the generated analysis as a TXT file.

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Frontend / Web Framework | Streamlit |
| PDF Processing | PyPDF |
| DOCX Processing | python-docx |
| Data Processing | Python |
| Version Control | Git and GitHub |
| Development Environment | Visual Studio Code |

## Project Structure

```text
AI_Resume_Analyzer/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Files excluded from Git
├── sample_resume.txt      # Sample resume for testing
│
└── venv/                  # Local virtual environment (not uploaded)
```

## Prerequisites

Before running the project, make sure you have installed:

- Python 3.9 or newer
- pip (Python package installer)
- Git
- Visual Studio Code (recommended)
- A web browser
- Internet connection for installing dependencies

### Step 1: Clone the Repository

Open your terminal and execute:

```bash
git clone https://github.com/Praneeth3105/AI_Resume_Analyzer.git
```

Navigate into the project folder:

```bash
cd AI_Resume_Analyzer
```

### Step 2: Create a Virtual Environment

Create an isolated Python environment:

```bash
python -m venv venv
```

On Windows, you can also use:

```bash
py -m venv venv
```

### Step 3: Activate the Virtual Environment

**Windows – Command Prompt:**

```bash
venv\Scripts\activate.bat
```

**Windows – PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows – Git Bash:**

```bash
source venv/Scripts/activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

After activation, you should see `(venv)` in your terminal.

### Step 4: Upgrade pip

Run the following command:

```bash
python -m pip install --upgrade pip
```

### Step 5: Install Dependencies

Install all the required Python packages:

```bash
pip install -r requirements.txt
```

### Step 6: Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open automatically in your default browser.

If it does not open automatically, visit:

```text
http://localhost:8501
```

## How to Use the Application

1. Open the AI Resume Analyzer application.
2. Upload your resume in PDF, DOCX, or TXT format.
3. Select your desired job role.
4. Submit the resume for analysis.
5. View the generated skill matching score.
6. Review the matched and missing skills.
7. Check the resume section checklist.
8. Read the improvement suggestions.
9. Download the analysis report as a TXT file.

## Testing

A sample resume file named `sample_resume.txt` is included in the repository.

You can upload this file to test the application.

Suggested target roles:

- Python Developer
- General Software Intern

## Troubleshooting

**1. Python is not recognized**

Install Python and make sure you select the option to add Python to PATH during installation.

**2. Streamlit command not found**

Activate the virtual environment and install the dependencies again:

```bash
pip install -r requirements.txt
```

**3. ModuleNotFoundError**

Install the missing package or reinstall all dependencies:

```bash
pip install -r requirements.txt
```

**4. Application does not open**

Run the following command and open the local URL displayed in the terminal:

```bash
streamlit run app.py
```

**5. Virtual environment activation error in PowerShell**

If PowerShell blocks activation, use Command Prompt or Git Bash activation instructions instead.

## Important Project Note

This project is an educational, rule-based prototype. Its skill matching score is calculated using predefined keywords and job-role skill lists. It does not represent an official recruitment score and does not currently use a live Large Language Model (LLM).

The project can be extended in the future with Natural Language Processing, Prompt Engineering, and LLM API integration for more advanced resume evaluation.

## Future Enhancements

- Integration with Large Language Models (LLMs).
- Advanced Natural Language Processing.
- Job description-based resume matching.
- ATS-friendly resume evaluation.
- Personalized resume improvement recommendations.
- Additional job roles and skill categories.

---
