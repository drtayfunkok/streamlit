#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd 
import numpy as np
from PIL import Image


# In[ ]:


st.title("This is a title")
st.text("tayfun")
st.markdown("streamlit")
st.header("this is a header")
st.error("abc")
st.info("abncdtt")
st.help(range)
st.write("hello :sunglasses:")

#imgae

img=Image.open("img.png")
st.image(img, caption="abc")


st.video("https://www.youtube.com/watch?v=GRPaV2Aq2GQ")

cbox=st.checkbox("Hide and Seek")
if cbox:
        st.write("Hide")
else:
    st.write("Seek")
    
status=st.radio("slect a clor", ("blue", "orange", "yellow"))

if status=="blue":
    st.write("blue")
elif status=="orange":
    st.write("blue")
else:
    st.write("yellow")
    
st.selectbox("Your Occupation", ["data scientist", "teacher"])

option1=st.slider("select a number", min_value=5, max_value=70,value=30, step=5)


st.date_input("today is")

st.sidebar.title("sidebar")


a=st.sidebar.slider("input")
b=st.sidebar.slider("input2")

st.write(a*b)





   

