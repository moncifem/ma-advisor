from langchain_openai import ChatOpenAI

def gpt_35_turbo():
    return ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

def gpt_4o():
    return ChatOpenAI(model="gpt-4o", temperature=0)