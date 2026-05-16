import json

def add_task(tasks):
  title = ""
  while title == "":
    title = input("Give me the title of the task: ")

  priority = ""
  while priority not in ["High", "Medium", "Low"]:
    priority = input("Give me the priority (High/Medium/Low): ")
  
  status = ""
  while status not in ["Pending", "Completed"]:
    status = input("Give me the status (Pending/Completed): ")

  tasks.append({
    "title": title,
    "priority": priority,
    "status": status
  })

def view_tasks(tasks):
  if len(tasks) != 0:
    print(f"{"-"*10} Tasks {"-"*10}")
    index = 0
    for task in tasks:
      index += 1
      print(f"Task {index}:")
      for key, value in task.items():
        print(f"{key}: {value}")
      print(f"{"-"*27}")
  else:
    print("Currently, there are no tasks to view.")

def mark_done(tasks):
  title = input("Give me the title of the task you want to change its status to 'Completed': ")
  for task in tasks:
    if title == task["title"]:
      if task["status"] != "Completed":
        task["status"] = "Completed"
        print(f"The status of the task '{task["title"]}' has been set to 'Completed'.")
      else:
        print(f"The status of the task '{task["title"]}' is already set as 'Completed'.")
      break
  else:
    print("Not Found!")

def get_high_priority_tasks(tasks):
  high_priority_tasks = [task for task in tasks if task["priority"] == "High"]
  return high_priority_tasks

def sort_tasks_by_title(tasks):
  sorted_tasks = sorted(tasks, key=lambda x: x['title'])
  return sorted_tasks

def save_JSON_file(tasks):
  with open("tasks.json", "w") as f:
    json.dump(tasks, f, indent=2)

def read_JSON_file():
  try:
    with open('tasks.json', 'r') as f:
      tasks = json.load(f)
  except FileNotFoundError:
    tasks = []
  return tasks

def main():
  print("Welcome to the CLI Data Cruncher!")
  while True:
    print("Options:")
    print("1 - View current tasks")
    print("2 - Add a new task")
    print("3 - Mark a task as 'completed'")
    print("4 - View sorted tasks by title")
    print("5 - View high priority tasks")
    print("6 - Exit")

    while True:
      try:
          option = int(input("Please, enter an option (1-6): "))
          if option not in [1, 2, 3, 4, 5, 6]:
            print("The option you have entered is not within 1-6!")
          else:
            break
      except ValueError:
          print("Invalid input!")

    tasks = read_JSON_file()

    if option == 1:
      view_tasks(tasks)
    elif option == 2:
      add_task(tasks)
    elif option == 3:
      mark_done(tasks)
    elif option == 4:
      sorted_tasks = sort_tasks_by_title(tasks)
      view_tasks(sorted_tasks)
    elif option == 5:
      high_priority_tasks = get_high_priority_tasks(tasks)
      view_tasks(high_priority_tasks)
    else:
      break
    
    save_JSON_file(tasks)

if __name__ == '__main__':
  main()