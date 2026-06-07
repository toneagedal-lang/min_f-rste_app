import streamlit as st
import pandas as pd
from datetime import date

st.title("Pasientregistrering 🏥")

# Liste over behandlere
behandlere = [
    "Benedikte", "Marit", "Mona",
    "Line", "Tone", "Bjørn Olav",
    "Vigdis", "Lene", "Jonathan",
    "Espen", "Ingrid J", "Ingdir C",
    "Lena", "Lilly", "Vibeke",
    "Oscar", "Behandler 17", "Behandler 18"
]

# Registreringsskjema
st.subheader("Registrer ny pasient")

dato = st.date_input("Dato for tildeling", date.today())
behandler = st.selectbox("Velg behandler", behandlere)
type_sak = st.radio("Type", ["Utredning", "Behandling"])

if st.button("Registrer pasient"):
    st.success("Pasient registrert! ✅")
    st.write(f"Dato: {dato}")
    st.write(f"Behandler: {behandler}")
    st.write(f"Type: {type_sak}")
