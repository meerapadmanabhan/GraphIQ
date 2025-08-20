import streamlit as st
from chatbotmultipletools import graph

st.title("GraphIQ")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display past messages
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Ask me something..."):
    # Add user message
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Run graph
    result = graph.invoke({"messages": prompt})

    # Walk through messages (Human, Tool Calls, Tool Results, AI)
    for m in result["messages"]:
        if m.type == "human":
            st.chat_message("user").write(m.content)
        elif m.type == "ai":
            if m.tool_calls:
                with st.expander("🔧 Tool Calls"):
                    st.write(m.tool_calls)
            st.chat_message("assistant").write(m.content)
        elif m.type == "tool":
            with st.expander(f"📡 Tool Response: {m.name}"):
                st.write(m.content)

    # Save conversation
    st.session_state["messages"].append({"role": "assistant", "content": result["messages"][-1].content})
