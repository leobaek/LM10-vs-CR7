import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
st.set_page_config(layout="wide")
def run_M_app() : 
    
    df = pd.read_csv('MessiRonaldo.csv')
    M = df.iloc[[0,2,4,6,8,10,12,14,16], :]
    M['Total Goal'] = M['Liga_Goals'] + M['CL_Goals']

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
    st.subheader('히스토그램')
    
    column_list = M.columns[2: ]
    histogram_column = st.selectbox('히스토그램 확인할 컬럼을 선택하세요', column_list)
    my_bins = st.number_input('빈의 갯수를 입력하세요', 5, 30, value=10,step=1)
    
    fig1 = plt.figure()
    plt.hist(data=M , x= histogram_column , bins= my_bins ,rwidth=0.8)
    plt.title
    st.pyplot(fig1)

    
    st.subheader('상관 관계 분석')

    selected_list = st.multiselect('상관분석을 하고싶은 컬럼을 선택하세요', column_list)

    df.corr()
    df_corr = df[selected_list].corr()
    
    fig2 = plt.figure()
    sb.heatmap(data= df_corr,annot=True, fmt='.2f', cmap='coolwarm', vmin= -1, vmax= 1, linewidths=0.5)
    st.pyplot(fig2)
    

    


