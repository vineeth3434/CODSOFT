#initialize an empty list to store tasks
tasks = []
def add_task(task):
    tasks.append(task)
    print("Task added:",task)

def view_tasks():
    if len(tasks) == 0:
        print("no tasks in the list")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def complete_task(task_index):
    if 1<= task_index <= len(tasks):
        completed_task = tasks.pop(task_index-1)
        print("completed task:",completed_task)
    else:
        print("Invalid task index.")
#choose the operations to perform on the list
while True:
    print("\nSelect an option :")
    print("1. Add Task")
    print("2. View Task")
    print("3. complete Task")
    print("4. Exit")

    choice = input("ENter choice (1/2/3/4):")

    if choice == '1':
        new_task=input("Enter new task :")
        add_task(new_task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        view_tasks()
        task_index =int("Enter the index of the task to complete :")
        complete_task(task_index)
    elif choice == '4':
        print("exiting the to-do list.")
        break
    else:
        print("Invalid choice.Please select a valid option.")    

            

