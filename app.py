#  Imported libraries/files
import constants
import sys
from copy import deepcopy


# Global variables
players = deepcopy(constants.PLAYERS)
teams = deepcopy(constants.TEAMS)
experienced = []
inexperienced = []
heights = []
guardians = []
panthers = []
bandits = []
warriors = [] 
 

#  Creates function to clean the data copied from 'constants.py'
def clean_data():
      #  For each player, convert the string value of 'experience' to boolean value 
      #  and add to new list (experienced / inexperienced)
      for player in players:
            #  If the exprience value is 'YES', convert to True
            if player['experience'] == 'YES':
                  player['experience'] = True
                  #  Add to experienced player's list
                  experienced.append(player)
            #  If the exprience value is 'NO', convert to False
            else:
                  player['experience'] = False
                  #  Add to inexperienced player's list
                  inexperienced.append(player)
                  
      #  For each player, convert the string value of 'height' to integer
      for player in players:
            #  Slice the string value to only gather numbers
            player['height'] = player['height'][:2]
            #  Convert the string value to integer
            player['height'] = int(player['height'])
            heights.append(player['height'])
            
      # Extend 'guardians' list of strings.     
      for player in players:
            # Remove the ' and ' between the names
            player['guardians'] = player['guardians'].split(" and ") 
            # Store each guardian in a list together for that player 
            guardians.extend(player['guardians'])
            

#  Creates function to assign players and 
#  evenly balance experienced/inexperienced among teams            
def create_teams(exp, inexp):
      panthers.append(exp[:3] + inexp[:3])
      bandits.append(exp[3:6] + inexp[3:6])
      warriors.append(exp[6:] + inexp[6:])


#  Creates a function to display the user selected team
def display_team(team):
      teamplayers = []
      teamexp = []
      teaminexp = []
      teamguardians = []
      i = 0
      while i < len(team):
            for player in team[i]:
                  if player['experience'] == True:
                        teamplayers.append(player['name'])
                        teamexp.append(player['name'])
                  else:
                        teamplayers.append(player['name'])
                        teaminexp.append(player['name'])
            i += 1
            
      i = 0
      while i < len(team):
            for player in team[i]:
                  teamguardians.extend(player['guardians'])
            i += 1
            
      #  (sum of team height in inches / num of players)
      sum = 0
      i = 0
      while i < len(team):
            for player in team[i]:
                  sum += int(player['height'])
            i += 1
      average = int(sum / 6)
            
      #  Clean display
      print("-" * 10)
      print("Total Players: 6")
      print(f"Experienced Players: {len(teamexp)}")
      print(f"InExperienced Players: {len(teaminexp)}")
      print(f"Average Team Height: {average} inches\n")  
      
      print("Players on Team:")
      print(", ".join(teamplayers))
      print("\n")
      
      print("Guardians: ")
      print(", ".join(teamguardians))
      print("\n")


#  Creates a function to prompt the user and display stats
def display_stats():
      #  Display main menu
      print("BASKETBALL TEAM STATS TOOL:\n\n"
            "---MENU---\n\n"
            "Here are your choices:\n"
            "1) Display Team Stats\n"
            "2) Quit\n")
      
      #  Prompt the user to enter an option (1/2)
      try:
            user_option = input("Enter an option: ")
      #  Catch potential input error
      except EOFError as err:
            pass
      else:      
            valid_options1 = ["1", "2"]
            while user_option not in valid_options1:
                  user_option = input("Please enter a 1 or 2 ")
            #  If the user elects to quit, exit program
            if user_option == "2":
                  print("Come back anytime! Goodbye!")
                  sys.exit()
            #  Otherwise, display team names
            while user_option != "2":
                  print(f"1) {teams[0]}\n"
                        f"2) {teams[1]}\n"
                        f"3) {teams[2]}\n")
                  valid_options2 = ["1", "2", "3"]
                  user_option2 = input("Enter an option: ")
                  while user_option2 not in valid_options2:
                        user_option2 = input("Please enter a 1, 2, or 3 ")
                  #  If user selects 1, display team[0] "Panthers" stats
                  if user_option2 == "1":
                        print(f"Team: {teams[0]} Stats")
                        display_team(panthers)
                        display_stats()
                  #  If user selects 2, display team[1] "Bandits" stats
                  elif user_option2 == "2":
                        print(f"Team: {teams[1]} Stats")
                        display_team(bandits)
                        display_stats()
                  #  If user selects 3, display team[2] "Warriors" stats
                  elif user_option2 == "3":
                        print(f"Team: {teams[2]} Stats")
                        display_team(warriors)
                        display_stats()

# Proper use of dunder __main__ ? :)
if __name__ == '__main__':
      #  Cleans the data copied from 'constants.py'
      clean_data()
      #  Creates 3 equally balanced teams
      create_teams(experienced, inexperienced)
      #  Start program
      display_stats()
