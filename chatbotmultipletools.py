#!/usr/bin/env python
# coding: utf-8

# In[6]:


from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper


# In[7]:


api_wrapper_arxiv = ArxivAPIWrapper(top_k_results=2,doc_content_chars_max=500)
arxiv = ArxivQueryRun(api_wrapper =api_wrapper_arxiv,description="Query Arxiv Papers")
print(arxiv.name)


# In[8]:


#test

arxiv.invoke("Agentic AI")


# In[9]:


api_wrapper_wiki = WikipediaAPIWrapper(top_k_results=2,doc_content_chars_max=500)
wiki = WikipediaQueryRun(api_wrapper =api_wrapper_wiki,description="Query Arxiv Papers")
print(wiki.name)


# In[14]:


#test
wiki.invoke("What is Computer Vision")


# In[15]:


from dotenv import load_dotenv
load_dotenv()

import os

os.environ["TAVILY_API_KEY"]=os.getenv("TAVILY_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")


# In[16]:


### Tavily Search Tool
from langchain_community.tools.tavily_search import TavilySearchResults
tavily = TavilySearchResults()


# In[17]:


tavily.invoke("Provide me the latest YOLO model version")


# In[ ]:


#combining all these tools in the list
tools=[arxiv,wiki,tavily]


# In[24]:


##initialize the LLM model
from langchain_groq import ChatGroq

llm=ChatGroq(model="qwen/qwen3-32b")


# In[25]:


llm.invoke("What is Agentic AI")


# In[28]:


llm_with_tools=llm.bind_tools(tools=tools)


# In[30]:


llm_with_tools.invoke("What is the latest yolo version? ")


# Workflow
# 

# In[36]:


##state Schema
from typing_extensions import TypedDict, List
from langchain_core.messages import AnyMessage # Human Message or AI message
from typing import Annotated #labelling
from langgraph.graph.message import add_messages #reducer in langgraph


# In[42]:


class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]


# In[43]:


## Entire Chatbot With LangGraph
from IPython.display import Image, display
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition


# In[47]:


### Node definition
def tool_calling_llm(state:State):
    return {"messages":[llm_with_tools.invoke(state["messages"])]}


#Build graph
builder = StateGraph(State)
builder.add_node("tool_calling_llm", tool_calling_llm)
builder.add_node("tools", ToolNode(tools))

##Edges
builder.add_edge(START, "tool_calling_llm")
builder.add_conditional_edges(
    "tool_calling_llm",
    # if the latest message (result) from the assistant is a tool call - tools_condition routes to tools
    # if the latest message (result) from the assistant is not a tool call - tools_condition routes to END
    tools_condition,
)
builder.add_edge("tools", END)

graph = builder.compile()

#View
display(Image(graph.get_graph().draw_mermaid_png()))


# In[ ]:


#testing
messages=graph.invoke({"messages":"10.7759/cureus.76320"})
for m in messages['messages']:
    m.pretty_print()


# In[51]:


#testing
messages=graph.invoke({"messages":"Hi, My name is Meera"})
for m in messages['messages']:
    m.pretty_print()


# In[ ]:




