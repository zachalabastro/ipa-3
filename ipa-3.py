'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    main_from = social_graph[from_member]
    main_to = social_graph[to_member]
    following_from = main_from["following"]
    following_to = main_to["following"]
    if from_member in following_to and to_member in following_from:
        final = "friends"
        return final
    elif from_member in following_to and to_member not in following_from:
        final = "followed by"
        return final
    elif from_member not in following_to and to_member in following_from:
        final = "follower"
        return final
    elif from_member not in following_to and to_member not in following_from:
        final = "no relationship"
        return final


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    for row in board:
        total_indiv_elements = set(row)
        if len(total_indiv_elements) == 1 and row[0] != "":
            winner = row[0]
            return winner
        
    columns = zip(*board)
    new_columns = [list(column) for column in columns]
    for row in new_columns:
        total_indiv_colelements = set(row)
        if len(total_indiv_colelements) == 1 and row[0] != "":
            winner = row[0]
            return winner
        
    diagonal = [board[i][i] for i in range(min(len(board), len(board[0])))]
    total_diagonal_elements = set(diagonal)
    if len(total_diagonal_elements) == 1 and diagonal[0] != "":
        winner = diagonal[0]
        return winner
    
    reverse_diagonal = reverse_diagonal = [board[i][len(board) - i - 1] for i in range(min(len(board), len(board[0])))]
    total_revdiagonal_elements = set(reverse_diagonal)
    if len(total_revdiagonal_elements) == 1 and reverse_diagonal[0] != "":
        winner = reverse_diagonal[0]
        return winner
    
    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    temporary_stop = first_stop
    total_time = 0

    while temporary_stop != second_stop:
        route = (temporary_stop, second_stop)
        if route in route_map:
            total_time += route_map[route]['travel_time_mins']
            temporary_stop = second_stop
        else:
            next_stop = None
            for route in route_map:
                if route[0] == temporary_stop:
                    next_stop = route[1]
                    break
            if next_stop is not None:
                total_time += route_map[route]['travel_time_mins']
                temporary_stop = next_stop
            else:
                return None
        
    return total_time