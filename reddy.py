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
         .stApp {
             background: url("https://thumbs.dreamstime.com/b/healthy-clean-eating-layout-vegetarian-food-diet-nutrition-concept-various-fresh-vegetables-ingredients-salad-white-105567339.jpg");
             background-size: cover
         }
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
    fer="""
    <h3 style="color:red">what is your gender?</h3>
    """
    w=st.markdown(fer,unsafe_allow_html=True)
    k=st.radio("",("male","female"))
    ht22="""
    <h4 style="color:#7ECC49">What did I eat today?</h4>
    """
    st.markdown(ht22,unsafe_allow_html=True)
    h=pd.read_csv("calories.csv")
    f=pd.DataFrame(h)
    t=f["Item"].values.tolist()
    c=f["Calorie per 100gm"].values.tolist()
    s=0
    z=[]
    checked_stocks=[]
    ht="""
    <h4>Quantity intake:</h4>
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
    fer1="""
    <h3 style="color:red">what is your age?</h3>
    """
    w1=st.markdown(fer1,unsafe_allow_html=True)
    age=st.number_input("")
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
    <h4>Workout time:</h4>
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
    st.sidebar.markdown("Your Calorie count is {}".format(s-s1))
    cal=s-s1
   
    if k=="male":
       if age<=13:
           
           if cal<1600:
                st.sidebar.success("You are fit")
           elif cal>1600 and cal<2200:
                st.sidebar.success("Focus on your diet")
           else:
                st.sidebar.success("You have a chance of becoming obese")
       elif age>13 and age<=30:
           if cal<2800:
                st.sidebar.success("You are fit")
           elif cal>2800 and cal<3200:
                st.sidebar.success("Focus on your diet")
           else:
              st.sidebar.success("You have a chance of becoming obese")
       elif age>31 and age<=50:
            if cal<2600:
                st.sidebar.success("You are fit")
            elif cal>2600 and cal<3000:
                st.sidebar.success("Focus on your diet")
            else:
                st.sidebar.success("You have a chance of becoming obese")
       else:
            if cal<2400:
                st.sidebar.success("You are fit")
            elif cal>2400 and cal<2800:
                st.sidebar.success("Focus on your diet")
            else:
                st.sidebar.success("You have a chance of becoming obese")
    elif k=="female":
        if age<=13:
            
           if cal<1600:
              st.sidebar.success("You are fit")
           elif cal>1600 and cal<2200:
              st.sidebar.success("Focus on your diet")
           else:
              st.sidebar.success("You have a chance of becoming obese")
        elif age>13 and age<=30:
           if cal<2400:
                st.sidebar.success("You are fit")
           elif cal>2400 and cal<4000:
                st.sidebar.success("Focus on your diet")
           else:
              st.sidebar.success("You have a chance of becoming obese")
        elif age>31 and age<=50:
           if cal<2200:
             st.sidebar.success("You are fit")
           elif cal>2200 and cal<2800:
              st.sidebar.success("Focus on your diet")
           else:
               st.sidebar.success("You have a chance of becoming obese")
        else:
           if cal<2000:
             st.sidebar.success("You are not much active in diet it seems")
           elif cal>2000 and cal<2200:
              st.sidebar.success("Focus on your diet")
           else:
              st.sidebar.success("You have a chance of becoming obese")
