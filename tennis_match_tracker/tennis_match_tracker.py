print("Tennis Match Tracker")

player1 = input("Enter Player 1 name: ")
player2 = input("Enter Player 2 name: ")

player1_games = 0
player2_games = 0

print()
print("Enter the winner of each game.")
print("Type 1 for", player1, "or 2 for", player2)
print("First player to 6 games wins the set.")
print()

while player1_games < 6 and player2_games < 6:
    print("Score:", player1, player1_games, "-", player2_games, player2)
    winner = input("Who won the game? ")

    if winner == "1":
        player1_games += 1
    elif winner == "2":
        player2_games += 1
    else:
        print("Please enter 1 or 2.")

print()
print("Final Score:", player1, player1_games, "-", player2_games, player2)

if player1_games > player2_games:
    print(player1, "wins the set!")
else:
    print(player2, "wins the set!")
