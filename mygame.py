print("Welcome to my adventure game. I hope you have fun")
name = input("What is your name? ")
age = int(input("what is ur age? "))
print("Hello", name)
if age >= 18:
    print("You are old enough to play!")
    wants_to_play = input("Do you want to play?(y/n) ").lower()
    health=20
    print("Your health is ", health)
    if wants_to_play == "y":
        print("You are the ruler of Yorkshire.")
        print("You were kidnapped and held captive in an old castle by bandits")
        print("The exit in the basement just opened.")
        print("Which direction would you like to go?")
        first_step = input("Outside and exit the castle or walk up the stairs (exit/stairs) ")

        if first_step == "stairs":
            print("You are now on the ground floor of the building")
            print("On the ground floor there are two weapons a  sword and a  club.")
            choose_weapon = input("Choose one (sword/club): ")
            if choose_weapon == "sword" :
                print("You chose a sword")
                print("Nice Choice")
                print("A stray cat comes from nowhere and tries to bite you. What will you do?")
                option0 = input("Cut it into half or run away (cut/run) ")
                if option0 == "cut":
                    print("When you try to cut it into half it bites you and you loose 5 health but you manage to kill it")
                    health-=5
                    print("Your health is : ", health)
                    print("You observe an old box in the corner of the room")
                    open_box = input("Will you open the box or leave it and walkup upstairs?(open/leave) ")
                    if open_box == "open":
                        print("When you open the box you find an old jetpack in the box and wear it")
                        print("You walk towards the window and crack it open using ur weapon")
                        print("After breaking the window you jump out and fly away to your people")
                        print("Yaay you won the game")
                        print("You won with ", health, "health")
                    else :
                        print("You choose to leave and walk up the stairs to the first floor")
                        print("The first floor is rigged with traps and you trigger one of them")
                        print("Arrows come from the walls and they stab you and you die")
                        health-=20
                        print("Your health is ", health)
                        print("You died")
                        print("Game over")
                else :
                    print("You try to run away and there is no place to run to the stray cat bites you and kills you")
                    health-=20
                    print("Your health is ", health)
                    print("You died")
                    print("Game over")
            else :
                print("You chose a club")
                print("Nice choice")
                print("A stray cat comes from nowhere and tries to bite you. What will you do?")
                option1 = input("Beat it up or run away(beat/run) ")

                if option1 == "beat":
                    print("You beat it up with a club on its head and it dies on the spot retaining all your health")
                    print("Your health is ", health)
                    print("You observe an old box in the corner of the room")
                    open_box = input("Will you open the box or leave it and walkup upstairs?(open/leave) ")
                    if open_box == "open":
                        print("When you open the box you find an old jetpack in the box and wear it")
                        print("You walk towards the window and crack it open using ur weapon")
                        print("After breaking the window you jump out and fly away to your people")
                        print("Yaay you won the game with ", health ,"health")
                        
                    else :
                        print("You choose to leave and walk up the stairs to the first floor")
                        print("The first floor is rigged with traps and you trigger one of them")
                        print("Arrows come from the walls and they stab you and you die")
                        health-=20
                else:
                    print("You try running a away and the cat catches up with you.")
                    print("It bites you and you die on the spot")
                    health-=20
                    
                 
        else :
            print("You were bitten by the poisonous dogs outside your building and died immediately")
            health -= 20
            print("Your health is ",health)
            print("Game over!!")
    else:
        print("Too bad I hope you'll play next time")
else:
    print("You are not old enough to play")
