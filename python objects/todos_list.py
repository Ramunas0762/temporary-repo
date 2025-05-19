todo_list = []

while True:

    job_todo = input("Job name: ")
    job_due = input("Due date: ")
    job_priority = input("Priority: ")

    todo = {
        "todo": job_todo,
        "due": job_due,
        "priority": job_priority
    }

    todo_list.append(todo)

    for p in todo_list:
        print(f"Job: {p['todo']}, Due: {p['due']}, Priority: {p['priority']}")
    
