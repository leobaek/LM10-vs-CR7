import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.set_page_config(layout="wide")
def run_M_app() : 
    
    df = pd.read_csv('MessiRonaldo.csv')
    M = df.iloc[[0,2,4,6,8,10,12,14,16], :]

    st.subheader('Leonel Messi')
    img4 = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fcafefiles.naver.net%2FMjAyMDAxMTBfMTU3%2FMDAxNTc4NTk2NDM0NTcw.Fw1QQdEHMm1w9kj5qEZ_JgSxaibc8yyBcd4Z4_p-YJUg.y-QH0ZXlI7V428B9eKP3YULP_6RD0XhtX6W1YFJt4k4g.GIF%2FexternalFile.gif&type=sc960_832_gif'
    st.image(img4)
    st.subheader('모든 통계는 2009시즌부터 2018시즌까지입니다.')
    st.subheader('Leonel Messi 시즌 별 통계')
    st.dataframe(M)
    M['Total Goals'] = M['Liga_Goals'] + M['CL_Goals']
    M_max = M.loc[(M['Liga_Goals'] + M['CL_Goals'] == 64), ['Season','Liga_Goals','CL_Goals','Total Goals'] ]
    
    
   


    ## 셀렉트박스
    lang = ['Liga 통산 골' , 'Liga 통산 어시스트' , 'CL 통산 골', 'CL 통산 어시스트' ,'한 해 최다 골']
    data = 329 , 138 , 83, 28, 64
    selected_lang = st.selectbox('확인 할 데이터를 선택하세요', lang)
    lg = 'Messi는 Liga에서 통산 329골을 넣었습니다.'
    if selected_lang == lang[0]:
        st.write('Messi는 Liga에서 통산 329골을 넣었습니다.')
    
    elif selected_lang == lang[1]:
        st.write('Messi는 Liga에서 통산 138어시스트를 기록했습니다.')

    elif selected_lang == lang[2]:
        st.write('Messi는 CL에서 통산 83골을 넣었습니다.')

    elif selected_lang == lang[3]:
        st.write('Messi는 CL에서 통산 28어시스트를 기록했습니다.')

    elif selected_lang == lang[4]:
        st.write('Messi의 한 해 최다 골은 64골입니다.')


   ## 히스토그램
    hist_column = M['Season']
    fig1 = plt.figure()
    plt.hist(data= M , x = hist_column )
    
    st.pyplot(fig1)


    


