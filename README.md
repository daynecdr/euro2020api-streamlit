# midbootproject_2021

    API creation for learning (and enjoyment) purposes
    The API draws info from a database found in MongoDB, which I prepared and uploaded
    The info from the API can be seen through a Streamlit APP developed by me

# Initial vision:
    The project consists of:
      -A(some) data set(s) with info on the UEFA Euro Cup 2020 uplodaded to Mongodb. 
      -An API built with Flask.
      -A streamlit page.
     
     In a future this might be uploaded to Docker, but for now its usage is limited due to being uploaded to MongoDB 
     
    *There is a separate requirements.txt for streamlit
    
# Data gathering and preparation:

    - There was a given data set for the project, with information about every match. Some columns were dropped from this data set. Some information was extracted and transformed via different processes.
    
    - Information was gathered from other sources to include individual player stats per team, and complete team rosters
    some of this info comes from the official UEFO euro cup web page and was obtained through webscraping 
    The individual player data comes from a csv file found on kaggle.com.
    
      
# Streamlit features:

    The streamlit app is separated into 3 pages: Matches, Teams and Players.
    -Matches allows you to select any given match and return info about it.
    -Teams allows you to select any individual team and get its roster.
    -Players shows data on each individual player.
    	*about 20% of the players did not make the cut due to special characters and time constraints, perhaps in v2?
