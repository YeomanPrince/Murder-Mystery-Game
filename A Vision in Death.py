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
    directions = [""]
    print("You walk over to a young lady. She has on a robe with her arms crossed hugging herself. You introduce yourself. 'Hi, my name is detective +name+ and I'm incharge of this investigation. Can we start with your name?")
    print("Webster, Ruby Webster. But just call me Ruby.")
    print("She says rubbing her arms in a sense of comfort, her head down looking up at you. She seems smaller with this action.")
    print("Can you tell me about what happened tonight, Ruby? You ask while thumbing the pages of your moleskin")
    print("")

def showweapon():
    pass

def showbody():
    pass


if __name__ == "__main__":
    while True:
        print("Welcome to A Vision in Death by Yeoman!")
        print("As a newly minted homicide detective, you've been called out of your bed to your first case.")
        print("Entering the scene you see a man face down in the living room, furniature strewn about looking like a struggle ensued.")
        print("An officer comes up to you and says 'You're new here... What's your name?'")
        name = input()
        print("'+name+ ... Ah! You're the new Dectective! It's a grusome one for your first case!")
        introScene()