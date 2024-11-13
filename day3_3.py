print("Welcome To Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You are at a crossroad, where do you want to go? Type "left" or "right" : ').lower()

if choice1 == "left" :
    choice2 = input('You have come to a lake, there is an island at the middle of the lake.Type "wait" for a boat.Type "swim" to swim across : ').lower()

    if choice2 == "wait" :
         choice3 = input("You arrived at the island unharmed. There is house with 3 doors , red,yellow and blue.Which color do you choose? ").lower()

         if choice3 == "red":
             print("It is a room full of fire.Game Over.")
         elif choice3 == "blue":
             print("You entered a room of beasts.Game Over.")
         elif choice3 == "yellow" :
             print("You found the treasure.You Win!")
         else :
             print("You choose a door that doen't exist.Game Over.")

    else:
        print("You got attacked by angry tout.Game Over.")
             
else :
    print("You fall in to a hole.Game Over.")