# midbootproject_2021

    API creation for learning (and enjoyment) purposes

# Initial vision:
    The project will consist of:
      -A(some) data set(s) with info on the UEFA Euro Cup 2020 uplodaded to Mongodb. 
      -An API built with Flask.
      -A streamlit page.
      
    *There is a separate requirements.txt for streamlit
    
# Data gathering and preparation:

    - There is a given data set for the project, with information about every match. Some columns will
    probably be dropped from this data set. Some information will be extracted via differetn processes.
    
    - Information will be gathered from other sources to include individual player stats per team, and complete team rosters
    some of this info comes from the official UEFO euro cup web page and will be obtained through webscraping 
    The individual player data comes from a csv file found on kaggle.com.
      
# Streamlit desired features:

    The idea is for the streamlit to be separated into 3 pages: Matches, Teams and Players.
    -Matches will allow you to select any given match and return info about it.
    -Teams will allow you to select any individual team and get its roster.
    -Players will show data on each individual player
