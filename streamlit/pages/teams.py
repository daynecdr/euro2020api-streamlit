import streamlit as st
import requests

def app():
    st.title('Teams')
    st.image('media/euro_groups.jpeg')
    st.text('Choose a team to see all of its players, you can use the image above as a reference \n Teams are organized by groups')
    st.text('')
    col1, col2, col3 = st.columns(3)

    col1.header('Group A')
    col1.selectbox('choose a team',['None','Turkey','Italy','Wales','Switzerland'])
    

    col2.header('Group B')
    col2.selectbox('choose a team',['None','Denmark','Finland','Belgium','Russia'])

    col3.header('Group C')
    col3.selectbox('choose a team',['None','Netherlands','Ukraine','Austria','North Macedonia'])

    col4,col5,col6 = st.columns(3)
    
    col4.header('Group D')
    col4.selectbox('choose a team',['None','England','Croatia','Scotland','Czech Republic'])

    col5.header('Group E')
    col5.selectbox('choose a team',['None','Spain','Sweden','Poland','Slovakia'])

    col6.header('Group F')
    col6.selectbox('choose a team',['None','Hungary','Portugal','France','Germany'])

    url_t='http://192.168.1.44:8080/teams'
    params={}
    match_to_show=requests.get(url_t,params).json()

    st.json(match_to_show)
    print(team_select)