# Import tkinter
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import re

from Game import Game
from BattingOrder import BattingOrderQueue
from PlayToPbPStack import play_to_pbp_string
from BubbleSort import bubble_sort

# Set a constant
ROSTER_SIZE = 9


class Teams:
    def __init__(self):
        self.team1_name = ""
        self.team2_name = ""
        self.team1_players = []
        self.team2_players = []

    def submit_teams(self):
        team1_name = entry_team1_name.get()
        team1_players = [entry_team1_player1.get(), entry_team1_player2.get(), entry_team1_player3.get(),
                         entry_team1_player4.get(), entry_team1_player5.get(), entry_team1_player6.get(),
                         entry_team1_player7.get(), entry_team1_player8.get(), entry_team1_player9.get()]

        team2_name = entry_team2_name.get()
        team2_players = [entry_team2_player1.get(), entry_team2_player2.get(), entry_team2_player3.get(),
                         entry_team2_player4.get(), entry_team2_player5.get(), entry_team2_player6.get(),
                         entry_team2_player7.get(), entry_team2_player8.get(), entry_team2_player9.get()]

        invalid = False
        if not check_if_valid_entry(team1_name) or not check_if_valid_entry(team2_name):
            display_invalid_entry_message()
            invalid = True
        else:
            j = 0
            while j < ROSTER_SIZE:
                if not check_if_valid_entry(team1_players[j]):
                    display_invalid_entry_message()
                    invalid = True
                    break
                if not check_if_valid_entry(team2_players[j]):
                    display_invalid_entry_message()
                    invalid = True
                    break
                j += 1

        if not invalid:
            # Once you pass through with valid results, now what?
            self.team1_name = team1_name
            self.team2_name = team2_name
            self.team1_players = team1_players
            self.team2_players = team2_players
            display_valid_entry_message()


# This will check if the entered team names and player names follow the validity requirements
def check_if_valid_entry(input_entry):
    valid_characters = re.compile("^[a-zA-Z -\']*$")
    if valid_characters.match(input_entry):
        # Make sure it isn't only spaces
        return any(char.isalnum() for char in input_entry)
    return False


def display_invalid_entry_message():
    messagebox.showerror('Invalid entry', 'Detected at least one invalid entry in team names and players. Valid input '
                                          'includes alphabet characters, spaces, apostrophes, and dashes. Only space '
                                          'entries are not allowed. Please edit input and resubmit.')
    window.destroy()


def display_valid_entry_message():
    messagebox.showinfo('Entry success!', 'Teams and players have been saved!')
    window.destroy()


def display_game_over_message():
    if new_game.away_score > new_game.home_score:
        game_over_string = new_game.team_1_name + " have beat " + new_game.team_2_name + " by a score of " + \
                           str(new_game.away_score) + " to " + str(new_game.home_score) + ". Thanks for playing!"
    elif new_game.away_score < new_game.home_score:
        game_over_string = new_game.team_2_name + " have beat " + new_game.team_1_name + " by a score of " + \
                           str(new_game.home_score) + " to " + str(new_game.away_score) + ". Thanks for playing!"
    else:
        game_over_string = new_game.team_1_name + " have tied " + new_game.team_2_name + " with a score of " + \
                           str(new_game.away_score) + " to " + str(new_game.home_score) + ". Thanks for playing!"
    messagebox.showinfo('Game over!', game_over_string)
    window.destroy()


# Create the first window for team and roster entry
window = tk.Tk()
window.title("Team and Roster Entry")

# Setup two new teams
new_teams = Teams()

# Team 1 entry fields
label_team1 = tk.Label(window, text="Team 1")
label_team1.grid(row=0, column=0, columnspan=2)

label_team1_name = tk.Label(window, text="Team Name:")
label_team1_name.grid(row=1, column=0, sticky="E")
entry_team1_name = tk.Entry(window)
entry_team1_name.grid(row=1, column=1)

label_team1_players = tk.Label(window, text="Players:")
label_team1_players.grid(row=2, column=0, sticky="E")

entry_team1_player1 = tk.Entry(window)
entry_team1_player1.grid(row=2, column=1)

entry_team1_player2 = tk.Entry(window)
entry_team1_player2.grid(row=3, column=1)

entry_team1_player3 = tk.Entry(window)
entry_team1_player3.grid(row=4, column=1)

entry_team1_player4 = tk.Entry(window)
entry_team1_player4.grid(row=5, column=1)

entry_team1_player5 = tk.Entry(window)
entry_team1_player5.grid(row=6, column=1)

entry_team1_player6 = tk.Entry(window)
entry_team1_player6.grid(row=7, column=1)

entry_team1_player7 = tk.Entry(window)
entry_team1_player7.grid(row=8, column=1)

entry_team1_player8 = tk.Entry(window)
entry_team1_player8.grid(row=9, column=1)

entry_team1_player9 = tk.Entry(window)
entry_team1_player9.grid(row=10, column=1)

# Team 2 entry fields
label_team2 = tk.Label(window, text="Team 2")
label_team2.grid(row=0, column=2, columnspan=2)

label_team2_name = tk.Label(window, text="Team Name:")
label_team2_name.grid(row=1, column=2, sticky="E")
entry_team2_name = tk.Entry(window)
entry_team2_name.grid(row=1, column=3)

label_team2_players = tk.Label(window, text="Players:")
label_team2_players.grid(row=2, column=2, sticky="E")

entry_team2_player1 = tk.Entry(window)
entry_team2_player1.grid(row=2, column=3)

entry_team2_player2 = tk.Entry(window)
entry_team2_player2.grid(row=3, column=3)

entry_team2_player3 = tk.Entry(window)
entry_team2_player3.grid(row=4, column=3)

entry_team2_player4 = tk.Entry(window)
entry_team2_player4.grid(row=5, column=3)

entry_team2_player5 = tk.Entry(window)
entry_team2_player5.grid(row=6, column=3)

entry_team2_player6 = tk.Entry(window)
entry_team2_player6.grid(row=7, column=3)

entry_team2_player7 = tk.Entry(window)
entry_team2_player7.grid(row=8, column=3)

entry_team2_player8 = tk.Entry(window)
entry_team2_player8.grid(row=9, column=3)

entry_team2_player9 = tk.Entry(window)
entry_team2_player9.grid(row=10, column=3)

# Save Teams Button
submit_button = tk.Button(window, text="Save Teams", command=new_teams.submit_teams)
submit_button.grid(row=11, column=0, columnspan=4)

# Start the main loop
window.mainloop()


# Setup new game
new_game = Game(new_teams.team1_name, new_teams.team2_name)

# Set constant
INNINGS_IN_GAME = 9

# Sort teams before this
bubble_sort(new_teams.team1_players)
bubble_sort(new_teams.team2_players)

if new_game.team_1_name != "":
    # Setup batting orders
    away_batting_order = BattingOrderQueue()
    home_batting_order = BattingOrderQueue()
    for j in range(ROSTER_SIZE-1):
        away_batting_order.enqueue(new_teams.team1_players[j])
        home_batting_order.enqueue(new_teams.team2_players[j])

window = tk.Tk()


# This will refresh a value (after a "submit" is clicked)
def update_value(value_type, new_value):
    value_type.set(new_value)


# This will update the baseball logo to match the team at bat
def updated_baseball_column():
    if new_game.away_team_at_bat:
        return 1
    else:
        return 5


# This will update the baseball diamond image based on which bases have loaded set to True
def update_diamond_image():
    image2 = "C:\\Users\\skyle\\PycharmProjects\\ds_finalproject\\" + new_game.map_to_bases_pc()
    image2 = Image.open(image2).resize((100, 100))
    test2 = ImageTk.PhotoImage(image2)
    diamond_label = tk.Label(image=test2)
    diamond_label.image = test2
    diamond_label.grid(row=3, column=3)


# This will update the name of the at bat and on deck players
def update_at_bat_on_deck():
    if new_game.away_team_at_bat:
        at_bat_player.set(away_batting_order.dequeue())
        on_deck_player.set(away_batting_order.peek())
    else:
        at_bat_player.set(home_batting_order.dequeue())
        on_deck_player.set(home_batting_order.peek())


# Row 0 - Label
window_label = tk.Label(text="Baseball Scoreboard")
window_label.grid(row=0, column=3)

# Row 1 - Outs and Innings
outs = tk.StringVar()
outs.set(new_game.display_out_string())
outs_label = tk.Label(textvariable=outs)
outs_label.grid(row=1, column=2)

innings = tk.StringVar()
innings.set(new_game.display_inning_string())
innings_label = tk.Label(textvariable=innings)
innings_label.grid(row=1, column=4)

# Row 2 - Team Names and hitting team indicator (baseball image)
fir_team = tk.StringVar()
fir_team.set(new_game.display_team1_name_var())
first_team_label = tk.Label(textvariable=fir_team, font=('Arial', 18, 'bold'))
first_team_label.grid(row=2, column=2)
sec_team = tk.StringVar()
sec_team.set(new_game.display_team2_name_var())
second_team_label = tk.Label(textvariable=sec_team, font=('Arial', 18, 'bold'))
second_team_label.grid(row=2, column=4)

if new_game.away_team_at_bat:
    baseball_column = 1
else:
    baseball_column = 5

image1 = Image.open("C:\\Users\\skyle\\PycharmProjects\\ds_finalproject\\baseball-icon-33.jpg").resize((30, 30))
test = ImageTk.PhotoImage(image1)
baseball_label = tk.Label(image=test)
baseball_label.image = test
baseball_label.grid(row=2, column=updated_baseball_column())

# Row 3 - Scores, diamond image
away_score = tk.StringVar()
away_score.set(new_game.away_score)
away_score_label = tk.Label(textvariable=away_score, font=('Arial', 32, 'bold'))
away_score_label.grid(row=3, column=2)

home_score = tk.StringVar()
home_score.set(new_game.home_score)
home_score_label = tk.Label(textvariable=home_score, font=('Arial', 32, 'bold'))
home_score_label.grid(row=3, column=4)

# Setting up baseball diamond image based on which base have loaded set to True
update_diamond_image()

# Row 4-7 - At-Bat / On-Deck
ab_label = tk.Label(text="At Bat: ", font=('Arial', 12, 'bold'))
ab_label.grid(row=4, column=3)


if new_game.team_1_name != "":
    at_bat_player = tk.StringVar()
    on_deck_player = tk.StringVar()
    if new_game.away_team_at_bat:
        at_bat_player.set(away_batting_order.dequeue())
        on_deck_player.set(away_batting_order.peek())
    else:
        at_bat_player.set(home_batting_order.dequeue())
        on_deck_player.set(home_batting_order.peek())
    at_bat_label = tk.Label(textvariable=at_bat_player, font=('Comic Sans', 12))
    at_bat_label.grid(row=5, column=3)

    # Row 5 - On Deck
    od_label = tk.Label(text="On Deck: ", font=('Arial', 12, 'bold'))
    od_label.grid(row=6, column=3)

    on_deck_label = tk.Label(textvariable=on_deck_player, font=('Comic Sans', 12))
    on_deck_label.grid(row=7, column=3)


# Row 6 - Play Outcome Options
variable = tk.IntVar(window)
tk.Radiobutton(window, text="Out", variable=variable, value=0).grid(row=8, column=1)
tk.Radiobutton(window, text="Single", variable=variable, value=1).grid(row=8, column=2)
tk.Radiobutton(window, text="Double", variable=variable, value=2).grid(row=8, column=3)
tk.Radiobutton(window, text="Triple", variable=variable, value=3).grid(row=8, column=4)
tk.Radiobutton(window, text="Home run", variable=variable, value=4).grid(row=8, column=5)


# Row 7 - Submit button
# This needs to do a lot of things including: move at_bat player back to end of batting order, tally a hit to move
# runners (and increment score if needed), or tally an out (and potentially switch at bat team / half of inning), and
# put a play on pbp stack, or clear the stack
def resolve_play():
    # Put play on stack, refresh popped play
    temp_store_at_bat_player = at_bat_player.get()
    if new_game.away_team_at_bat:
        away_batting_order.enqueue(at_bat_player.get())
    else:
        home_batting_order.enqueue(at_bat_player.get())

    new_game.play_outcome = variable.get()
    pbp_string = play_to_pbp_string(temp_store_at_bat_player, new_game.play_outcome)
    new_game.play_result()
    update_at_bat_on_deck()

    # Update all values
    update_value(outs, new_game.display_out_string())
    update_value(innings, new_game.display_inning_string())
    update_value(away_score, new_game.away_score)
    update_value(home_score, new_game.home_score)
    if new_game.inning <= INNINGS_IN_GAME:
        update_value(pbp, pbp_string)
        baseball_label.grid(row=2, column=updated_baseball_column())
        update_diamond_image()
    else:
        update_value(pbp, "Game Over!")
        display_game_over_message()


# Checking if window is destroyed
if new_game.inning <= INNINGS_IN_GAME:
    Button = tk.Button(window, text="Log play", command=resolve_play)
    Button.grid(row=9, column=3)

    # Row 8 - Play by play label
    pbp_label = tk.Label(text="Last play: ", font=('Arial', 12, 'bold'))
    pbp_label.grid(row=10, column=3)

    # Row 9 - "Popped" play
    pbp = tk.StringVar()
    pbp.set("Game start!")
    pbp_label = tk.Label(textvariable=pbp, font=('Arial', 12))
    pbp_label.grid(row=11, column=3)

if new_game.team_1_name != "":
    window.mainloop()
