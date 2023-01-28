
todo_list = []


def add_todo():
    todo_list.append(input("What to do: "))
    return

def mark_todo():
    if not todo_list:
        print("No task to remove")
        return

    done = todo_list.pop()
    print("Congrats on ", done)
    return

def print_todo():
    if not todo_list: print("You have done all the tasks")
    for todo in todo_list:
            print(todo)

def select_op(choice):
    if (choice == '#'): return -1

    if choice == '+': add_todo()
    elif choice == '-': mark_todo()
    elif choice == '?': print_todo()

    return 0

while True:
    print("+ Add to ToDo")
    print("? View List")
    print("- Done")
    print("# Terminate")

    # take input from the user
    choice = input("Enter choice (+ - ? #): ")
    print(choice)
    if(select_op(choice) == -1):
        #program ends here
        print("Done. Terminating")
        exit()
