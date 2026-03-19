import json
from typing import List, Dict, Any
from openai import OpenAI
from rich.console import Console
from rich.live import Live
from rich.markdown import Markdown

from .config import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL
from .tools import TOOLS_SCHEMA, AVAILABLE_TOOLS

console = Console()

class DeepSeekClient:
    def __init__(self):
        if not DEEPSEEK_API_KEY:
            console.print("[bold red]错误: 未找到 DEEPSEEK_API_KEY 环境变量。[/bold red]")
            console.print("请在运行前设置环境变量，或在当前目录创建一个 .env 文件并添加 `DEEPSEEK_API_KEY=your_key`。")
            exit(1)
            
        self.client = OpenAI(
            api_key=DEEPSEEK_API_KEY,
            base_url=DEEPSEEK_BASE_URL
        )
        self.messages: List[Dict[str, Any]] = [
            {"role": "system", "content": "你是一个有用的 AI 助手，可以回答问题、阅读代码、并通过工具执行终端命令。回答请尽量精简并使用中文。"}
        ]
        
    def add_user_message(self, content: str):
        self.messages.append({"role": "user", "content": content})

    def stream_chat(self) -> str:
        """与模型对话，处理流式输出并自动处理工具调用"""
        
        while True:
            try:
                # 调用模型
                response = self.client.chat.completions.create(
                    model="deepseek-chat",
                    messages=self.messages,
                    tools=TOOLS_SCHEMA,
                    stream=True
                )
            except Exception as e:
                console.print(f"[bold red]API 请求失败: {e}[/bold red]")
                return ""

            # 接收并渲染模型的响应
            full_content = ""
            tool_calls = {}

            console.print("\n[bold cyan]DeepSeek:[/bold cyan]")
            
            with Live(Markdown(""), refresh_per_second=10, console=console) as live:
                for chunk in response:
                    delta = chunk.choices[0].delta
                    
                    # 文本内容
                    if delta.content:
                        full_content += delta.content
                        live.update(Markdown(full_content))
                    
                    # 工具调用
                    if delta.tool_calls:
                        for tool_call in delta.tool_calls:
                            index = tool_call.index
                            if index not in tool_calls:
                                tool_calls[index] = {
                                    "id": tool_call.id,
                                    "type": "function",
                                    "function": {
                                        "name": tool_call.function.name or "",
                                        "arguments": tool_call.function.arguments or ""
                                    }
                                }
                            else:
                                if tool_call.function.name:
                                    tool_calls[index]["function"]["name"] += tool_call.function.name
                                if tool_call.function.arguments:
                                    tool_calls[index]["function"]["arguments"] += tool_call.function.arguments

            # 如果没有工具调用，对话结束
            if not tool_calls:
                self.messages.append({"role": "assistant", "content": full_content})
                return full_content

            # 处理工具调用
            # 先将 assistant 的 tool_calls 加入消息历史
            message_tool_calls = list(tool_calls.values())
            self.messages.append({
                "role": "assistant",
                "content": full_content,
                "tool_calls": message_tool_calls
            })

            console.print()

            for tool_call in message_tool_calls:
                func_name = tool_call["function"]["name"]
                func_args_str = tool_call["function"]["arguments"]
                
                try:
                    args = json.loads(func_args_str)
                except json.JSONDecodeError:
                    console.print(f"[bold red]解析工具参数失败: {func_args_str}[/bold red]")
                    args = {}

                console.print(f"[bold yellow]=> 调用工具:[/bold yellow] {func_name} (参数: {func_args_str})")
                
                # 执行对应的本地函数
                if func_name in AVAILABLE_TOOLS:
                    result = AVAILABLE_TOOLS[func_name](**args)
                else:
                    result = f"Error: 工具 {func_name} 不存在。"
                    
                # 将结果添加回 messages 并进行下一轮推理
                self.messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call["id"],
                    "content": str(result)
                })
            
            # 回到 while True 的开头，携带 tool messages 重新调用模型
