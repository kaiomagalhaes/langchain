import os

from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI


prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

prompt_text = prompt.format(product="colorful socks")

print(prompt_text)

llm = OpenAI(openai_api_key=os.environ.get('OPENAI_API_KEY'), temperature=0.9)

print(llm(prompt_text))
