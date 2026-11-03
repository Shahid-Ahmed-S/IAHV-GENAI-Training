import pandas as pd

def get_team_data(team_name):
    print(f"\nEnter bowling details for {team_name}")
    n = int(input("Enter number of bowlers: "))

    if n <= 0:
        print("Error: Number of players must be greater than 0.")
        return None

    data = []
    for i in range(n):
        print(f"\nPlayer {i + 1}")
        name = input("Player name: ")
        overs = float(input("Overs bowled: "))
        maidens = int(input("Maiden overs: "))
        runs = int(input("Runs conceded: "))
        wickets = int(input("Wickets taken: "))
        extras = int(input("Extras: "))
        data.append([
            name, overs, maidens, runs, wickets, extras
        ])

    df = pd.DataFrame(
        data,
        columns=[
            "Player",
            "Overs",
            "Maidens",
            "Runs",
            "Wickets",
            "Extras"
        ]
    )
    return df

team1 = get_team_data("Team 1")

team2 = get_team_data("Team 2")

print("\n================================")
print("TEAM 1 BOWLING PERFORMANCE")
print("================================")
print(team1)

print("\n================================")
print("TEAM 2 BOWLING PERFORMANCE")
print("================================")
print(team2)