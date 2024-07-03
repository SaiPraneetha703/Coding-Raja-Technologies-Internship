import json
import os
from datetime import datetime

TASKS_FILE = 'tasks.json'

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Loads tasks from a JSON file if it exists."""
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as file:
                self.tasks = json.load(file)

    def save_tasks(self):
        """Saves the current list of tasks to a JSON file."""
        with open(TASKS_FILE, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, description, priority, due_date):
        """Adds a new task to the list."""
        task = {
            'description': description,
            'priority': priority,
            'due_date': due_date,
            'completed': False
        }
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task_id):
        """Removes a task from the list by its ID (index)."""
        if 0 <= task_id < len(self.tasks):
            del self.tasks[task_id]
            self.save_tasks()
        else:
            print("Invalid task ID")

    def mark_task_completed(self, task_id):
        """Marks a task as completed by its ID (index)."""
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id]['completed'] = True
            self.save_tasks()
        else:
            print("Invalid task ID")

    def list_tasks(self):
        """Lists all tasks with their details."""
        for i, task in enumerate(self.tasks):
            status = "Completed" if task['completed'] else "Not Completed"
            print(f"ID: {i} | Description: {task['description']} | Priority: {task['priority']} | Due Date: {task['due_date']} | Status: {status}")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter task priority (high, medium, low): ").lower()
            if priority not in ['high', 'medium', 'low']:
                print("Invalid priority. Please enter high, medium, or low.")
                continue
            due_date = input("Enter due date (YYYY-MM-DD): ")
            try:
                datetime.strptime(due_date, '%Y-%m-%d')
                todo_list.add_task(description, priority, due_date)
                print("Task added.")
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        
        elif choice == '2':
            try:
                task_id = int(input("Enter task ID to remove: "))
                todo_list.remove_task(task_id)
                print("Task removed.")
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                todo_list.mark_task_completed(task_id)
                print("Task marked as completed.")
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        
        elif choice == '4':
            todo_list.list_tasks()
        
        elif choice == '5':
            break
        
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
