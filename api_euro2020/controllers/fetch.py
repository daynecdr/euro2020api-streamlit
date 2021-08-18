from app import app
from flask import request
from utils.json_response import json_response, str_json
from utils.mongo_connect import mongo_read
from utils.type_casting import cast_types_matches, cast_types_stats
from utils.handle_error import handle_error

@app.get('/')
@handle_error
def first_page():
    return {'UEFA Euro 2020':'or was it 2021?',
            'endpoints':'teams, players, matches',
        }

@app.get('/test')
@handle_error
def test_page():
    return {'this page':'was created',
            'in order to check if':'endpoints are working',
        }

@app.get('/teams')
@handle_error
def get_teams():
    q = dict(request.args)
    if 'mongo_query' in q.keys():
        q=str_json(q['mongo_query'])
    print (q)    
    return json_response(list(mongo_read('bdml_project','all_players_team',q)))

    
@app.get('/players')
@handle_error
def get_players():
    q=cast_types_stats(**dict(request.args))
    if 'mongo_query' in q.keys():
        q=str_json(q['mongo_query'])
    print (q)
    return json_response(list(mongo_read('bdml_project','player_stats_rec',q)))


@app.get('/matches')
@handle_error
def get_matches():
    q=cast_types_matches(**dict(request.args))
    if 'mongo_query' in q.keys():
        q=str_json(q['mongo_query'])
    print (q)
    return json_response(list(mongo_read('bdml_project','matches_rec',q).sort("_id",-1)))
