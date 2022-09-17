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
        
htt="""
<div class="waveWrapper waveAnimation">
  <div class="waveWrapperInner bgTop">
    <div class="wave waveTop" style="background-image: url('http://front-end-noobs.com/jecko/img/wave-top.png')"></div>
  </div>
  <div class="waveWrapperInner bgMiddle">
    <div class="wave waveMiddle" style="background-image: url('http://front-end-noobs.com/jecko/img/wave-mid.png')"></div>
  </div>
  <div class="waveWrapperInner bgBottom">
    <div class="wave waveBottom" style="background-image: url('http://front-end-noobs.com/jecko/img/wave-bot.png')"></div>
  </div>
</div>
"""
st.markdown(htt,unsafe_allow_html=True)

html_temp = """

    <h1 style ="color:#299438;text-align:center;">🍽️AM I fit🍽️?? </h1>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)
col1,col2=st.columns(2)
set_bg_hack_url()

with col1:
    html_temp1="""
    <h4 style="color:7ECC49">What did I eat today?</h4>
    """
    st.markdown(html_temp1,unsafe_allow_html=True)
    h=pd.read_csv("calories.csv")
    f=pd.DataFrame(h)
    t=f["Item"].values.tolist()
    c=f["Calorie per 100gm"].values.tolist()
    s=0
    z=[]
    checked_stocks=[]
    ht="""
    <h4 style="color:#96C3EB">Quantity intake:</h4>
    """
    st.sidebar.markdown(ht,unsafe_allow_html=True)
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
    ht2="""
    <h4 style="color:#7ECC49">Exercises performed:</h4>
    """
    
    st.markdown(ht2,unsafe_allow_html=True)
    e=y["Exercise"].values.tolist()
    m=y["calories per hour"].values.tolist()
    check_boxes1=[st.checkbox(stock,key=stock) for stock in e]
    checked_stocks1=[stock for stock,checked in zip(e,check_boxes1) if checked]
    x=[]
    u=0
    s1=0
    ht3="""
    <h4 style="color:#96C3EB">Workout time:</h4>
    """
    
    
    st.sidebar.markdown(ht3,unsafe_allow_html=True)
    for a in checked_stocks1:
        d=st.sidebar.number_input("enter in minutes",key=e.index(a)+100)
        x.append(d)     
    for a in checked_stocks1:
        if a in e:
            s1=s1+m[e.index(a)]*x[u]
            u=u+1  
    s1=s1/60       
if st.sidebar.button("predict"):
    st.sidebar.markdown("Your Calorie count is{}".format(s-s1))
   # st.success(s-s1)
    

       
      
    
       
