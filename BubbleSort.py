# A simple bubble sort will work for this program's purposes since the rosters are small (9 players eac)
def bubble_sort(input_roster):
    n = len(input_roster)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if input_roster[j] > input_roster[j + 1]:
                input_roster[j], input_roster[j + 1] = input_roster[j + 1], input_roster[j]
