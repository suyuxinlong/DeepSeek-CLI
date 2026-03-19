# DeepSeek Terminal CLI (开源版)

这是一个功能强大的开源命令行工具，让你能直接在终端与 DeepSeek 大模型进行流式对话。它不仅支持基础聊天，还具备**读取本地文件**和**执行系统命令**的智能体 (Agent) 能力。

## 🌟 核心特性

- **一键直达**：在任何路径直接输入 `deepseek` 即可启动。
- **流式输出**：打字机般的实时回复体验，由 `rich` 库提供优雅的 Markdown 渲染。
- **交互式对话**：支持多轮对话、命令历史记录和 `Ctrl+C` 中断。
- **文件读取能力**：你可以要求 DeepSeek “分析这段代码”或“总结这个文档”。
- **系统命令执行**：内置安全确认机制。DeepSeek 可以根据你的需求生成并执行 Shell 命令（如查看目录、运行脚本等）。
- **极简配置**：兼容 OpenAI API 协议，只需一个 API Key 即可启动。

---

## 🚀 快速安装

为了在系统的任何地方都能通过 `deepseek` 命令启动，请按照以下步骤操作：

### 1. 克隆/下载本项目
```bash
git clone https://github.com/your-username/deepseek-cli.git
cd deepseek-cli
```

### 2. 环境配置与全局安装
建议在虚拟环境中安装以保持系统整洁：
```bash
python3 -m venv venv
source venv/bin/activate
pip install -e .
```
*注：`-e` 模式（可编辑模式）意味着你对代码的修改会立即生效，无需重新安装。*

---

## ⚙️ 配置 API Key

1. 在项目根目录创建 `.env` 文件：
   ```bash
   cp .env.example .env
   ```
2. 编辑 `.env` 文件，填入你的 DeepSeek API Key：
   ```env
   DEEPSEEK_API_KEY="sk-xxxxxxxxxxxxxxxxxxxx"
   ```

---

## 📖 使用指南

### 1. 开启交互对话（推荐）
在终端任何地方直接输入：
```bash
deepseek
```

### 2. 快速问答
如果你只想进行单次提问，可以直接跟上问题：
```bash
deepseek "如何使用 Python 实现一个装饰器？"
```

### 3. 查看版本信息
```bash
deepseek version
# 或者使用快捷参数
deepseek -v
```

### 4. 使用智能 Agent 功能
在对话中，你可以直接对 DeepSeek 下达涉及本地文件或系统的指令：
- **文件分析**：`"帮我重构一下 ./main.py 里的逻辑"`
- **系统操作**：`"帮我看看当前目录下占用空间最大的文件夹是哪个"`
- **自动修复**：`"运行一下测试脚本，如果报错了请告诉我怎么修复"`

---

## 📂 项目结构

```text
deepseek-cli/
├── deepseek_cli/       # 核心源代码包
│   ├── __init__.py     # 包初始化与版本定义
│   ├── client.py       # API 客户端、流式渲染与工具调用逻辑
│   ├── tools.py        # 本地工具定义 (文件读取、命令执行)
│   ├── config.py       # 环境变量与全局配置加载
│   └── main.py         # CLI 入口逻辑 (Typer 控制器)
├── .env.example        # 环境变量配置模板
├── setup.py            # Python 包安装脚本 (定义全局命令入口)
└── README.md           # 项目说明文档
```

---

## 🤝 贡献与反馈
我们非常欢迎任何形式的贡献！如果你有更好的想法，欢迎：
1. 提交 Issue 报告 Bug 或提出新功能建议。
2. 提交 Pull Request 改进代码逻辑。
3. 完善文档，让更多人能轻松上手。

## 📄 开源协议
本项目采用 [MIT License](LICENSE) 开源协议。你可以自由地使用、修改和分发本工具。
