[中文文档](README_zh.md) | [English](README.md)

# DeepSeek Terminal CLI (Open Source Edition)

A powerful open-source command-line tool that allows you to chat with the DeepSeek large model directly in your terminal using streaming output. It supports not only basic chat but also features Agent capabilities for **reading local files** and **executing system commands**.

🔗 **Repository:** [https://github.com/suyuxinlong/DeepSeek-CLI](https://github.com/suyuxinlong/DeepSeek-CLI)

## 🌟 Core Features

- **Quick Access**: Type `deepseek` in any path to start.
- **Streaming Output**: Typewriter-like real-time response experience, elegantly rendered in Markdown by the `rich` library.
- **Interactive Chat**: Supports multi-turn conversations, command history, and `Ctrl+C` interruption.
- **File Reading Capability**: You can ask DeepSeek to "analyze this code" or "summarize this document".
- **System Command Execution**: Built-in safety confirmation mechanism. DeepSeek can generate and execute Shell commands based on your needs (e.g., viewing directories, running scripts).
- **Minimalist Configuration**: Compatible with the OpenAI API protocol; only an API Key is required to start.

---

## 🚀 Quick Installation

To launch via the `deepseek` command from anywhere on your system, please follow these steps:

### 1. Clone/Download this project
```bash
git clone https://github.com/suyuxinlong/DeepSeek-CLI.git
cd DeepSeek-CLI
```

### 2. Environment Setup & Global Installation
It is recommended to install in a virtual environment to keep your system clean:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -e .
```
*Note: The `-e` (editable) mode means your code modifications will take effect immediately without needing reinstallation.*

---

## ⚙️ Configuration (API Key)

1. Create a `.env` file in the project root directory:
   ```bash
   cp .env.example .env
   ```
2. Edit the `.env` file and fill in your DeepSeek API Key:
   ```env
   DEEPSEEK_API_KEY="sk-xxxxxxxxxxxxxxxxxxxx"
   ```

---

## 📖 Usage Guide

### 1. Start Interactive Chat (Recommended)
Type directly anywhere in the terminal:
```bash
deepseek
```

### 2. Quick Q&A
If you only want to ask a single question, you can append it directly:
```bash
deepseek "How to implement a decorator in Python?"
```

### 3. Check Version Information
```bash
deepseek version
# Or use the shortcut parameter
deepseek -v
```

### 4. Use Smart Agent Features
During a conversation, you can give DeepSeek instructions involving local files or the system:
- **File Analysis**: `"Help me refactor the logic in ./main.py"`
- **System Operations**: `"Help me check which folder takes up the most space in the current directory"`
- **Auto-Fix**: `"Run the test script, and if it errors out, tell me how to fix it"`

---

## 📂 Project Structure

```text
DeepSeek-CLI/
├── deepseek_cli/       # Core source code package
│   ├── __init__.py     # Package initialization and version definition
│   ├── client.py       # API client, streaming rendering, and tool invocation logic
│   ├── tools.py        # Local tool definitions (file reading, command execution)
│   ├── config.py       # Environment variable and global configuration loading
│   └── main.py         # CLI entry logic (Typer controller)
├── .env.example        # Environment variable configuration template
├── setup.py            # Python package installation script (defines global command entry)
└── README.md           # Project documentation
```

---

## 🤝 Contribution & Feedback
We welcome contributions in any form! If you have better ideas, feel free to:
1. Submit an Issue to report a bug or suggest new features.
2. Submit a Pull Request to improve code logic.
3. Improve documentation to make it easier for others to get started.

## 📄 License
This project is open-sourced under the [MIT License](LICENSE). You are free to use, modify, and distribute this tool.
