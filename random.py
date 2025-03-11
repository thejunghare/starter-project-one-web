import csv
import random

def create_groups(csv_filepath, group_size=4):
    """
    Reads student names from a CSV file, creates groups of a specified size,
    and assigns unique techie names to each group.

    Args:
        csv_filepath: Path to the CSV file containing student names.
        group_size: The desired size of each group.

    Returns:
        A list of groups, where each group is a list of student names with a group name.
    """

    try:
        with open(csv_filepath, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            students = [row[0] for row in reader if row]  # Extract student names from the first column

    except FileNotFoundError:
        print(f"Error: File '{csv_filepath}' not found.")
        return []

    num_students = len(students)
    if num_students < group_size:
        print(f"Error: Not enough students for groups of {group_size}")
        return []

    random.shuffle(students)
    groups = []
    techie_names = ["Tech Titans", "Code Crusaders", "Binary Brawlers", "Digital Dominators", "Pixel Pioneers",
                    "Byte Riders", "Algorithm Aces", "Innovation Incubators", "Cyber Squad", "Logic Legends",
                    "Data Dynamos", "Network Ninjas", "Software Savants", "GUI Gurus", "Cloud Commanders"]

    for i in range(0, num_students, group_size):
        group = students[i:min(i + group_size, num_students)]
        if len(group) < group_size and len(groups) > 0:
            # Add remaining students to the last group's members
            groups[-1]['members'].extend(group)
            continue
        group_name = techie_names.pop(random.randrange(len(techie_names))) if techie_names else f"Group {len(groups) + 1}"
        groups.append({"group_name": group_name, "members": group})

    return groups

# Example usage: Replace 'students.csv' with your file's path
# Make sure to upload students.csv to your Colab environment first
groups = create_groups('file.csv')

# Print the groups
for group in groups:
    print(f"Group: {group['group_name']}")
    for student in group['members']:
        print(f"  - {student}")
    print()