import os

TODO_FILE = "todos.txt"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    return []

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        for todo in todos:
            f.write(f"{todo}\n")

def show_todos(todos):
    if not todos:
        print("No todos yet!")
    else:
        for i, todo in enumerate(todos, 1):
            print(f"{i}. {todo}")

def add_todo(todos, new_todo):
    todos.append(new_todo)
    print(f"Added: {new_todo}")

def remove_todo(todos, index):
    if 1 <= index <= len(todos):
        removed = todos.pop(index - 1)
        print(f"Removed: {removed}")
    else:
        print("Invalid todo number!")

def main():
    todos = load_todos()
    
    while True:
        print("\n--- Todo List ---")
        print("1. Show todos")
        print("2. Add todo")
        print("3. Remove todo")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            show_todos(todos)
        elif choice == "2":
            new_todo = input("Enter new todo: ")
            add_todo(todos, new_todo)
        elif choice == "3":
            show_todos(todos)
            index = int(input("Enter the number of the todo to remove: "))
            remove_todo(todos, index)
        elif choice == "4":
            save_todos(todos)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    