# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 23:59:56 2022

@author: harsh
"""

import streamlit as st
import pandas as pd
def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         """
         <style>
         .stApp {{
             background-image: url("food.jpg");
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
    h=pd.read_csv("calories.csv")
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
    b=pd.read_csv("exercises.csv")
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
        html_temp3="""
        <h4 style="color:#FF9933">tiktik you are absolutely fit.</h4>
        """
        
        st.sidebar.markdown(html_temp3,unsafe_allow_html=True)

    elif s2>500:
        html_temp5="""
        <h4 style="color:#FF9933">oh no!Seems that you are missing your diet</h4>
        """
        
        st.sidebar.markdown(html_temp5,unsafe_allow_html=True)

       
       
       #st.warning("No worries .. Keep on exercising ")
    elif s2<300:
        html_temp6="""
        <h4 style="color:#FF9933">Inky pinky ponky.
        Seems you are underweight!!</h4>
        """
        
        st.sidebar.markdown(html_temp6,unsafe_allow_html=True)

       
      
    
       
