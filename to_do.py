# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print("Task added: {}".format(task))

# Function to display all tasks in the list
def show_tasks():
    print("Tasks:")
    for index, task in enumerate(tasks, start=1):
        print("{}. {}".format(index, task))
#Function to Mark the completed tasks as done
def mark_done(t):
    del tasks[t-1]
    print("task {} is marked as done.".format(t))

# Main program loop
while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. Show Tasks")
    print ("3.Mark completed task as done!")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)

    elif choice == "2":
        show_tasks()
        
    elif choice == "3":
        t = int(input("Enter the task number: "))
        mark_done(t)
        
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")