import os
import json


def get_subfolders():
    """
    This function gets all the immediate subfolder names
    in the directory where the script is being executed.
    It ignores the .git folder and sorts the remaining folders
    numerically from lesser to bigger.
    """
    try:
        # Get the list of all entries in the current directory
        entries = os.listdir('.')

        # Filter the list to get only the subfolders, ignoring the .git folder
        subfolders = [entry for entry in entries if os.path.isdir(entry) and entry != '.git']

        # Sort the list of subfolders numerically
        # Assumes folder names can be cast to integers.
        subfolders.sort(key=int)

        return subfolders
    except ValueError:
        # Handle cases where folder names are not valid numbers.
        print("Error: One or more folder names could not be converted to a number.")
        return []
    except OSError as e:
        print(f"Error: {e}")
        return []


def create_json_output():
    """
    This function creates and prints the desired JSON output
    containing the sorted list of subfolders.
    """
    subfolders = get_subfolders()

    # Create a dictionary with a "posts" key
    # The value is the sorted list of subfolders
    output_data = {"posts": subfolders}

    # Convert the dictionary to a JSON string and print it
    # 'indent=4' makes the output more readable
    json_output = json.dumps(output_data, indent=4)
    print(json_output)


if __name__ == "__main__":
    create_json_output()