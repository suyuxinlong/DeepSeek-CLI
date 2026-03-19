import os
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

# 获取 DEEPSEEK_API_KEY
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

if not DEEPSEEK_API_KEY:
    DEEPSEEK_API_KEY = "" # 避免导入时立刻报错，可以在命令执行时再检查

DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"
