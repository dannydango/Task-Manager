# Start

# Import
import datetime


# Function to register username
def reg_user():
    valid_password = False
    while not valid_password:
        user = input("What is the new username you would like to register ")

        # Check if the username already exists in the file
        with open("user.txt", "r") as file:
            for line in file:
                if user in line:
                    print("This username already exists. Please choose a different username.")
                    break
            else:
                # The username does not exist in the file, so proceed with password validation
                while not valid_password:
                    password = input("What password would you like to choose? ")
                    password2 = input("Please type your password again to confirm ")

                    if password != password2:
                        print("Your password did not match")
                        continue
                    else:
                        with open("user.txt", "a") as k:
                            k.write("\n" + user + "," + " " + password)
                            print("Username and password saved")
                        valid_password = True

                        break


# Function to add task

def add_task(username, task, task_des, due_date):
    date = str(datetime.date.today())
    with open("tasks.txt", "a") as file:
        file.write("\n" + username + "," + " " + task + "," + " "
                   + task_des + "," + " " + date + "," + " " + due_date + "," + " " + "No")


# Function to view all
def view_all():
    file1 = open('tasks.txt', 'r')
    count = 0

    while True:
        count += 1
        # Read from file and split + strip
        line = file1.readline()
        task_list = line.strip().split(", ")
        if not line:
            break
        # Print in a user-friendly fashion
        print("-" * 50 + "\n")
        print("Task:" + "\t \t \t \t" + task_list[1] + "\n" +
              "Assigned to:" + "\t \t" + task_list[0] + "\n" +
              "Date assigned:" + "\t \t" + task_list[3] + "\n" +
              "Due date:" + "\t \t \t" + task_list[4] + "\n"
                                                        "Task Complete:" + "\t \t" + task_list[5] + "\n" +
              "Task Description" + "\n" + task_list[2] + "\n".format(count, line.strip()))
        print("-" * 50)
    file1.close()


# Function to view my task
def view_mine():
    f = open("tasks.txt", "r+")
    contents = f.readlines()
    tasks_found = False  # Flag to track if any tasks were found for the user

    for value, task in enumerate(contents):
        if usernameInput in task:
            print(f"{value}. {task}")
            tasks_found = True

    if not tasks_found:
        print("No tasks were found for the specified user.")
        return  # Return control to the calling function (i.e., the menu)

    task_num = int(input("What is you task number? "))

    split_data = contents[task_num].split(", ")

    # Print a menu of options for the user
    print("What would you like to do?")
    print("1. Mark task as complete")
    print("2. Change user")
    print("3. Change due date")
    print("4. Quit")

    # Prompt the user to select an option
    option = int(input("Enter your selection: "))

    #  Change date, mark as complete or change user
    if option == 3:
        split_data[4] = input("What is the new due date you would like? (yyyy-mm-dd) ")

    elif option == 1:
        split_data[5] = "yes\n"

    elif option == 2:
        split_data[0] = input("Which user would you like to assign to this task ")

    # Quit or pick up incorrect option
    elif option == 4:
        print("Quit to menu")

    else:
        print("You typed an incorrect option, please try again")
    # Join data and rewrite to file
    join_data = ", ".join(split_data)
    contents[task_num] = join_data

    f = open("tasks.txt", "w")
    for line in contents:
        f.write(line)


# Function for task overview
def task_overview():
    # Open the tasks.txt file in read mode
    with open('tasks.txt', 'r') as f:
        # Read the contents of the file into a list
        tasks = f.readlines()

    # Initialize variables to store the number of tasks, completed tasks, and uncompleted tasks
    total_tasks = 0
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0

    # Get the current date
    now = datetime.datetime.now()
    print(now)
    # Iterate over the list of tasks
    for task in tasks:
        total_tasks += 1
        parts = task.split(',')
        # Get the due date
        due_date = parts[4].strip()
        # Check if the task is completed or not
        if 'yes' in parts[5].lower():
            completed_tasks += 1
        elif 'no' in parts[5].lower():
            # Increment the uncompleted tasks count
            uncompleted_tasks += 1
            # Check if date is overdue
            if datetime.datetime.strptime(due_date, '%Y-%m-%d') < now:
                overdue_tasks += 1

    # Calculate the percentage of tasks that are incomplete and overdue
    percent_incomplete = (uncompleted_tasks / total_tasks) * 100
    overdue_percent = (overdue_tasks / total_tasks) * 100

    # Open the task_overview.txt file in write mode
    with open('task_overview.txt', 'w') as f:
        f.write(f'Total number of tasks: {total_tasks}\n')
        f.write(f'Total number of completed tasks: {completed_tasks}\n')
        f.write(f'Total number of uncompleted tasks: {uncompleted_tasks}\n')
        f.write(f'Total number of overdue tasks: {overdue_tasks}\n')
        f.write(f'Percentage of tasks that are incomplete: {percent_incomplete:.2f}%\n')
        f.write(f'Percentage of tasks that are overdue: {overdue_percent:.2f}%\n')


# Function for user_overview
def user_overview():
    # Read in the user.txt and tasks.txt files
    with open("user.txt", "r") as f:
        user_lines = f.readlines()

    with open("tasks.txt", "r") as f:
        tasks_lines = f.readlines()

    # Get the total number of users and tasks
    total_users = len(user_lines)
    total_tasks = len(tasks_lines)

    # Create a dictionary to store the number of tasks assigned to each user
    tasks_by_user = {}

    # Iterate through the tasks and count the number of tasks for each user
    for task in tasks_lines:
        task_parts = task.split(",")
        username = task_parts[0]
        if username in tasks_by_user:
            tasks_by_user[username] += 1
        else:
            tasks_by_user[username] = 1

    # Open the user_overview.txt file for writing
    with open("user_overview.txt", "w") as f:
        # Write the total number of users and tasks to the file
        f.write("Total number of users: " + str(total_users) + "\n")
        f.write("Total number of tasks: " + str(total_tasks) + "\n\n")

        # Iterate through the users and write their overview to the file
        for user in user_lines:
            username = user.split(",")[0]
            # Get the number of tasks assigned to this user
            num_tasks = tasks_by_user[username] if username in tasks_by_user else 0
            # Calculate the percentage of tasks assigned to this user
            percent_assigned = num_tasks / total_tasks * 100
            # Write the username and number of tasks to the file
            f.write("Username: " + username + "\n")
            f.write("Total number of tasks assigned to username: " + str(num_tasks) + "\n")
            f.write("Percentage of total assigned tasks: " + str(percent_assigned) + "%\n")

            # Initialize counters for the number of complete, incomplete, and overdue tasks
            num_complete = 0
            num_incomplete = 0
            num_overdue = 0
            # Iterate through the tasks and count the number of complete, incomplete, and overdue tasks for this user
            for task in tasks_lines:
                task_parts = task.split(",")
                task_parts = [task.replace("\n", "") for task in task_parts]
                if task_parts[0] == username:
                    completion_status = task_parts[5]
                    due_date = task_parts[4].strip()
                    if completion_status.lower() == " yes":
                        num_complete += 1
                    elif completion_status.lower() == " no":
                        num_incomplete += 1
                        # Check if the task is overdue
                        if datetime.datetime.now() > datetime.datetime.strptime(due_date, "%Y-%m-%d"):
                            num_overdue += 1

            # Calculate the percentages of complete, incomplete, and overdue tasks for this user
            percent_complete = num_complete / num_tasks * 100 if num_tasks > 0 else 0
            percent_incomplete = num_incomplete / num_tasks * 100 if num_tasks > 0 else 0
            percent_overdue = num_overdue / num_tasks * 100 if num_tasks > 0 else 0
            # Write the percentages of complete, incomplete, and overdue tasks to the file
            f.write("Percentage of user assigned tasks that are complete: " + str(percent_complete) + "%\n")
            f.write("Percentage of tasks that are yet to be completed: " + str(percent_incomplete) + "%\n")
            f.write("Percentage of tasks that are yet to be completed and are overdue: " + str(percent_overdue)
                    + "%\n\n")


# Function to print user overview in terminal
def user_overview_print():
    # Open file and split data at new line
    with open('user_overview.txt', 'r') as h:
        text = h.read()
        lines = text.split('\n')
        # Print data in a User friendly way
        for line in lines:
            print(line)


# Function to print task overview in terminal
def task_overview_print():
    # Open file and split data at new line
    with open('task_overview.txt', 'r') as j:
        text = j.read()
        lines = text.split('\n')
        # Print data in a user-friendly way
        print('-' * 20)
        for line in lines:
            print(line)
        print('-' * 20)


# Function to get login details
def get_login_details():
    username = input("What is your username? ")
    password = input("What is your password? ")
    return username, password


login = False

# Read user.txt into a list
with open("user.txt", "r") as user_file:
    lines = user_file.read().split("\n")

while not login:
    # Get login details from user
    usernameInput, passwordInput = get_login_details()

    # Check against user.txt and verify user input
    for line in lines:
        username, password = line.split(",")
        username = username.strip()
        password = password.strip()
        if username == usernameInput and password == passwordInput:
            login = True
            print("your details are correct. Login was successful")
            break
    else:
        login = False
        print("Your details are incorrect, Please try again")


# Check login status is true and allow access to menu
while login is True:
    menu = input('''Select one of the following options below:
r - Register a user (Admin Only)
a - Add  a task
va - View all tasks
vm - View my task
ds - View statistics
gr - Generate reports
e - Exit
: ''').lower()
    # Pull function to register user

    if menu == 'r' and usernameInput == "admin":

        reg_user()
    # Gather user input and pull function add task
    elif menu == 'a':
        username = input("What is the username of the user you want to assign a task ")
        task = input("What is the task you want to assign ")
        task_des = input("Please leave a brief description of the task ")
        due_date = input("When will the task be due by in format yyyy-mm-dd ")

        add_task(username, task, task_des, due_date)
    # Pull function to view all
    elif menu == 'va':

        view_all()
    # Pull function to view mine and edit
    elif menu == 'vm':

        view_mine()
    # Menu to choose statistics report
    elif menu == 'ds':
        ds_menu = input('''Select one of the following options below:
        t - See task overview
        u - See user overview
        b - See task and user overview
        : ''').lower()
        # Pull function to view task overview
        if ds_menu == "t":
            task_overview_print()
        # Pull function to view user overview
        elif ds_menu == "u":
            user_overview_print()
        # Pull funtion to view both task and user overview
        elif ds_menu == "b":
            task_overview_print()
            user_overview_print()

        else:
            print("That was not an option")

    # Pull function to generate reports on user and task overview
    elif menu == 'gr':
        user_overview()
        task_overview()

    # Exit program
    elif menu == "e":
        print("Goodbye!")
        exit()

    else:
        print("You have made a wrong choice or do not have access, Please Try again")
