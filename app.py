import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from app_home import run_home_app
from app_R import run_R_app
from app_M import run_M_app

def main() : 
    

    st.title('메시와 호날두 통계와 그 둘을 분석하는 앱')
    

 

    menu = ['Home','Messi EDA','Ronaldo EDA' , 'Compare M with R']

    choice = st.sidebar.selectbox('메뉴', menu )

    if choice == 'Home' :
        run_home_app()
    
    elif choice == 'Messi EDA' :
        run_M_app()
    
    elif choice == 'Ronaldo EDA' :
        run_R_app()
    
    elif choice =='Compare M with R' :
        pass
     
   



if __name__ =='__main__' :
    main()



