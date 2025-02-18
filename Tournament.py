import random
import math


def check_square_value(n, value = 2):
    if(value < 2):
        return False
    if(value == n):
        return True
    if(value > n):
        return False
    else:
        return check_square_value(n, value * value)
def initialize_teams(n):
    # Initializes 'n' teams with random strengths.
    if math.log2(n) % 1 != 0:
        raise ValueError("Number of teams must be a power of 2.")

    teams = []
    for i in range(n):
        team = {
            "name": f"Team_{i+1}",
            "strength": random.randint(1, 100)
        }
        teams.append(team)
    
    return teams

def simulate_match(team_a, team_b):
    #  Simulates a match between two teams based on their strengths.
    chance = random.randint(1, 100)
    print(f"Math between Team: {team_a} and Team: {team_b} (chance): {chance}")
    if 40 <= chance <= 60:
        winner = team_a if team_a["strength"] < team_b["strength"] else team_b
    else:
        winner = team_a if team_a["strength"] > team_b["strength"] else team_b

    return winner

def simulate_round(team_list):
    #  Simulates a round, reducing the number of teams by half.
    winners = []
    for i in range(0, len(team_list), 2):
        winner = simulate_match(team_list[i], team_list[i+1])
        winners.append(winner)
    
    return winners

def champions_league():
    # Runs the full tournament and returns the champion.
    n = 0
    while(check_square_value(n) == False):
        n = int(input("Provide the number of trams competing in the Tournament"))
    teams = initialize_teams(n)
    print("Initial Teams:")
    for team in teams:
        print(f"{team['name']} - Strength: {team['strength']}")

    round_num = 1
    while len(teams) > 1:
        print(f"\nRound {round_num}:")
        teams = simulate_round(teams)
        for team in teams:
            print(f"Qualified: {team['name']}")
        round_num += 1

    champion = teams[0]
    print(f"\nThe champion is: {champion['name']} (Strength: {champion['strength']})")
    return champion

# Example: Run the tournament with 16 teams
champions_league()
