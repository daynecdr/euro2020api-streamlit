# midbootproject_2021 V1.1
    
    This project was done as a project for CORE CODE School Bootcamp
    
    The idea was to create an API to get info from a database prepared by me and have it feed info to an app in Streamlit
    The nature of this project was for learning purposes
     
    The API was created with Flask
    The database is hosted in MongoDB Atlas, and it was concocted through different CSV files, some of which were originally given to us.
    After a process of data enrichment and cleaning, as well as some webscraping, they were uploaded to MongoDB
    The web App was developed through Streamlit
    
    Both the API and streamlit App were converted into Docker images and are hosted on Heroku. They can be accessed here:

    WebApp
    https://euro-streamlit.herokuapp.com/
    
    API
    https://euro2020-api.herokuapp.com/

    Apart from that, Visual Studio Code and Jupyter Notebook were used to code and work through the data. 
    
    
# Data gathering and preparation:

    - There was a given data set for the project, with information about every match. Some columns were dropped from this data set. Information was extracted and transformed via different processes.
       These processes can be found in the jupyter-notebooks in the database folder. But be warned, it's a messy place in there.
    
    - Information was gathered from other sources to include individual player stats per team, and complete team rosters
       some of this info comes from the official UEFO Euro cup web page and was obtained through webscraping 
    
    - The individual player data comes from a csv file found on kaggle.com. Some logic loops were applied in conjuction with previously extracted data to isolate just players participating in the tournament. However, about 20% of the players did not make the cut due to differences in naming conventions and there was no time to apply a proper fix to this issue.
    
      
# Streamlit features:

    The streamlit app is separated into 3 pages: Matches, Teams and Players:
    
    -Matches allows you to select any given match and return info about it.
    -Teams allows you to select any individual team and get its roster.
    -Players shows data on each individual player according to some user-set parameters.
    	
# 2 branches:
    
    The project is divided into two branches: Main and Heroku; The main branch is geared towards working in a localhost environment while the heroku branch has adaptations for its successful deployment in the cloud based service.
    
# Closing comments:

    It's been a blast working on this project, as well as a great learning experience. There is not much here in the way of steps for making this work. If for any reason you are interested, let me know and I'd be happy to help

    Thanks to CORE CODE School (https://www.corecode.school/), to both the teachers and my partners!

