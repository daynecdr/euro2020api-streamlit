import streamlit as st
import requests


def app():
    st.title('Matches')
    st.image('media/euro2020_teams.png')
    st.text('')
    st.text('')
    # home='HOME'
    # away='AWAY'
    header= st.empty()
    header.title('matchup')
    st.text('')
    match_select=st.slider('use the following slide to select a match and get some info about it',min_value=50,max_value=0)

    url_m='http://192.168.1.44:8080/matches'
    params={}
    match_to_show=requests.get(url_m,params).json()[match_select]

    st.json(match_to_show)
    
    home=match_to_show.get('team_name_home')
    print(home)
    away=match_to_show.get('team_name_away') 
    score1=match_to_show.get('team_home_score')
    score2=match_to_show.get('team_away_score')
    stage=match_to_show.get('stage')   
    if home:
        header.title(f'{home} {score1} : {away} {score2}\n{stage}')

    
        