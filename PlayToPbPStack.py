# This Python file will contain a method that takes in a player name and play outcome and returns a play-by-play string
def outcome_to_string(play_outcome):
    match play_outcome:
        case 1:
            return " has hit a single."
        case 2:
            return " has hit a double."
        case 3:
            return " has hit a triple."
        case 4:
            return " has hit a home run!"
        case 0:
            return " is out."


def play_to_pbp_string(player, play_outcome):
    pbp_string = player + outcome_to_string(play_outcome)
    return pbp_string
