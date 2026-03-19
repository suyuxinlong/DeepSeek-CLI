import os
import subprocess
from rich.console import Console

console = Console()

def read_file(filepath: str) -> str:
    """读取并返回指定文件内容。"""
    if not os.path.exists(filepath):
        return f"Error: 文件 {filepath} 不存在。"
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        return f"File content of '{filepath}':\n\n{content}"
    except Exception as e:
        return f"Error: 无法读取文件 {filepath}。详细信息: {e}"

def execute_command(command: str) -> str:
    """执行本地系统命令，必须先经过用户确认。"""
    # 让用户确认是否执行命令
    console.print(f"\n[bold red]⚠️ 警告: DeepSeek 请求执行系统命令: [/bold red][bold cyan]{command}[/bold cyan]")
    try:
        confirm = input("允许执行此命令吗？[y/N]: ").strip().lower()
        if confirm != 'y':
            return "执行被用户取消。"
    except KeyboardInterrupt:
        return "执行被用户取消。"

    try:
        console.print(f"[dim]正在执行命令: {command}...[/dim]")
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        output = result.stdout
        if result.stderr:
            output += f"\nSTDERR:\n{result.stderr}"
        if not output.strip():
            output = "命令已成功执行，但没有输出。"
        return output
    except Exception as e:
        return f"Error: 命令执行失败。详细信息: {e}"

# 用于 Function Calling 的 schema
TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "读取并返回本地指定文件内容。如果需要分析文件、查看代码，可以使用此工具。",
            "parameters": {
                "type": "object",
                "properties": {
                    "filepath": {
                        "type": "string",
                        "description": "本地文件的相对或绝对路径，例如 './main.py' 或 '/etc/hosts'"
                    }
                },
                "required": ["filepath"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "execute_command",
            "description": "在本地系统中执行 Shell 命令并返回执行结果。仅在需要查询系统状态、运行脚本或列出文件时使用。",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "要执行的 bash/shell 命令，例如 'ls -la' 或 'python --version'"
                    }
                },
                "required": ["command"]
            }
        }
    }
]

# 将函数名映射到实际的 Python 函数
AVAILABLE_TOOLS = {
    "read_file": read_file,
    "execute_command": execute_command
}
