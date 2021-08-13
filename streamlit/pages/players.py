import streamlit as st
import requests

def app():
    st.title('Players')
    st.image('media/player.jpg')
    st.text('')
    st.markdown('#### Set some parameters to filter players and check their stats')


    url_p='http://192.168.1.44:8080/players'

    selector=st.multiselect('stats selector',['age','rating','nationality'])
    


    # params={'overall':91}
    # j_test=requests.get(url_p,params).json()
    # st.json(j_test)
