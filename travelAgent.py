import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub 

llm = ChatOpenAI(model = "gpt-3.5-turbo")

tools = load_tools(['ddg-search', 'wikipedia'], llm=llm)

print(tools[0].name, tools[0].description)

prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, prompt=prompt, verbose=True)

# agent = initialize_agent(
#   tools,
#   llm,
#   agent = 'zero-shot-react-description',
#   verbose = True
# )

# print("_______________")
# print(agent.agent.llm_chain.prompt.template)
# print("_______________")

query = """
Vou viajar para Londres em agosto de 2024.
Quero que faça um roteiro de viagem para mim com os eventos quer irão ocorrer na data da viagem da cidade e com o preço de passagem de São Paulo para Londres.
"""

agent_executor.invoke({"input": query})

# ReAct (reason + react) = construção do prompt de interações de pensamento e ação 