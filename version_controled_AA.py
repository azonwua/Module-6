"""Module 6 version-control

Run this starter program, complete the TODO tasks, and commit your changes.
No outside packages are required.
"""


def show_project_info():
    """Display basic information about this version-control exercise."""
    project_name = "Python Version Control Exercise"
    version = "1.1"
    print(f"Project: {project_name}")
    print(f"Version: {version}")
    print("Git helps track changes in a software project.")


def show_git_workflow():
    """Print the basic sequence used in this exercise."""
    steps = [
        "1. Edit and save your Python file.",
        "2. Stage your changes with git add.",
        "3. Record a local commit with git commit.",
        "4. Upload your commit to GitHub with git push.",
    ]
    for step in steps:
        print(step)


def main():
    show_project_info()
    print()
    show_git_workflow()
    print()

    # TODO 1: Change the project_name and version values above to your own.
    # TODO 2: Add a print() statement below that explains, in your own words,
    #         why it is useful to save your code changes with Git.
    print("Tracking code changes with Git is useful because it provides a complete history of your project, allowing you to easily revert to earlier versions if something breaks.")

    # TODO 3: Add another print() statement describing one difference
    #         between git commit and git push.
    print("One difference is that 'git commit' saves your staged changes locally on your machine, while 'git push' uploads those local commits to a remote repository like GitHub.")


if __name__ == "__main__":
    main()
