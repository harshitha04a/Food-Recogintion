# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 23:59:56 2022

@author: harsh
"""

import streamlit as st
import pandas as pd
from emoji import emojize
def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://thumbs.dreamstime.com/b/healthy-clean-eating-layout-vegetarian-food-diet-nutrition-concept-various-fresh-vegetables-ingredients-salad-white-105567339.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

html_temp = """

    <h1 style ="color:#1c4e05;text-align:center;">AM I fit?? </h1>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)
col1,col2=st.columns(2)
set_bg_hack_url()

with col1:
    html_temp1="""
    <h4 style="color:#E05194">What did I eat today?</h4>
    """
    st.markdown(html_temp1,unsafe_allow_html=True)
    h=pd.read_csv("C://Users//harsh//Downloads//calories.csv")
    f=pd.DataFrame(h)
    t=f["Item"].values.tolist()
    c=f["Calorie per 100gm"].values.tolist()
    s=0
    z=[]
    checked_stocks=[]
    st.sidebar.title("Quantity intake:")
    check_boxes=[st.checkbox(stock,key=stock) for stock in t]
    for stock,checked in zip(t,check_boxes):
        if checked:
            checked_stocks.append(stock) 
            l=st.sidebar.number_input("enter gram",key=t.index(stock))
            z.append(l)
    j=0
    for i in checked_stocks:  
        if i in t:
            s=s+c[t.index(i)]*z[j]
            j=j+1
    s=s/100
with col2:
    b=pd.read_csv("C:/Users/harsh/Downloads/exercises.csv")
    y=pd.DataFrame(b)
    html_temp2="""
    <h4 style="color:#FF9933">Exercises performed:</h4>
    """
    
    st.markdown(html_temp2,unsafe_allow_html=True)
    e=y["Exercise"].values.tolist()
    m=y["calories per hour"].values.tolist()
    check_boxes1=[st.checkbox(stock,key=stock) for stock in e]
    checked_stocks1=[stock for stock,checked in zip(e,check_boxes1) if checked]
    x=[]
    u=0
    s1=0
    st.sidebar.title("Workout time")
    for a in checked_stocks1:
        d=st.sidebar.number_input("enter in minutes",key=e.index(a)+100)
        x.append(d)     
    for a in checked_stocks1:
        if a in e:
            s1=s1+m[e.index(a)]*x[u]
            u=u+1  
    s1=s1/60       
if st.sidebar.button("predict"):
    s2=s-s1
   # st.success(s-s1)
    if s2>300 and s2<=500 :
        xy="""
        alert("tiktik you're absolutely fit");
       """
        st.markdown(xy,unsafe_allow_html=True)
        st.markdown('Streamlit is **_really_ cool**.')
    elif s2>500:
        xy="""
        alert("oh no!Seems that you're missing your diet");
       """
        st.markdown(xy)
        st.markdown('Streamlit is **_really_ cool**.')
       #st.warning("No worries .. Keep on exercising ")
    elif s2<300:
        xy="""
        alert("Inky pinky ponky..");
       """
        st.markdown(xy,unsafe_allow_html=True)
        st.markdown('Streamlit is **_really_ cool**.')
       
