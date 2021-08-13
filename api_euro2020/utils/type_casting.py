TYPES_STATS = {
        'overall':int,
        'age':int,
        'potential':int
}

TYPES_MATCHES = {
    'team_home_score':int,
    'team_away_score':int,
    'total_shots_home':int,
    'total_shots_away':int,
    'shots_on_target_home':int,
    'shots_on_target_away':int,
    'pens':bool
}

def check_types(typ):
    def decorator_kreator(fn):
        def wrapper(**kwargs):
            for k,v in kwargs.items():
                kwargs[k] = typ.get(k, str)(v)
            return fn(**kwargs)
        return wrapper
    return decorator_kreator

@check_types(TYPES_STATS)
def cast_types_stats(**kwargs):
    return kwargs

@check_types(TYPES_MATCHES)
def cast_types_matches(**kwargs):
    return kwargs