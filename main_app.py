import streamlit as st
import pygsheets
import pandas as pd

st.title('PRJ_빵댕이를 흔들 수  있습니까?')
st.image('im.jpeg')
st.subheader('신청하기')

with st.form(key='my_form'):
    name = st.text_input(label='이름을 입력하세요')
    number = st.text_input(label='전화번호를 알려주세요')
    submit_button = st.form_submit_button(label='Submit')
    
    if submit_button:
        login_credential = 'future-disruption-index-adc3981eedd2.json'
        gc = pygsheets.authorize(service_file=login_credential)

        sh = gc.open_by_key('18j_RUQmj_Aox6VulRxEvfSbV7LfUlridVc6cWH1rc0U')
        ws1 = sh[0]
        original = ws1.get_as_df()

        update = pd.DataFrame({'이름':name,"전화번호":number},index=[0])
        new = pd.concat([original,update])

        ws1.clear()
        ws1.set_dataframe(new,(1,1))

        st.text('신청이 완료되었습니다!')

