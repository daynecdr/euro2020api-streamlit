import streamlit as st
import requests

def app():
    #st.title('Players')
    
    col1, col2, col3 = st.columns(3)
    col1.image('media/player.jpg')
    col2.image('media/player2.jpg')
    col3.image('media/player3.jpg')

    col4, col5, col6 =st.columns(3)
    col4.image('media/player4.jpg')
    col5.image('media/player5.jpg')
    col6.image('media/player6.jpg')

    
    st.text('')
    st.markdown('#### Set some parameters to filter players and check their stats')

    cola, colb = st.columns(2)
    
    age_option=cola.radio('age', ['off','exact match','older than', 'younger than'])
    cola.text('')    
    age=cola.slider('select age: ',min_value=16, max_value=41)
    #   
    
    skill_option=colb.radio('skill', ['off','exact match','better than', 'worse than'])
    colb.text('')    
    skill=colb.slider('select skill: ',min_value=50,max_value=99)
    #

    # nationality_option=colc.radio('nationality',['off', 'on','this option does nothing','this button is worthless'])
    # colc.text('')
    # nat=None
    # nat=colc.text_input('enter nationality: ')
    
    turn_giver=st.button('Show me the results!')
    if not turn_giver:
        st.stop()
    
    # if age:
    #     age=int(age)
    # if skill:
    #     skill=int(skill)
    params=None
    
    if age_option=='exact match' and skill_option=='off' :
        params={'age': age}
        print (params,type(params),'worked')

    if age_option=='exact match' and skill_option=='exact match':
        params={"mongo_query": f'{{"$and":[{{"age":{age}}},{{"overall":{skill}}}]}}'}
        print (params,type(params),'workkkt')

    if age_option=='exact match' and skill_option=='better than':
        params={"mongo_query": f'{{"$and":[{{"age":{age}}},{{"overall":{{"$gt":{skill}}}}}]}}'}
        print (params,type(params),'workkkt')

    if age_option=='exact match' and skill_option=='worse than':
        params={"mongo_query": f'{{"$and":[{{"age":{age}}},{{"overall":{{"$lt":{skill}}}}}]}}'}
        print (params,type(params),'workkkt')
    
    if age_option=='off' and skill_option=='exact match':
        params={'overall':skill}
        print (params,type(params),'workkkt')

    if age_option=='off' and skill_option=='better than':
        params={"mongo_query": f'{{"overall":{{"$gt":{skill}}}}}'}
        print (params,type(params),'workkkt')

    if age_option=='off' and skill_option=='worse than':
        params={"mongo_query": f'{{"overall":{{"$lt":{skill}}}}}'}
        print (params,type(params),'workkkt')

    if age_option=='older than' and skill_option=='off' :
        params={"mongo_query": f'{{"age":{{"$gt":{age}}}}}'}
        print (params,type(params),'worked')

    if age_option=='older than' and skill_option=='exact match' :
        params={"mongo_query": f'{{"$and":[{{"overall":{skill}}},{{"age":{{"$gt":{age}}}}}]}}'}
        print (params,type(params),'worked')

    if age_option=='older than' and skill_option=='better than' :
        params={"mongo_query": f'{{"$and":[{{"age":{{"$gt":{age}}}}},{{"overall":{{"$gt":{skill}}}}}]}}'}
        print (params,type(params),'worked')
    
    if age_option=='older than' and skill_option=='worse than' :
        params={"mongo_query": f'{{"$and":[{{"age":{{"$gt":{age}}}}},{{"overall":{{"$lt":{skill}}}}}]}}'}
        print (params,type(params),'worked')
        
    if age_option=='younger than' and skill_option=='off' :
        params={"mongo_query": f'{{"age":{{"$lt":{age}}}}}'}
        print (params,type(params),'worked')

    if age_option=='younger than' and skill_option=='exact match' :
        params={"mongo_query": f'{{"$and":[{{"overall":{skill}}},{{"age":{{"$lt":{age}}}}}]}}'}
        print (params,type(params),'worked')

    if age_option=='younger than' and skill_option=='better than' :
        params={"mongo_query": f'{{"$and":[{{"age":{{"$lt":{age}}}}},{{"overall":{{"$gt":{skill}}}}}]}}'}
        print (params,type(params),'worked')
    
    if age_option=='younger than' and skill_option=='worse than' :
        params={"mongo_query": f'{{"$and":[{{"age":{{"$lt":{age}}}}},{{"overall":{{"$lt":{skill}}}}}]}}'}
        print (params,type(params),'worked')
    

    
    
    
    
    #params={'age':24}
    #params={"mongo_query": f'{{"$and":[{{"age":{None}}},{{"overall":}}]}}'}
    
    url_p='http://192.168.1.44:8080/players'
    players_to_show=requests.get(url_p,params).json()

    #print(age_option,skill_option,nationality_option)
    #print(age,skill,nat)
    print(players_to_show)
    print(params)
    print (type(params))
    num=0
    for data in players_to_show:
        print(data)
        num += 1
    print (num)
    print(params)
    st.markdown(f'### There are {num} players matching those parameters')
    # print(type(age))
    # print(type(skill))
    # params={'overall':91}
    # j_test=requests.get(url_p,params).json()
    st.json(players_to_show)
