from menu import display_menu, display_choices
from logic import play_round

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        display_choices()
        user_input = input("Enter option (1-3): ")

        if user_input == "1":
            user_choice = "stone"
        elif user_input == "2":
            user_choice = "paper"
        elif user_input == "3":
            user_choice = "scissors"
        else:
            print("Invalid choice!")
            continue

        computer_choice, result = play_round(user_choice)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print("Result:", result)

    elif choice == "2":
        print("Thanks for playing!")
        break

    else:
        print("Invalid choice! Try again.")