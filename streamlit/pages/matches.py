import streamlit as st
import requests


def app():
    #st.title('Matches')
    st.image('media/euro2020_teams.png')
    st.text('')
    st.text('')
        
    match_select=st.slider('Use the following slide to select a match and get some info about it',min_value=0,max_value=50)

    url_m='http://192.168.1.44:8080/matches'
    params={}
    match_to_show=requests.get(url_m,params).json()[match_select]
    
    header= st.empty()
    header.title('')

    colA, colB, colC = st.columns(3)
    col1, col2, col3 = st.columns(3)
    

    st.text('')
    st.text('Below is the full data for the match')
    st.text('')
    st.json(match_to_show)
    
    home=match_to_show.get('team_name_home')
    away=match_to_show.get('team_name_away') 
    score1=match_to_show.get('team_home_score')
    score2=match_to_show.get('team_away_score')
    shots1=match_to_show.get('total_shots_home')
    shots2=match_to_show.get('total_shots_away')
    target1=match_to_show.get('shots_on_target_home')
    target2=match_to_show.get('shots_on_target_away')
    poss1=match_to_show.get('possession_home')
    poss2=match_to_show.get('possession_away')
    stage=match_to_show.get('stage')   
    if home:

        colB.markdown(f'#### {stage}')
        #header.title(f'{home} {score1} : {away} {score2}\n{stage}')
        #col1.header('')
        col1.title(f'{home}')
        col1.markdown(f'### {shots1}')
        col1.markdown(f'### {target1}')
        col1.markdown(f'### {poss1}')

        #col2.text(f'{stage}')
        col2.title(f'{score1}:{score2}')
        col2.markdown('### shots')
        col2.markdown('### shots on target')
        col2.markdown('### possession')

        #col3.header('')
        col3.title(f'{away}')
        col3.markdown(f'### {shots2}')
        col3.markdown(f'### {target2}')
        col3.markdown(f'### {poss2}')
    
        