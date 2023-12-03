class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added to the to-do list.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks in the to-do list.')
        else:
            print('To-Do List:')
            for i, task in enumerate(self.tasks, start=1):
                print(f'{i}. {task}')

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f'Task "{removed_task}" removed from the to-do list.')
        else:
            print('Invalid task index.')

def main():
    todo_list = TodoList()

    while True:
        print('\n1. Add Task\n2. View Tasks\n3.Remove Task\n4. Exit')
        choice = input('Enter your choice (1/2/3/4): ')

        if choice == '1':
            task = input('Enter the task: ')
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_index = int(input('Enter the task index to remove: '))
            todo_list.remove_task(task_index)
        elif choice == '4':
            print('Exiting the to-do list application. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter 1, 2, 3, or 4.')

if __name__ == "__main__":
    main()
