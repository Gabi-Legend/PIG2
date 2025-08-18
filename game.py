import random
import time

playersCount = int(input("How many players? (2-4): "))
while playersCount < 2 or playersCount > 4:
    playersCount = int(input("Choose between 2 and 4: "))

scores = [0] * playersCount

active = [True] * playersCount  

print("\nThe game has started!\n")
while sum(active) > 1:
    for i in range(playersCount):
        if not active[i]:
            continue

        print(f"\nPlayer {i+1}'s turn.")
        time.sleep(1)

        dice = random.randint(1, 6)

        if dice == 1:
            print(f"Player {i+1} rolled 1 and is OUT!")
            scores[i] = 0
            active[i] = False
        else:
            scores[i] += dice
            print(f"Rolled: {dice}, total score = {scores[i]}")

            while True:
                choice = input("Do you want to roll again? (y/n): ").lower()
                if choice == "y":
                    dice = random.randint(1, 6)
                    time.sleep(1)
                    if dice == 1:
                        print(f"Player {i+1} rolled 1 and is OUT!")
                        scores[i] = 0
                        active[i] = False
                        break
                    else:
                        scores[i] += dice
                        print(f"Rolled: {dice}, total score = {scores[i]}")
                elif choice == "n":
                    print(f"Player {i+1} stays at {scores[i]}")
                    break
                else:
                    print("Invalid choice. Type y or n.")

        if sum(active) == 1:
            break  

winner = [i+1 for i in range(playersCount) if active[i]][0]
print(f"\n🏆 Player {winner} wins with {scores[winner-1]} points! 🏆")
