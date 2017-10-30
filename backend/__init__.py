

def process_user_query(query_string):
    names = query_string.split(' ')
    greetings = [ ]
    for name in query_string.split():
        greetings.append(f'Hi {names}!'')
    return greet
