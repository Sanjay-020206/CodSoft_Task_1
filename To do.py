class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __repr__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        description = input("Enter task description: ")
        new_task = Task(description)
        self.tasks.append(new_task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for index, task in enumerate(self.tasks, 1):
                print(f"{index}. {task}")

    def update_task(self):
        self.view_tasks()
        task_number = int(input("Enter the task number to update: ")) - 1
        if 0 <= task_number < len(self.tasks):
            new_description = input("Enter new task description: ")
            self.tasks[task_number].description = new_description
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    def complete_task(self):
        self.view_tasks()
        task_number = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number].completed = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    def delete_task(self):
        self.view_tasks()
        task_number = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_number < len(self.tasks):
            del self.tasks[task_number]
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            todo_list.add_task()
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.update_task()
        elif choice == '4':
            todo_list.complete_task()
        elif choice == '5':
            todo_list.delete_task()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
