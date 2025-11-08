# 🚀 Agentic AI Coding Assistant
> **Autonomous code reasoning, debugging, and file manipulation powered by Gemini Flash**

This project is a hands-on implementation of an **agentic AI coding assistant** built in Python that can **read, update, run, and debug codebases autonomously** using **Gemini Flash API** with structured tool calling.

Inspired by **freeCodeCamp.org's tutorial by Lane Wagner**, this agent demonstrates how modern LLMs can drive **multi-step coding workflows**, mimicking real autonomous dev agents.

---

## ✨ Features

- 🧠 **Agentic Reasoning Loop** — Plan → Act → Observe → Improve until the task is complete
- 🛠 **Tool Calling System** with built-in tools:
  - 📁 Scan project directory
  - 📄 Read files
  - ✍️ Write / update files
  - ▶️ Run Python scripts & capture errors
- 🐞 **Autonomous Debugging** — Fixes bugs, updates code, reruns to validate
- 🔐 **Sandboxed Execution** — Prevents access outside project directory
- 🤖 **Real-world coding assistance simulation** like AI software engineers

---

## 🎬 Demo

![Agentic Loop Demo](demo.gif)  
*The agent scans, edits, fixes, and verifies code autonomously in a loop.*

---

## 🧠 How It Works

1. You give a natural language command like:
   > *"Fix the bug in calculator.py"*
2. The agent:
   - Scans files
   - Reads source code
   - Detects bugs or logical issues
   - Writes fixes back to the codebase
   - Runs the program to verify results
3. The loop continues until the task succeeds ✅

This showcases **multi-step reasoning** and **autonomous software automation** using Gemini API tool calling.

---

## 🗂 Project Structure

```
.
├── agent.py            # Main agent loop + Gemini integration
├── tools/              # Custom tool implementations
│   ├── scan.py         # Directory scanner
│   ├── read.py         # File reader
│   ├── write.py        # File writer
│   ├── run.py          # Python execution engine
├── demo_app/           # Sample buggy project (e.g., calculator)
├── requirements.txt    # Python dependencies
└── main.py             # CLI entrypoint
```

---

## ⚙️ Setup & Installation

### ✅ Prerequisites

- **Python 3.8+**
- **Gemini API key (Flash model access recommended)**
- **UV package manager**

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2. Install dependencies using UV
```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### 3. Set your Gemini API Key
```bash
export GEMINI_API_KEY="your_api_key_here"
```

### 4. Run the agent
```bash
python main.py "Fix the bug in calculator.py"
```

---

## 🧪 Example Usage

```bash
python main.py "What is inside tests.py?"
python main.py "Fix errors and make the script run without crashing"
```

The agent will:
✔ Explore project files  
✔ Modify code if needed  
✔ Execute it  
✔ Iterate until success  

---

## 🔒 Safety Notes

- The agent **can only access files in the project directory**
- Code execution is restricted to **Python files inside the workspace**
- No system-level commands are run

---

## 🛠 Built With

| Tech | Purpose |
|------|--------|
| Python | Core language |
| Gemini Flash API | LLM reasoning & tool calling |
| UV | Dependency & environment management |

---

## 🤝 Contributions

Pull requests are welcome! Feel free to:
- Add new tools (linting, test generation, etc.)
- Improve reasoning prompts
- Expand sandboxing and logging

---

## 📜 License

MIT License — Feel free to use, learn from, and build on it.

---

### 🚀 Future Improvements

- Add vector-based code search
- Support multiple languages (JS, TS, Go, etc.)
- Add unit test generation tool
- Introduce planning visualization UI
