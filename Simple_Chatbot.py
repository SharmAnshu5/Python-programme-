def print_response(response):
    print(response)

def main():
    print("Welcome to the Simple Question and Answering Program!")
    print("=====================================")
    print("You may ask any one of these questions:")
    print("Hi")
    print("How are you?")
    print("Are you working?")
    print("What is your name?")
    print("What did you do yesterday?")
    print("Quit")

    while True:
        question = input("Enter one question from above list: ").lower()
        if question in ['hi']:
            print_response("Hello")
        elif question in ['how are you?', 'how do you do?']:
            print_response("I am fine")
        elif question in ['are you working?', 'are you doing any job?']:
            print_response("yes. I'am working in KLU")
        elif question in ['what is your name?']:
            print_response("My name is Emilia")
            name = input("Enter your name? ")
            print_response("Nice name and Nice meeting you, " + name)
        elif question in ['what did you do yesterday?']:
            print_response("I saw Bahubali 5 times")
        elif question in ['quit']:
            print_response("Goodbye!")
            break
        else:
            print_response("I don't understand what you said. Please try again!")

if __name__ == "__main__":
    main()