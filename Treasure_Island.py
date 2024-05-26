print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

level1= input('you are at a crossroad. where do you want to go? Type "left" or "right:').lower()
if level1 == "left":
  level2= input('you have to cross a river. type do you want to "swim" or "wait"').lower()
  if level2 == "wait":
    level3 = input('you have to choose a door. type which door you want to select "Red" or "Blue" or "Yellow"').lower()
    if level3 == "Red":
      print("Burned by fire. Game Over")
    elif level3 == "Blue":
      print("Eaten by Blasten Game Over")
    elif :
      print("You Win")
  else:
    print("Attacked by trout Game Over")
else:
  print("Fall into a hole Game Over")