import typer
from typing import Optional
from rich.console import Console
from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory

from .client import DeepSeekClient
from . import __version__

# 设置 invoke_without_command=True 允许直接运行主命令
app = typer.Typer(help="DeepSeek Terminal CLI", invoke_without_command=True)
console = Console()

def start_interactive_chat(client: DeepSeekClient):
    """启动交互式对话模式 (REPL)"""
    console.print(f"[bold green]欢迎使用 DeepSeek CLI (v{__version__})![/bold green]")
    console.print("输入你的问题开始对话。支持流式输出、读取文件和执行终端指令。")
    console.print("输入 [bold yellow]exit[/bold yellow] 或 [bold yellow]quit[/bold yellow] 退出，按 [bold yellow]Ctrl+C[/bold yellow] 中断当前生成。")
    console.print("-" * 50)

    session = PromptSession(history=InMemoryHistory())

    while True:
        try:
            user_input = session.prompt("\nYou: ")
            user_input = user_input.strip()

            if not user_input:
                continue
            
            if user_input.lower() in ['exit', 'quit']:
                console.print("再见！")
                break
            
            client.add_user_message(user_input)
            client.stream_chat()
            
        except KeyboardInterrupt:
            console.print("\n[bold yellow]已取消[/bold yellow]")
            continue
        except EOFError:
            console.print("\n再见！")
            break

@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    message: Optional[str] = typer.Argument(None, help="可选：单次向 DeepSeek 提问的内容"),
    version_flag: bool = typer.Option(False, "--version", "-v", help="查看版本信息")
):
    """
    DeepSeek 终端助手。直接输入 'deepseek' 进入对话，或输入 'deepseek \"问题\"' 快速问答。
    """
    # 如果用户只想看版本
    if version_flag:
        console.print(f"DeepSeek CLI v{__version__}")
        raise typer.Exit()

    # 如果运行了子命令（如 deepseek version），则不执行默认逻辑
    if ctx.invoked_subcommand is not None:
        return

    client = DeepSeekClient()

    if message:
        # 情况 1: 用户输入了 'deepseek "问题"'
        client.add_user_message(message)
        client.stream_chat()
        console.print()
    else:
        # 情况 2: 用户仅输入了 'deepseek'
        start_interactive_chat(client)

@app.command("version")
def show_version():
    """打印版本信息"""
    console.print(f"DeepSeek CLI v{__version__}")

def run():
    app()

if __name__ == "__main__":
    run()
