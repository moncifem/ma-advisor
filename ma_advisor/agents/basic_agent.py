from typing import TypedDict, Annotated
from langgraph.graph import add_messages, StateGraph, START, END
from langchain_core.messages import AnyMessage, HumanMessage
from ma_advisor.utils.model import gpt_35_turbo
from dotenv import load_dotenv

load_dotenv()

llm = gpt_35_turbo()

class MessageState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]

builder = StateGraph(MessageState)

def assistant(state: MessageState):
    return {"messages": llm.invoke(state["messages"])}

builder.add_node("assistant", assistant)

builder.add_edge(START, "assistant")
builder.add_edge("assistant", END)

graph = builder.compile()

def query_basic_agent(query: str):
    """Query the basic agent
    
    Args:
        str: Takes a string as input, transforms it into a human message and invokes the graph
    """
    return graph.invoke({"messages": [HumanMessage(content=query)]})

# try:
#     with open("basic_agent.png","wb") as pic:
#         pic.write(graph.get_graph().draw_mermaid_png())
# except:
#     pass

