import streamlit as st
import requests

def app():
    #st.title('Teams')
    st.image('media/euro_groups.jpeg')
    st.text('Choose a team to see all of its players, you can use the image above as a reference \nTeams are organized by groups')
    st.text('')
 

    url_t='https://euro2020-api.herokuapp.com/teams'
    params={}
    team_to_show=requests.get(url_t,params).json()

    team_name=None
    get_team=None
    gkp=None
    dfns=None
    mid=None
    frw=None
    team_name=st.text_input('Write the name of the team to check its full roster. Capitalize countries. N. Macedonia should be spelled North Macedonia')
    error=st.empty()
    
    for data in team_to_show:
        if team_name==data.get('Team'):
            get_team=team_name
        # if team_name==None:
        #     pass    
        # else:
        #     error=st.text('Team not found, check your spelling. Team name should be capitalized. If you are looking for North Macedonia, spell it out')
        #     break

    for data in team_to_show:
        if get_team==data.get('Team'):
            gkp=data.get('Goalkeepers')
            dfns=data.get('Defenders')
            mid=data.get('Midfielders')
            frw=data.get('Forwards')
    
        # for data in team_to_show:
        #     if team_name==data.get('Team'): 
        #         error=st.text('Team not found, check your spelling. Team name should be capitalized. If you are looking for North Macedonia, spell it out')

    if gkp:
        st.markdown(f'## {get_team}')
        st.markdown(f'## Goal Keepers:\n {gkp}')
        st.markdown(f'## Defenders:\n {dfns}')
        st.markdown(f'## Midfielders:\n {mid}')
        st.markdown(f'## Forwards:\n {frw}')


        # print (data.get('Team'))
    # try:
    
    # except:
    
    #home=match_to_show.get('team_name_home')

    #st.json(team_to_show)
    #print(team_name)








    ##################DEPRECATED##################

    # col1, col2, col3 = st.columns(3)

    # col1.header('Group A')
    # col1.selectbox('choose a team',['None','Turkey','Italy','Wales','Switzerland'])
    

    # col2.header('Group B')
    # col2.selectbox('choose a team',['None','Denmark','Finland','Belgium','Russia'])

    # col3.header('Group C')
    # col3.selectbox('choose a team',['None','Netherlands','Ukraine','Austria','North Macedonia'])

    # col4,col5,col6 = st.columns(3)
    
    # col4.header('Group D')
    # col4.selectbox('choose a team',['None','England','Croatia','Scotland','Czech Republic'])

    # col5.header('Group E')
    # col5.selectbox('choose a team',['None','Spain','Sweden','Poland','Slovakia'])

    # col6.header('Group F')
    # col6.selectbox('choose a team',['None','Hungary','Portugal','France','Germany'])