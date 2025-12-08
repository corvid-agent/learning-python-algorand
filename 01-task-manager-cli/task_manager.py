import json


def main():
    """
    Main function to run the task manager CLI application.
    """

    
    print("=== Task Manager CLI ===")
    print("Welcome to the Task Manager!")


    tasks = []


    def save_tasks() ->  None:
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)


    def load_tasks() -> None:
        nonlocal tasks
        try:
            with open("tasks.json", "r") as f:
                tasks = json.load(f)
        except FileNotFoundError:
            pass


    load_tasks()


    def add_task(description: str) -> None:
        tasks.append(description)
        save_tasks()
        list_task()


    def list_task() -> None:
        for index, task in enumerate(tasks):
            print(f'{index + 1}. {task}')


    def complete_task(task_number: int) -> None:
        index = task_number - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f'Task completed: {removed}')
            save_tasks()
            list_task()
        else:
            print('Número inválido')


    while True:
        print("\n1. Add Task")
        print("\n2. List Tasks")
        print("\n3. Complete Task")
        print("\n4. Exit")


        choice = int(input('Choose an option: '))


        if choice == 1:
            description = str(input('Add task: '))
            add_task(description)
        elif choice == 2:
            list_task()
        elif choice == 3:
            number = int(input('Task number: '))
            complete_task(number)
        elif choice == 4:
            print('Cya!')
            break


if __name__ == "__main__":
    main()

