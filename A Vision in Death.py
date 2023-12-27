def introScene():
    directions = ["Get statements", "Look at the body", "Search for evidence"]
    print("Everything you've learned has come to this. You know there are three things you needs to check; the room for evidence, check the body, and get statements from the witness. Which one will you choose first?")
    userInput = ()
    while userInput not in directions:
        print("Options: Get statements/Look at the body/Search for evidence")
        userInput = input()
        if userInput == "Get statements":
            showlady()
        elif userInput == "Look at the body":
            showbody()
        elif userInput == "Search for evidence":
            showweapon()
        else:
            print("Please enter a valid option to proceed.") 


def showlady():
    directions = ["Ask albi", "Go back"]
    print("You walk over to a young lady. She has on a robe with her arms crossed hugging herself. You introduce yourself. 'Hi, my name is detective +name+ and I'm incharge of this investigation. Can we start with your name?")
    print("Webster, Ruby Webster. But just call me Ruby.")
    print("She says rubbing her arms in a sense of comfort, her head down looking up at you. She seems smaller with this action.")
    print("Can you tell me about what happened tonight, Ruby? You ask while thumbing the pages of your moleskin")
    print("I went out with my friend for drinks. And then I came back...")
    print("She chokes out a sob. You give her your hankerchief, she thanks you as she dabs her eyes.")
    # not finished dialogue and make options for interogation
    userInput = input()
    while userInput not in directions:
        print("Options: Ask alibi or Go back")
    if userInput == "Ask Alibi":
        Askalibi()

    elif userInput == "Go back":
        goback()

    else:
        print("Please enter valid option to proceed")    

        def goback():
            pass    

        def Askalibi():
            pass
    

def showweapon():
    directions = ["Check knife", "Check revolver", "Go back"]
    print("You look around the room, checking each corner and crevice.")
    userInput = ""
    while userInput not in directions:
        userInput = input()
        print("Options: Check knife, Check revolver, Go back")


def showbody():
    print("You step up to the body and see that it appears to be a male in his early thirties.")
    print("Upon your intial scan of the body you see a wound in the center of his forehead")
    print("His face had a shocked expression to him as dried blood trailed and caked the side of his face.")
    print("You check the rest of his body and you see that his body has bruises on his bare chest,")
    print("and 'BASTARD' written on his stomach with a red substance.")
    print("You felt a little sick looking at the sight...")
    userInput = ""
    while userInput not in directions:
        userInput = input()
        print("Options: Talk to M.E, Check red substance, Go back")
        if userInput =="Talk to M.E":
            ME()

        elif userInput == "Check red substance":
            RedSub()

        elif userInput == "Go back":
            Back()    

        else:
            print("Please enter vailid option to proceed.")  
        
 def ME():
    pass


def RedSub():
    pass

def Back():
    pass
   


if __name__ == "__main__":
    while True:
        print("Welcome to A Vision in Death by Yeoman!")
        print("As a newly minted homicide detective, you've been called out of your bed to your first case.")
        print("Entering the scene you see a man face down in the living room, furniature strewn about looking like a struggle ensued.")
        print("An officer comes up to you and says 'You're new here... What's your name?'")
        name = input()
        print(f"{name .capitalize} ... Ah! You're the new Dectective! It's a grusome one for your first case!")
        introScene()