import sys
# import typing


def ft_archive_creation() -> None:
    """ Open, read and close a file"""
    try:
        print("=== Cyber Archives Recovery ===")
        print(f"Asscessing file '{sys.argv[1]}'")
        file_name = sys.argv[1]
        file = open(file_name, "r")
        content = file.read()
        print("---\n")
        print(content)
        file.close()
        print(f"\n---\nFile '{file_name}' closed.")

        file = open(file_name, "r")
        lines = file.readlines()
        char_to_append = "#"

        print("Transformed data:\n---\n")
        for line in lines:
            modified_line = line.rstrip("\n") + char_to_append + "\n"
            print(modified_line, end="")
        print("---\n")

        new_file = input("Enter new file name (or empty): ")
        if not new_file:
            print("Not Saving data")
        else:
            new_file_object = open(f"{new_file}", "w")
            for line in lines:
                modified_line = line.rstrip("\n") + char_to_append + "\n"
                new_file_object.write(modified_line)
            print(f"Saving to new '{new_file}'")
            print(f"Data saved in file '{new_file}'")
    #   """ Nonexistent file """
    except FileNotFoundError:
        print(f"Error opening file '{file_name}': "
              f"[Errno 2] No such file or dicrectory: '{file_name}'\n")
    #   """ Inaccessible file"""
    except PermissionError:
        print(f"Error opening file '{file_name}': "
              f"[Errno 13] Permission denied: '{file_name}'\n")


if __name__ == "__main__":
    ft_archive_creation()
