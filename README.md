# 🎬 CheckzCine

Transform unstructured movie descriptions into structured, AI-generated movie intelligence.

CheckzCine is an AI-powered movie information extraction application built using **LangChain**, **Mistral AI**, **Pydantic**, and **Streamlit**. The application analyzes movie descriptions and automatically extracts key metadata such as title, director, genres, cast, ratings, awards, and plot summaries in a structured format.

---

## 🌐 Live Demo

🚀 **Streamlit App:** *https://checkzcine-tqdvx7sbagpxtbg73ivmx5.streamlit.app/<img width="1888" height="867" alt="home png" src="https://github.com/user-attachments/assets/31ccd764-34d7-471f-b680-f7af127e228a" />
*

---

## 📸 Application Preview

### Home Screen

![Home Screen](<img width="1888" height="867" alt="home png" src="https://github.com/user-attachments/assets/e1eea85a-9a4b-4585-8766-824cfb9c84ef" />home.png)

### Movie Information Extraction

![Output Screen](<img width="1897" height="886" alt="output png" src="https://github.com/user-attachments/assets/6b47b5f9-fce3-4238-bd6b-6badeb731bfd" />output.png)

---

## ✨ Features

* 🎬 Extract movie title and release year
* 🎭 Identify genres and cast members
* 🎥 Extract director information
* ⭐ Capture movie ratings
* 🏆 Detect awards and nominations
* 📝 Generate concise plot summaries
* 🔍 Convert unstructured text into structured data
* ✅ Schema validation using Pydantic
* 🤖 Powered by Mistral Small 2603
* 🎨 Professional Streamlit interface

---

## 🛠️ Tech Stack

### AI & NLP

* LangChain
* Mistral Small 2603
* Prompt Engineering
* Structured Output Parsing

### Backend

* Python
* Pydantic
* python-dotenv

### Frontend

* Streamlit

---

## 🏗️ Architecture

```text
Movie Description
        │
        ▼
ChatPromptTemplate
        │
        ▼
Mistral Small 2603
        │
        ▼
Pydantic Output Parser
        │
        ▼
Structured Movie Schema
        │
        ▼
Streamlit Interface
```

---

## ⚙️ How It Works

### Step 1: User Input

The user provides a movie description paragraph.

### Step 2: Prompt Engineering

LangChain formats the input using a carefully designed ChatPromptTemplate.

### Step 3: LLM Processing

Mistral Small 2603 analyzes the description and extracts movie-related information.

### Step 4: Output Validation

PydanticOutputParser validates the generated response against a predefined schema.

### Step 5: Presentation

The extracted information is displayed through an interactive Streamlit interface.

---

## 📋 Extracted Information

The application extracts:

| Field        | Description            |
| ------------ | ---------------------- |
| Title        | Movie name             |
| Release Year | Year of release        |
| Genre        | One or multiple genres |
| Director     | Movie director         |
| Cast         | Main cast members      |
| Rating       | Movie rating           |
| Awards       | Awards and nominations |
| Plot Summary | Concise movie summary  |

---

## 📂 Project Structure

```text
CheckzCine/
│
├── core.py
├── UIcore.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/AyushChaki/CheckzCine.git
cd CheckzCine
```

Create a virtual environment:

```bash
uv venv
```

Activate the environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
uv pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_api_key_here
```

---

## ▶️ Run Locally

```bash
streamlit run UIcore.py
```

---

## 📈 Future Improvements

* IMDb API Integration
* Rotten Tomatoes Integration
* Movie Poster Retrieval
* Multi-language Support
* Export Results as JSON
* Batch Movie Analysis
* Movie Recommendation Engine
* Vector Database Integration

---

## 💡 Learning Outcomes

This project demonstrates practical implementation of:

* Large Language Models (LLMs)
* Prompt Engineering
* Structured Information Extraction
* Pydantic Schema Validation
* LangChain Expression Language (LCEL)
* Streamlit Application Development
* AI-Powered Data Processing

---

## 👨‍💻 Author

### Ayush Chaki

🔗 GitHub: https://github.com/AyushChaki

🔗 LinkedIn: https://www.linkedin.com/in/ayush-chaki-a49165310/

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
