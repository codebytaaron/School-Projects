tasks = []
subjects = []
priorities = []
completed = []


def show_menu():
    print()
    print("STUDY PLANNER")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task complete")
    print("4. View unfinished tasks")
    print("5. View tasks by subject")
    print("6. Show progress")
    print("7. Remove a task")
    print("8. Exit")


def add_task():
    task = input("Enter the assignment or task: ")
    subject = input("Enter the subject: ")
    priority = input("Priority (High, Medium, Low): ")

    tasks.append(task)
    subjects.append(subject)
    priorities.append(priority)
    completed.append(False)

    print("Task added!")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks added yet.")
    else:
        print()
        print("ALL TASKS")

        for i in range(len(tasks)):
            status = "Done" if completed[i] else "Not Done"

            print(
                str(i + 1) + ".",
                tasks[i],
                "| Subject:", subjects[i],
                "| Priority:", priorities[i],
                "|", status
            )


def mark_complete():
    view_tasks()

    if len(tasks) > 0:
        number = int(input("Enter task number to mark complete: "))

        if number >= 1 and number <= len(tasks):
            completed[number - 1] = True
            print("Task marked complete!")
        else:
            print("Invalid task number.")


def unfinished_tasks():
    print()
    print("UNFINISHED TASKS")

    found = False

    for i in range(len(tasks)):
        if completed[i] == False:
            print(
                str(i + 1) + ".",
                tasks[i],
                "|", subjects[i],
                "|", priorities[i]
            )
            found = True

    if found == False:
        print("You have no unfinished tasks!")


def tasks_by_subject():
    subject = input("Enter a subject: ")
    found = False

    print()
    print("TASKS FOR", subject.upper())

    for i in range(len(tasks)):
        if subjects[i].lower() == subject.lower():
            status = "Done" if completed[i] else "Not Done"

            print(
                tasks[i],
                "| Priority:", priorities[i],
                "|", status
            )

            found = True

    if found == False:
        print("No tasks found for that subject.")


def show_progress():
    if len(tasks) == 0:
        print("No tasks added yet.")
        return

    done = 0

    for status in completed:
        if status == True:
            done += 1

    percent = done / len(tasks) * 100

    print()
    print("Tasks completed:", done)
    print("Total tasks:", len(tasks))
    print("Progress:", round(percent, 1), "%")

    if percent == 100:
        print("Everything is finished!")
    elif percent >= 75:
        print("Almost done!")
    elif percent >= 50:
        print("More than halfway there!")
    else:
        print("Keep working!")


def remove_task():
    view_tasks()

    if len(tasks) > 0:
        number = int(input("Enter task number to remove: "))

        if number >= 1 and number <= len(tasks):
            index = number - 1

            removed_task = tasks[index]

            tasks.pop(index)
            subjects.pop(index)
            priorities.pop(index)
            completed.pop(index)

            print(removed_task, "was removed.")
        else:
            print("Invalid task number.")


print("Welcome to the Study Planner!")

running = True

while running:
    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        mark_complete()

    elif choice == "4":
        unfinished_tasks()

    elif choice == "5":
        tasks_by_subject()

    elif choice == "6":
        show_progress()

    elif choice == "7":
        remove_task()

    elif choice == "8":
        running = False
        print("Good luck with your work!")

    else:
        print("Please enter a number from 1 to 8.")
