"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data_list = get_data()
    print(data_list)

    for i in range(0, len(data_list)):
        print(f"{data_list[i][0]} is taught by {data_list[i][1]} and had {data_list[i][2]} students")

def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data_list = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        data_list.append(parts)
        # print(parts)  # See what the parts look like (notice the integer is a string)
        # parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
    input_file.close()
    return data_list


main()