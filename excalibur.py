def chose_excalibur():
    print("You awaken, only to be blinded by the gleaming light that shines through the thick leaves of the forest. You sit up and take a minute to study the things around you. Through the trees of the forest you see an enormous, beautiful kingdom. To the left, you can't see but hear the pleasant sound of streaming river")
    choice = input("Do you want to go to the city? y/n")
    if(choice == "y"):
        print("you go to the city")
        print("You arrive at the city gates, the walls tower over you.")
        print("???: You there! What brings you here to Bebbanburg!? You lost, boy!?")
        print("*You look around you, but can't seem to visually find the voice. It sounds like it's coming from a small hole in the gates*")
        print("\"???: Do you understand English boy?\"")
        choice1_1 = input ("Come in peace / Insult the guard")
        if (choice1_1 == "Come in peace"):
            print("You: Aye, I seek only peace and want no trouble")
            print("???: You're quite a ways away from safety boy!")
            print("???: Where are you from?")

            choice1_2 = input ("Lie / Tell the truth")
            if (choice1_2 == "Lie"):
                print("You: I'm from the kingdom of Wessex.")
                print("You: I'm ")
            if (choice1_2 == "Tell the truth"):
                print("You: I don't know sir.")
                print("You: I awoken in the forest, with no memory of whom I once was.")
                print("You: I've got no sense of who I am or where I am.")
                print("???: I see... then you really are a lost boy.")
                print("???: Let him in Leofric!")
                print("*You gaze in awe at the enormous gates movement. With every passing second, you're able to peer deeper into the beautiful kingdom*")



        if (choice1_1 == "Insult the guard"):
            print("You: Am I to be intimidated by a guard who is afraid to face his opponents directly?")
            print("???: You're willing to reinforce those words with the clash of metal then?")
            print("*You realize, you don't have a sword with you*")

            choice1_3 = input ("Bluff / Take back what you said")
            if choice1_3 == ("Bluff"):
                print()
            if choice1_3 == ("Take back what you said"):
                print()



    if (choice == "n"):
        print("You get up, and walk towards the mysterious sound in the depths of the forest")
    
  
        print("Drawn to the sound of running water, you make your way farther into the forest")
        print("You follow what seems to be a small, human made path, which eventually connects to the river you heard. You stop to appreciate the clean, clear water when you suddenly see something large moving through in your direction. Do you hide, or do you try to get a closer look?")  
        choice = input ("What do you do? try to hide / closer look")
        if (choice == "try to hide"):
            print("You dive for the nearest patch of growth that can conceal you and listen to your surroundings. Over the excited chatter of birds and the hushed sound of the wind you can faintly hear hushed voices through the dense undergrowth. After around a minute, fade out and you are left with the quiet ambience of the forest once again. Suddenly you notice the most beautiful creature that you have ever seen. You only see it for a fraction of a second, but you are immediately enchanted by it. Money,progress,time travel, none of it is as important as this creature now. You never return from the forest.")

        if (choice == "closer look"):
            print("You move towards the sounds to find what looks like a dozen hunters carrying bows marching through the forest. Cautiously, you try to signal to them without making any sudden movements. You are still unsure about whether or not they are hostile. At the sight of you, they pause, and then one of them starts shouting. Before you can react, he draws his bow and takes aim at you. Confused and scared, you run as far as you can before taking cover behind a tree. A hail of arrows fly past you. Following the arrows comes the heavy thud of footsteps as you hear the entire group charging your position.") 
            print("Realizing that you only have one way out, you quickly activate the time travel sequence on your watch.") 
            print("You hear the foosteps getting closer")
            print("2...")
            print("A second wave of arrows flies past you")
            print("1...")
            print("A large bearded man comes around the corner with an axe, swinging it directly at you")
            print("0...")
            print("You wake up in your room again, intact. You are dissapointed that your experience ended so soon, but it could have been worse")

