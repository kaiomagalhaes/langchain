from langchain.llms import OpenAI
import os


llm = OpenAI(openai_api_key=os.environ.get('OPENAI_API_KEY'), temperature=0.9)

text = "What would be a good company name for a company that makes colorful socks?"
print(llm(text))


