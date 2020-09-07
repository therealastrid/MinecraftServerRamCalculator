def calculateSpigot(plugins, players):
    final = 100

    final = final+(int(players)*50)+(int(plugins)*100)
    print(f'You will need {final}mb of ram')

print("Loading the minecraft calculator")
print("================================")
print('\n\n')

plugins = input("How many plugins do you plan to use? ")
players = input("How many players do you plan to have on at once? ")
calculateSpigot(plugins, players)