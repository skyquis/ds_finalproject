# This Game class will control the logic of the baseball game. Will contain info such as Innings, Scores,
# Team Names, etc.

class Game:
    def __init__(self, team1_name="Away", team2_name="Home"):
        self.inning = 1
        self.outs = 0
        self.team_1_name = team1_name
        self.team_2_name = team2_name
        self.away_score = 0
        self.home_score = 0
        self.play_outcome = 10
        self.away_team_at_bat = True
        self.first_base_loaded = False
        self.second_base_loaded = False
        self.third_base_loaded = False

    def display_inning_string(self):
        if self.away_team_at_bat:
            inning_half = "Inning: Top "
        else:
            inning_half = "Inning: Bottom "
        return str(inning_half) + str(self.inning)

    def display_out_string(self):
        out_string = "Outs: " + str(self.outs)
        return out_string

    def display_team1_name_var(self):
        return self.team_1_name

    def display_team2_name_var(self):
        return self.team_2_name

    def map_to_bases_pc(self):
        if self.first_base_loaded and self.second_base_loaded and self.third_base_loaded:
            return "123.jpg"
        elif self.first_base_loaded and self.second_base_loaded:
            return "12.jpg"
        elif self.first_base_loaded and self.third_base_loaded:
            return "13.jpg"
        elif self.second_base_loaded and self.third_base_loaded:
            return "23.jpg"
        elif self.first_base_loaded:
            return "1.jpg"
        elif self.third_base_loaded:
            return "3.jpg"
        elif self.second_base_loaded:
            return "2.jpg"
        else:
            return "Bases Empty.jpg"


    # This function will be called in a play outcome of 3 (triple), or 4 (home run) since the bases will be empty after.
    # It also will be called in the case of getting to out 3.
    def clear_bases(self):
        self.first_base_loaded = False
        self.second_base_loaded = False
        self.third_base_loaded = False

    def increment_score(self):
        if self.away_team_at_bat:
            self.away_score += 1
        else:
            self.home_score += 1

    def play_result(self):
        # Resolve if "Out" first
        if self.play_outcome == 0:
            self.outs += 1
            if self.outs == 3:
                if not self.away_team_at_bat:
                    self.inning += 1
                self.away_team_at_bat = not self.away_team_at_bat
                self.clear_bases()
                self.outs = 0
        # Resolve a Single
        elif self.play_outcome == 1:
            if self.third_base_loaded:
                if self.away_team_at_bat:
                    self.away_score += 1
                else:
                    self.home_score += 1
                self.third_base_loaded = False
            if self.second_base_loaded:
                self.third_base_loaded = True
                self.second_base_loaded = False
            if self.first_base_loaded:
                self.second_base_loaded = True
            self.first_base_loaded = True
        # Resolve a Double
        elif self.play_outcome == 2:
            if self.third_base_loaded:
                if self.away_team_at_bat:
                    self.away_score += 1
                else:
                    self.home_score += 1
                self.third_base_loaded = False
            if self.second_base_loaded:
                if self.away_team_at_bat:
                    self.away_score += 1
                else:
                    self.home_score += 1
            if self.first_base_loaded:
                self.third_base_loaded = True
            self.second_base_loaded = True
            self.first_base_loaded = False
        # Resolve a Triple
        elif self.play_outcome == 3:
            if self.third_base_loaded:
                self.increment_score()
            if self.second_base_loaded:
                self.increment_score()
            if self.first_base_loaded:
                self.increment_score()
            self.clear_bases()
            self.third_base_loaded = True
        # Resolve a Home Run
        elif self.play_outcome == 4:
            if self.third_base_loaded:
                self.increment_score()
            if self.second_base_loaded:
                self.increment_score()
            if self.first_base_loaded:
                self.increment_score()
            self.clear_bases()
            self.increment_score()

