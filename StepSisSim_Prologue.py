yes = "yes" or "Yes"
no = "no" or "No"
defend = "defend" or "Defend"
kick = "kick" or "Kick"
punch = "punch" or "Punch"
read = "read" or "Read"
accept = "accept" or "Accept"
decline = "decline" or "Decline"

print("alright, looks like you found something that you're not supposed to.")
print("how about you turn back and leave? ")
response = str(input())
if response == yes:
    print("Thank you.")
    sdf = input("Press any key to exit the program.")
if response == no:
    print("well, it's your choice. looks like we'll have to do this the hard way.")
    print("Guys, we've got company!")
    # At this point, you'll enter a "fighting" game. You can kick, punch or defend.
    print("""Instructions:
    You can kick, punch and defend""")
    round1 = str(input("You can kick, punch and defend. What do you choose?"))
    if round1 == defend:
        print("pussy")
        sdf = input("Press any key to pussy out.")
    if round1 == punch:
        print("You punched the creator, dealing 15 damage into him!")
        print("The creator defended! In the next round, you will deal less damage into him!")
        round2 = str(input("You can kick, punch and defend. What do you choose?"))
        if round2 == defend:
            print("You defended!")
            print("The creator... He's... He's not a human...")
            print("The creator ran towards you. When he touched you, you became dust.")
            print("You died.")
            sdf = str(input("Press any key to exit."))
        if round2 == kick:
            print("You kicked the creator, dealing him 9̶9̶9̶ damage!")
            print("The creator... He's... He's not a human...")
            print('Creator: "Run, while you can!"  ')
            print("You pussied out.")
            sdf = str(input("Press any key to exit."))
        if round2 == punch:
            print("You gathered all of your strength, and punched the creator so hard he died from it!")
            print("You won!")
            passit = str(input("Type 'Read' to read the conversation."))
            if passit == read:
                print("I- I don't even know what to say-")
                print("You're powerful.")
                print("Powerful enough to restart the development of Step Sister Simulator.")
                print("So, what do you say? Do you accept it?")
                rstrt = str(input("Accept or decline? "))
                if rstrt == decline:
                    print("A developer punched you in the balls, dealing 999 damage!")
                    print("You died.")
                    sdf = str(input("Press any key to exit."))
                if rstrt == accept:
                    print("Thank you. You saved us all...")
                    sdf = str(input("Press any key to exit."))
    if round1 == kick:
        print("You kicked the creator, dealing 25 damage into him!")
        print("The creator punched you in the nuts, dealing 50 damage into you!")
        round2_kick = str(input("You can kick, punch and defend. What do you choose?"))
        if round2_kick == defend:
            print("You defended!")
            print("The creator hit you, but you dodged him!")
            print("The creator ran into the wall, and he got damaged! He lost 30 HP.")
            round3_defend = str(input("You can kick, or punch."))
            if round3_defend == punch:
                print("You punched the creator, dealing him 15 damage!")
                print("The creator bit your leg! (for some unknown reason)")
                print("You started punching the creator's head, killing him in action!")
                print("You won!")
                passit = str(input("Type 'Read' to read the conversation"))
                if passit == read:
                    print("I- I don't even know what to say-")
                    print("You're powerful.")
                    print("Powerful enough to restart the development of Step Sister Simulator.")
                    print("So, what do you say? Do you accept it?")
                    rstrt = str(input("Accept or decline"))
                    if rstrt == decline:
                        print("A developer punched you in the balls, dealing 999 damage!")
                        print("You died.")
                        sdf = str(input("Press any key to exit."))
                    if rstrt == accept:
                        print("Thank you. You saved us all...")
                        sdf = str(input("Press any key to exit."))
            if round3_defend == kick:
                print("You tried kicked the creator, but he grabbed your leg and threw you to the wall!")
                print("The creator kicked you!")
                print("You died.")
                sdf = str(input("Press any key to exit."))
        if round2_kick == punch:
            print("You punched the creator in the balls, dealing 70 damage into him!")
            print("The creator bit your neck, killing you in the action!")
            print("You died.")
            sdf = str(input("Press any key to exit."))
        if round2_kick == kick:
            print("You kicked the creator, dealing 50 damage into him!")
            print("The creator kicked you so hard, that you fell onto the floor.")
            print("You died.")
            sdf = str(input("Press any key to exit."))
