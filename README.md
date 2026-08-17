# Nagendra 🤖 AI Research Assistant

> An Agentic AI application built from scratch using Python that intelligently decides how to answer user questions by selecting the appropriate tool.

---

## 📖 Project Overview

AI Research Assistant is a modular Python application that demonstrates the fundamentals of Agentic AI without relying on frameworks like LangChain or LangGraph.

Instead of sending every question directly to a Large Language Model, the application first uses an AI Planner to determine the best action.

Depending on the user's request, it can:

- Answer general knowledge questions
- Search the web for current information
- Perform mathematical calculations
- Read and summarize PDF documents
- Answer questions based on PDF content

The project was built to understand how AI Agents work internally before moving to advanced frameworks.

---

# ✨ Features

- 🧠 AI Planner
- 🌐 Web Search (Tavily API)
- ➗ Calculator Tool
- 📄 PDF Reader
- 📚 PDF Question Answering
- 🔀 Automatic Tool Routing
- 🛡 Error Handling
- 🏗 Modular Architecture
- 🚀 Easy to Extend

---

# 🏗 Architecture

```
                    User

                      │

                      ▼

              AI Planner (LLM)

                      │

      ┌───────────────┼───────────────┐

      ▼               ▼               ▼

  Web Search      Calculator      PDF Reader

      │               │               │

      └───────────────┼───────────────┘

                      ▼

             AI Response Generator

                      │

                      ▼

                    User
```

---

# 📁 Project Structure

```text
ai-research-assistant/

│
├── main.py
├── requirements.txt
├── .env
│
└── app/
    ├── agent.py
    ├── calculator.py
    ├── config.py
    ├── llm.py
    ├── pdf_reader.py
    ├── prompts.py
    ├── search.py
    └── tools.py
```

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| OpenRouter API | LLM Access |
| Tavily API | Web Search |
| PyPDF | PDF Reading |
| Requests | API Communication |
| python-dotenv | Environment Variables |

---

# ⚙ Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd ai-research-assistant
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```
OPENROUTER_API_KEY=your_openrouter_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

# ▶️ Run the Application

```bash
python main.py
```

---

# 💬 Example Questions

General Knowledge

```
What is Python?
```

Calculator

```
125 * 378
```

Search

```
Latest AI news

Today's gold price

Weather in Hyderabad
```

PDF

```
Summarize sample.pdf

What is the conclusion of sample.pdf?
```

---

# ✅ Current Capabilities

- AI Planning
- Web Search
- Calculator
- PDF Reading
- PDF Summarization
- PDF Question Answering
- Error Handling
- Modular Design

---

# 🚀 Future Improvements

- Conversation Memory
- RAG Integration
- LangChain
- LangGraph
- OCR for Scanned PDFs
- Search Query Optimization
- Multiple Tool Execution
- Web Interface (Streamlit)
- Chat History

---

# 📚 What I Learned

This project helped me understand:

- Agentic AI
- Prompt Engineering
- Tool Routing
- Modular Python Development
- API Integration
- Error Handling
- AI Planning
- Software Engineering Principles

---

# 👨‍💻 Author

**Nagendra P**

Built as a learning project to understand Agentic AI by implementing an AI Research Assistant from scratch using Python.

---