#to do list 
# This is our main list where all tasks will be stored.
# Each task will be a dictionary with 'description' and 'completed' status.
print("Welcome to your To-Do List!")
tasks = []

def add_task(description):
    """Adds a new task to the list."""
    task = {
        "description": description,
        "completed": False  # New tasks are not completed by default
    }
    tasks.append(task)
    print(f"Task '{description}' added.")

def view_tasks():
    """Displays all tasks in the list, with their status."""
    if not tasks: # Checks if the list is empty
        print("No tasks in the list yet!")
        return

    print("\n--- Your To-Do List ---")
    for index, task in enumerate(tasks):
        # enumerate gives us both the index (position) and the item
        status = "✅" if task["completed"] else "⏳" # Checkmark for completed, hourglass for pending
        print(f"{index + 1}. {status} {task['description']}") # +1 because lists are 0-indexed
    print("-----------------------\n")

def mark_task_complete(task_number):
    """Marks a task as completed."""
    if 0 <= task_number - 1 < len(tasks): # Validate the task number
        tasks[task_number - 1]["completed"] = True
        print(f"Task {task_number} marked as complete.")
    else:
        print("Invalid task number. Please try again.")

def delete_task(task_number):
    """Deletes a task from the list."""
    if 0 <= task_number - 1 < len(tasks): # Validate the task number
        removed_task = tasks.pop(task_number - 1) # .pop() removes by index and returns the item
        print(f"Task '{removed_task['description']}' deleted.")
    else:
        print("Invalid task number. Please try again.")

def main_menu():
    """Displays the main menu and handles user input."""
    while True: # This loop keeps the program running until you choose to exit
        print("\n--- To-Do List Menu ---")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark task as complete")
        print("4. Delete a task")
        print("5. Exit")
        print("-----------------------")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            description = input("Enter the task description: ")
            add_task(description)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks() # Show tasks first so user knows the numbers
            try:
                task_num = int(input("Enter the number of the task to mark complete: "))
                mark_task_complete(task_num)
            except ValueError: # Handle cases where user types text instead of a number
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            view_tasks() # Show tasks first so user knows the numbers
            try:
                task_num = int(input("Enter the number of the task to delete: "))
                delete_task(task_num)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            print("Thank you for using the To-Do List!")
            break # This breaks out of the while loop, ending the program
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# This ensures that main_menu() is called when the script is executed
if __name__ == "__main__":
    main_menu()

