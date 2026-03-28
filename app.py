import streamlit as st


st.title("Master Calculator")
st.write("This is a simple calculator app built with Streamlit.")

num=st.number_input("Enter a Number",step=1)

sq=num**2
cu=num**3

st.write(f"The square of {num} is {sq}")
st.write(f"The cube of {num} is {cu}")