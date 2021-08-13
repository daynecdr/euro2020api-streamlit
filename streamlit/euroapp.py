import streamlit as st
from multiapp import MultiApp
from pages import home,teams,players,matches


##########AUDIO##########
# st.sidebar.markdown('##### An assortment of **_totally_ legal** songs for your enjoyment while you browse this site\n \n \n')
# st.sidebar.text('')
# st.sidebar.text('')

# st.sidebar.text('club foot')
# st.sidebar.audio('../../media/club_foot.mp3')

# st.sidebar.text('this cold?')
# st.sidebar.audio('../../media/this_cold.mp3')

# st.sidebar.text('breathe')
# st.sidebar.audio('../../media/breathe.mp3')

# st.sidebar.text('guerrilla radio')
# st.sidebar.audio('../../media/guerrilla.mp3')

# st.sidebar.text("view from the afternoon")
# st.sidebar.audio('../../media/view_afternoon.mp3')

# st.sidebar.text("what's golden")
# st.sidebar.audio('../../media/golden.mp3')
#########################
#this files are commented out because they depend on local files

st.image('media/euro2020_logo.png')

st.title("UEFA Euro 2020 \nor was it 2021?")



app = MultiApp()

app.add_app("Home", home.app)
app.add_app("Matches", matches.app)
app.add_app("Teams", teams.app)
app.add_app("Players", players.app)


app.run()