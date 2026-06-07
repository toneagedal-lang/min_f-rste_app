import streamlit as st
import pandas as pd

st.title("Min første app! 🎉")

data = pd.DataFrame({
    "navn": ["Maria", "Ole", "Kari", "Per"],
    "alder": [25, 28, 32, 45],
    "karakter": ["A", "B", "A", "C"]
})

st.write("Her er dataen vår:")
st.dataframe(data)

st.bar_chart(data.set_index("navn")["alder"])
