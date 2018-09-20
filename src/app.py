from tasks import todo_list, create_task, mark_as_finished, delete_all_tasks, delete_task
from accounts import accounts, add_account, login


if __name__ == "__main__":
    name = input("Enter your name: ")
    password = input("Enter password:")

    if not login(name, password):
        add_account(name, password)

    print("Select Option:")
    print("1. Create Task")
    print("2. deleting a task")
    print("3. deleting all tasks")
    print("4. Marking a task finished")

    selection = input("selection: ")


    if selection == 1:
        task = input("Enter task to create")
        create_task(task)

    elif selection == 2:
        task = input("Enter task to delete")
        delete_task(task)

    elif selection == 3:
        delete_all_tasks()

    elif selection == 4:
        task = input("Enter finished task")
        mark_as_finished(task)