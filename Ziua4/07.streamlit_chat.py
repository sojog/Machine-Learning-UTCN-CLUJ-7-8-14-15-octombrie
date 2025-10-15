## pip install streamlit
import streamlit as st


st.title("Aici va fi un site de predictie asupra supravietuitorilor din Titanic")
mesaj = st.chat_input("Insereaza o valoare")

print(mesaj)


print("session_state:", st.session_state)

if not st.session_state.get("messages"):
    st.session_state["messages"] = [ ]

if mesaj:
    print("Utilizatorul a scris:", mesaj)
    st.session_state["messages"].append(mesaj)

print("session_state:", st.session_state)


for msg in st.session_state["messages"]:
    with st.chat_message("human") as chat_msg:
        st.write(msg)

    with st.chat_message("ai") as chat_msg:
        st.write("Da, ai drepta ca cu privire la.." + msg)