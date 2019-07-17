import constants
import random
import sys


PLAYERS = constants.PLAYERS
TEAMS = constants.TEAMS
LENGTH = len(PLAYERS)


experienced = []
inexperienced = []
for player in PLAYERS:
    if player['experience'] == 'YES':
        experienced.append(player['name'])
    else:
        inexperienced.append(player['name'])
        
        
guardians = []
for player in PLAYERS:
    guardians.append(player['guardians'])
    
    
heights = []
for player in PLAYERS:
    heights.append(int(player['height'][:2]))
    

def display_stats():
      print("BASKETBALL TEAM STATS TOOL:\n\n"
            "---MENU---\n\n"
            "Here are your choices:\n"
            "1) Display Team Stats\n"
            "2) Quit\n")
      user_option = input("Enter an option: ")
      try:
            user_option = int(user_option)
      except ValueError as err:
            print("\nOops! Please enter either 1 or 2...\n")
            display_stats()
      else:      
            if user_option == 2:
                  print("Come back anytime! Goodbye!")
                  sys.exit()
            else:
                  print(f"1) {TEAMS[0]}\n"
                        f"2) {TEAMS[1]}\n"
                        f"3) {TEAMS[2]}\n")
            try:
                  user_option2 = int(input("Enter an option: "))
            except ValueError as err:
                  print("\nOops! Please enter 1, 2, or 3...\n")
                  display_stats()
            else:
                  if user_option2 == 1:
                        print(f"Team: '{TEAMS[0]}' Stats")
                        print("-" * 10)
                        print("Total Players: 6\n\n"
                              "Players on Team:")
                        print("Experienced: " + ", ".join(experienced[:3]))
                        print("Inexperienced: " + ", ".join(inexperienced[:3]))
                        print("\n")
                        print("Guardians:")
                        print(", ".join(guardians[:6]))
                        print("\n")
                        average_heights = int(sum(heights[:6]) / 3)
                        print("Average Height: " + f"{average_heights} inches")
                        print("\n")
                        display_stats()
                  elif user_option2 == 2:
                        print(f"Team: '{TEAMS[1]}' Stats")
                        print("-" * 10)
                        print("Total Players: 6\n\n"
                              "Players on Team:")
                        print("Experienced: " + ", ".join(experienced[3:6]))
                        print("Inexperienced: " + ", ".join(inexperienced[3:6]))
                        print("\n")
                        print("Guardians:")
                        print(", ".join(guardians[6:12]))
                        print("\n")
                        average_heights = int(sum(heights[6:12]) / 3)
                        print("Average Height: " + f"{average_heights} inches")
                        print("\n")
                        display_stats()
                  elif user_option2 == 3:
                        print(f"Team: '{TEAMS[2]}' Stats")
                        print("-" * 10)
                        print("Total Players: 6\n\n"
                              "Players on Team:")
                        print("Experienced: " + ", ".join(experienced[6:]))
                        print("Inexperienced: " + ", ".join(inexperienced[6:]))
                        print("\n")
                        print("Guardians:")
                        print(", ".join(guardians[12:]))
                        print("\n")
                        average_heights = int(sum(heights[12:]) / 3)
                        print("Average Height: " + f"{average_heights} inches")
                        print("\n")
                        display_stats()


if __name__ == '__main__':
      display_stats()
