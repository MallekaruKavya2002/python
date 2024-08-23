class ToDoList:
    def __init__(self):
        self.tasks = {}

    def display_tasks(self):
        for task, status in self.tasks.items():
            print(f"{task}: {status}")

    def add_task(self, task):
        self.tasks[task] = "Not Started"
        print(f"Task '{task}' added.")

    def update_task(self, task, status):
        if task in self.tasks:
            self.tasks[task] = status
            print(f"Task '{task}' updated.")
        else:
            print(f"Task '{task}' not found.")

    def delete_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
            print(f"Task '{task}' deleted.")
        else:
            print(f"Task '{task}' not found.")


def main():
    todo = ToDoList()

    while True:
        print("\n1. Display Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            todo.display_tasks()
        elif choice == "2":
            task = input("Enter task name: ")
            todo.add_task(task)
        elif choice == "3":
            task = input("Enter task name: ")
            status = input("Enter new status: ")
            todo.update_task(task, status)
        elif choice == "4":
            task = input("Enter task name: ")
            todo.delete_task(task)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()

