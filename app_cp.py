import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def run_cp_app() :
    
    global df
    st.subheader('메시와 호날두의 시즌별 골기록')
    df = pd.read_csv('MessiRonaldo.csv')
    df['Total Goals'] = df['Liga_Goals'] + df['CL_Goals']
    R = df.iloc[[1,3,5,7,9,11,13,15,17], :]
    M = df.iloc[[0,2,4,6,8,10,12,14,16], :]
    x = M['Season']
    y = R['Season']
    x2 = M['Total Goals']
    y2 = R['Total Goals']

    
       



    fig1 = plt.figure()

    plt.plot(x, x2)
    plt.plot(y, y2)
    plt.title('Messi and Ronaldo seasonal goal record ')
    plt.legend(["Messi","Ronaldo"])
    plt.xlabel('Season')
    plt.ylabel('Total Goals')
    plt.xticks(rotation=45)

    st.pyplot(fig1)

   

    


