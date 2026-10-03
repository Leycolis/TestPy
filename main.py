colors = ["Red", "Blue", "Green"]


def color_list():
    print("--- Color List ---")
    print(colors)


def main():
    while True:
        print("--- Colors ---")
        print("1. View colors")
        print("2. Add color")
        print("3. Delete color")
        print("4. Search for the color")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            color_list()

        elif choice == "5":
            print("Exit")
            break


main()