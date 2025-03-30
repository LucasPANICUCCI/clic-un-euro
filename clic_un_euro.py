import streamlit as st

st.set_page_config(page_title="Un clic, un euro 💰")

if "compteur" not in st.session_state:
    st.session_state.compteur = 0

st.title("💶 Un clic = 1 euro")
st.write(f"Montant actuel : **{st.session_state.compteur} €**")

if st.button("Ajouter 1 €"):
    st.session_state.compteur += 1
