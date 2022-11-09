import datetime

# date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
# date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
# print(f"That day is/was {date.strftime('%A')}")
# print(date.strftime("%d/%m/%Y"))
from project import Project

menu = """Menu:
(L)oad projects  
(S)ave projects  
(D)isplay projects  
(F)ilter projects by date
(A)dd new project  
(U)pdate project
(Q)uit"""


def main():
    file_name = "project.txt"
    projects = []
    projects = read_in_file(file_name, projects)

    print(f"{menu}\n")
    choice = input("Enter menu option: ").upper()
    while choice != "Q":
        if choice == "L":
            # Load projects
            new_file_name = input("Enter File Name: ")
            read_in_file(new_file_name, projects)

        elif choice == "S":
            # Save projects
            out_file = input("Enter Out file name: ")
            with open(out_file, "w") as out_file:
                print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
                for project in projects:
                    print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}",file=out_file)

        elif choice == "D":
            # Display Projects
            for project in projects:
                print(
                    f"{project.name:22}\t{project.start_date}\t{project.priority}\t{project.cost_estimate:10}\t{project.completion_percentage}")

        elif choice == "F":
            # Filter Projects by Date
            pass
        elif choice == "A":
            # Add New Project
            name = input("Enter name: ")
            start_date = input("Enter start date: ")
            priority = int(input("Enter priority: "))
            cost_estimate = float(input("Enter cost estimate: "))
            completion_percentage = int(input("Enter completion percentage: "))
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
        elif choice == "U":
            # Update Project
            name = input("Enter name of project to update: ")
            for project in projects:
                if project.name == name:
                    print(project.completion_percentage)
                    updated_completion_percentage = int(input("Enter completion percentage: "))
                    project.completion_percentage = updated_completion_percentage
                    print(f"updated completed percentage is {updated_completion_percentage}%")
        else:
            print("Invalid menu choice")
        print(menu)
        choice = input("Enter menu option: ").upper()


def read_in_file(file_name, projects):
    in_file = open(file_name, 'r')
    in_file.readline()

    for line in in_file:
        parts = line.strip().split('\t')
        t = Project("jo", "2/01/2022", 1, 50, 90)
        projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))
    in_file.close()
    return projects


main()
