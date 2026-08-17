from app.agent import process_question

# from app.llm import ask_llm



def start_chat():

    print("===================================")
    print("   Nagendra AI Research Assistant")
    print("===================================")

    while True:

        question = input("\nYou: ")

        if question.lower() == "exit":
            print("\nGoodbye! 👋")
            break

        answer = process_question(question)
        # answer = ask_llm(question)

        print("\nAI:")
        print(answer)