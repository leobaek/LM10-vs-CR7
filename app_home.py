import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run_home_app() :
    
    st.text('리오넬 메시와 크리스티아누 호날두') 
    st.text('09-10 시즌부터 17-18시즌까지의 통계 데이터 표시')
    st.text('그리고 그 둘을 비교 분석합니다.')
    
    img = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fcafefiles.naver.net%2FMjAxODA4MjRfMTU5%2FMDAxNTM1MTEzNTczMjI5.kD3Lt61vtUURs_ZNQBsDJwe08UJcXDgI-ngKgaZlPPQg.jfR4g7J56iopKihtwT52DvC0FDK0rit39BqK09BAYv0g.JPEG.jfirstlove%2F%25B8%25AE%25BF%25C0%25B3%25DA_%25B8%25DE%25BD%25C3.jpg&type=sc960_832'
    img2 = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fcafefiles.naver.net%2FMjAxNzAxMjFfNzUg%2FMDAxNDg0OTczOTEyODc5.fYwkOJQFe8dEYldnQw9Yr2-IUiCmcqYxJ2kDYpMx8Tgg.AWfJDU27Bm-4beLKh7HuzEKDCZ4rHhg5PATXmc35U6gg.JPEG.com582%2FexternalFile.jpg&type=sc960_832'
    st.image([img,img2] , width= 300)

    if __name__ =='__main__' :
        main()

        