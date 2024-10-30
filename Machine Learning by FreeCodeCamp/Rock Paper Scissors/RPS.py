# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays
# ago. It is not a very good player, so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=None):
    if opponent_history is None:
        opponent_history = []
    opponent_history.append(prev_play)

    ideal_response = {"P": "S", "R": "P", "S": "R"}

    if prev_play == "":
        return "S"  # Starting with Rock

    last_ten = opponent_history[-10:]

    if len(last_ten) > 3:
        counter = 0
        if last_ten[-3:] == ['P', 'P', 'R']:
            counter += 1
            choises = ['P', 'R', 'S']
            return choises[counter % len(choises)]

    if len(last_ten) > 3:
        if last_ten[-3:] == ['R', 'R', 'R']:
            return "P"
        elif last_ten[-3:] == ['P', 'P', 'P']:
            return "S"
        elif last_ten[-3:] == ['S', 'S', 'S']:
            return "R"

        most_frequent = max(set(last_ten), key=last_ten.count)
    else:
        most_frequent = last_ten[-1] if last_ten else "S"  # Default to Rock if no history

    return ideal_response[most_frequent]