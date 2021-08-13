import streamlit as st
from multiapp import MultiApp
from pages import home,teams,players,matches


##########AUDIO##########
st.sidebar.markdown('##### An assortment of **_totally_ legal** songs for your enjoyment while you browse this site\n \n \n')
st.sidebar.text('')
st.sidebar.text('')

st.sidebar.text('club foot')
st.sidebar.audio('../../media/club_foot.mp3')

st.sidebar.text('this cold?')
st.sidebar.audio('../../media/this_cold.mp3')

st.sidebar.text('breathe')
st.sidebar.audio('../../media/breathe.mp3')

st.sidebar.text('guerrilla radio')
st.sidebar.audio('../../media/guerrilla.mp3')

st.sidebar.text("what's golden")
st.sidebar.audio('../../media/golden.mp3')

###Radio integration - project on hold
# a = st.sidebar.radio('Radio_core:',[1,2])
# if 1:   
#     st.audio('media/club_foot.mp3')
#########################


st.image('media/euro2020_logo.png')

st.title("UEFA Euro 2020 \n or was it 2021?")



app = MultiApp()

app.add_app("Home", home.app)
app.add_app("Matches", matches.app)
app.add_app("Teams", teams.app)
app.add_app("Players", players.app)

app.run()