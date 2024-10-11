import streamlit as st
import slim

x = st.slider("Number of candidates",2)
y = st.slider("Number of positions",1)

print(x,y)

st.write("minumum cost is:",slim.run(x,y) )
