import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
def run_R_app() :
    st.subheader('Cristiano Ronaldo')
    img = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fcafefiles.naver.net%2F20140501_5%2Freconjuni_1398938726110ey1Do_GIF%2F__1_1.GIF&type=sc960_832_gif'
    st.image(img)


    df = pd.read_csv('MessiRonaldo.csv')
    R= df.iloc[[1,3,5,7,9,11,13,15,17], :]
    R['Total Goal'] = R['Liga_Goals'] + R['CL_Goals']

    st.subheader('모든 통계는 2009시즌부터 2018시즌까지입니다.')
    st.subheader('Cristiano Ronaldo 시즌 별 통계')
    st.dataframe(R)

    R['Total Goals'] = R['Liga_Goals'] + R['CL_Goals']
    R_max = R.loc[(R['Liga_Goals'] + R['CL_Goals'] == 58), ['Season','Liga_Goals','CL_Goals','Total Goals'] ]

## 셀렉트박스
    lang = ['Liga 통산 골' , 'Liga 통산 어시스트' , 'CL 통산 골', 'CL 통산 어시스트' ,'한 해 최다 골']
    selected_lang = st.selectbox('확인 할 데이터를 선택하세요', lang)
    lg = 'Messi는 Liga에서 통산 329골을 넣었습니다.'
    if selected_lang == lang[0]:
        st.write('Ronaldo는 Liga에서 통산 292골을 넣었습니다.')
    
    elif selected_lang == lang[1]:
        st.write('Ronaldo는 Liga에서 통산 97어시스트를 기록했습니다.')

    elif selected_lang == lang[2]:
        st.write('Ronaldo는 CL에서 통산 105골을 넣었습니다.')

    elif selected_lang == lang[3]:
        st.write('Ronaldo는 CL에서 통산 33어시스트를 기록했습니다.')

    elif selected_lang == lang[4]:
        st.write('Ronaldo의 한 해 최다 골은 58골입니다.')


    st.subheader('히스토그램')
    
    column_list = R.columns[2: ]
    histogram_column = st.selectbox('히스토그램 확인할 컬럼을 선택하세요', column_list)
    my_bins = st.number_input('빈의 갯수를 입력하세요', 5, 30, value=10,step=1)
    
    fig1 = plt.figure()
    plt.hist(data=R , x= histogram_column , bins= my_bins ,rwidth=0.8)
    plt.title
    st.pyplot(fig1)

    
    st.subheader('상관 관계 분석')

    selected_list = st.multiselect('상관분석을 하고싶은 컬럼을 선택하세요', column_list)

    df.corr()
    df_corr = df[selected_list].corr()
    
    fig2 = plt.figure()
    sb.heatmap(data= df_corr,annot=True, fmt='.2f', cmap='coolwarm', vmin= -1, vmax= 1, linewidths=0.5)
    st.pyplot(fig2)