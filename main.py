print("Welcome to the game!!")
name = input("What is your name? ")
age = int(input("What is your age? "))
health = 10

if age >= 18:
    print(f"Hello {name}. You are old enough to play!")

    wants_to_play = input("Do you want to play (yes/no)? : ").lower()
    if wants_to_play == "yes":
        print("Let's play!!")
        print(f"You are starting with {health} health.")

        left_or_right = input("First choice... Left or Right (left/right)? : ").lower()
        if left_or_right == "left":
            peng = input("You meet a peng ting along a path. Do you approach her or ignore her (approach/ignore)? : ").lower()
            if peng == "approach":
                print("A courageous clown is a good clown. You got her number and 10 more gansta points.")

                ans = input("You follow the path and reach a lake. Do you swim across or go around (across/around)? : ").lower()
                if ans == "around":
                    print("You went around and reached the other side of the lake.")
                elif ans == "across":
                    print("You managed to get across but were bit by a fish and lost 5 health.")
                    health -= 5

                ans = input("You notice a house and a river. Which do you go to (house/river)? : ").lower()
                if ans == "house":
                    print(
                        "You go to the house and are greeted by its owner. He doesn't like you and you lose 5 health.")
                    health -= 5
                    if health <= 0:
                        print("You now have 0 health and you lost the game.")
                    else:
                        print("You have survived. You win!")
                else:
                    print("You fell in the river and lost.")

            elif peng == "ignore":
                print("Wyd bro?? You lost the game.")

        else:
            print("You fell down and lost...")
    else:
        print("Cya...")
else:
    print("Sorry, you are too young to play!")