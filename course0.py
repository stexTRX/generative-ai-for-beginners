from dotenv import load_dotenv
import os

load_dotenv("D:\\courses_detailed\\generative_ai_for_beginners\\generative-ai-for-beginners\\.env")
github_token = os.getenv("GITHUB_TOKEN")
print(github_token)