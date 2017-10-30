

def process_user_query(query_string):
    names = query_string.split(' ')
    greetings = [ ]

    for name in query_string.split():
        greetings.append(f'Hi {names}!')
    return grettings


def greet_upper(query_string):
    capital = query_string.split(' ')
    greet_capital = [ ]
    for char in capital[0]:
        if char in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            greet_capital.append(f'Hi {captial}!')
    return greet_capital
