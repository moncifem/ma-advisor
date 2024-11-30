from agents.base_agent import graph, query_basic_agent
from dotenv import load_dotenv
load_dotenv()

print(graph.get_graph())

question = "how much is the volume of the world"

print(query_basic_agent(query=question))
# while True:
#     question = input("type a question: ")
    