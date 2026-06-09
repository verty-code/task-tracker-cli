from tasks_service import add_task, get_all_tasks, mark_task_done, delete_task

def get_int(user_input):
    try:
        return int(user_input)
    except (ValueError, TypeError):
        return False
    
def show_no_number_error():
    print('The task number is not a number. Please enter a number')

def show_no_task_error():
    print('Such a task does not exist')
    
def work_with_input(user_input, func):
    user_input = get_int(user_input)
    if user_input is False:
        show_no_number_error()
        return False
    if (func(user_input)):
        return True
    else:
        show_no_task_error()
        return False


while True:
    print('''
Menu:
      
1. Add tasks
2. Show tasks
3. Mark task as done
4. Delete task
0. Exit
''')
    try:
        user_input = int(input("Enter the command: "))
        if user_input == 1:
            title = input("Enter a task name: ")
            add_task(title)
            print('Task added')
        elif user_input == 2:
            tasks = get_all_tasks()
            if tasks:
                print('List of tasks:')
                for id, task_name, is_done in tasks:
                    if is_done == 1:
                        print(f'{id}. {task_name} [DONE]')
                    else:
                        print(f'{id}. {task_name} [NOT DONE]')
            else:
                print("No tasks yet")
        elif user_input == 3:
            while True:
                task_id = input("Enter the number of the task you want to change: ")
                if work_with_input(task_id, mark_task_done):
                    print('Task completed')
                    break
                else:
                    is_continue = input('Do you still want to change a task? (y/Y/n/N)')
                    if is_continue == 'n' or is_continue == 'N':
                        break
        elif user_input == 4:
            while True:
                task_id = input("Enter the number of the task you want to delete: ")
                if work_with_input(task_id, delete_task):
                    print('Task deleted')
                    break
                else:
                    is_continue = input('Do you still want to delete a task? (y/Y/n/N)')
                    if is_continue == 'n' or is_continue == 'N':
                        break
                        
        elif user_input == 0:
            break
        else: 
            print("This command does not exist. Please select a valid command (a number from 0 to 4)")
    except ValueError:
        print("The command was entered incorrectly. Please select a valid command (a number from 0 to 4).")