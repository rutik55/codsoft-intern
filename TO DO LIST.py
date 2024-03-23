class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"Description: {self.description}\nDue Date: {self.due_date}\nStatus: {status}\n"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("="*50)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task removed successfully.")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if self.tasks:
            for i, task in enumerate(self.tasks, 1):
                print(f"Task {i}:")
                print(task)
                print("=" * 50)

        else:
            print("No tasks in the to-do list.")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")
def main():
    todo_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task = Task(description, due_date)
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.display_tasks()
            index = int(input("Enter task index to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            todo_list.display_tasks()
            index = int(input("Enter task index to mark as completed: ")) - 1
            todo_list.mark_completed(index)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
