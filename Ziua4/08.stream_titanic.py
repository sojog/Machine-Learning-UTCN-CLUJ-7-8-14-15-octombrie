## pip install streamlit
import streamlit as st
import pickle
from sklearn.pipeline import Pipeline


with open("titanic.pkl", "rb") as file_reader:
    model:Pipeline = pickle.load(file_reader)


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

with st.chat_message("assistant") as chat_msg:
    st.write("Care este genul tau???")


for msg in st.session_state["messages"]:
    with st.chat_message("human") as chat_msg:
        st.write(msg)

    gender = 1 if msg == "male" else 0

    pasager = [3,	gender,	22.0,	1,	0,	7.2500,	8,	2]

    supravietuiste = model.predict([ pasager  ])

    with st.chat_message("ai") as chat_msg:
        st.write(f"Pasagerul supravietuieste: {bool(supravietuiste[0])}" )