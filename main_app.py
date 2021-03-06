import streamlit as st
import pygsheets
import pandas as pd

st.title('PRJ_빵댕이를 흔들 수 있습니까?')

with open("text.md") as f:
    st.markdown(f.read())

checkboxlv1 = st.checkbox('너무 좋아요!', key='lv1')
if checkboxlv1:
    st.image('im.jpeg')

    with open("info.md") as f:
        st.markdown(f.read())

    checkboxlv2 = st.checkbox('네, 초대할게요!')
    if checkboxlv2:
        with open("money.md") as f:
            st.markdown(f.read())
            
        checkboxlv3 = st.checkbox('네, 알겠습니다!')
        if checkboxlv3:
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
                    new = new.drop_duplicates()

                    ws1.clear()
                    ws1.set_dataframe(new,(1,1))

                    st.text('신청이 완료되었습니다!')

