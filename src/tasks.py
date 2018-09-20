todo_list = []

def create_task(task):
    '''
    Add the task to the todo_list
    '''
    todo_list.append(task)

def delete_task(task):
    '''
    Remove the task from the todo_list
    '''
    todo_list.remove(task)

def mark_as_finished(task):
    if not task.endswith('finished'):
       task = task + ' finished'

def delete_all_tasks():
    # todo_list.clear()
    del todo_list[:]
