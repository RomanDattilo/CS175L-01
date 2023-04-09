#Roman Dattilo
#CS 175L


count=0

with open('WorldSeriesWinners.txt', 'r') as file:
    for team in file:
        team=team.rstrip('\n')
        if team.lower() in team.lower():
            count +=1

search_team=''
while search_team.lower() != 'quit':
    search_team = input("Enter the name of a team or Quit: ").lower()
    if search_team != 'quit':
        count = 0
        with open('WorldSeriesWinners.txt', 'r') as file:
            for team in file:
                team=team.rstrip('\n')
                if search_team.lower() in team.lower():
                    count +=1
        print(f"{search_team} won the World Series {count} times between 1903 and 2009.")


