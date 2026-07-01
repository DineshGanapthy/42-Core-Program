import sys
# import typing


def ft_stream_managment() -> None:
    """ Open, read and close a file"""
    try:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        file_name = sys.argv[1]
        file = open(file_name, "r")
        content = file.read()
        print("---\n")
        print(content)
        file.close()
        print(f"---\nFile '{file_name}' closed.\n")

        try:
            file = open(file_name, "r")
            lines = file.readlines()
            char_to_append = "#"

            print("Transformed data:\n---\n")
            for line in lines:
                modified_line = line.rstrip("\n") + char_to_append + "\n"
                print(modified_line, end="")
            print("\n---")

            print("Enter new file name (or empty):")
            new_file = sys.stdin.readline().rstrip('\n')
            if not new_file:
                print("Not Saving data")
            else:
                new_file_object = open(f"{new_file}", "w")
                for line in lines:
                    modified_line = line.rstrip("\n") + char_to_append + "\n"
                    new_file_object.write(modified_line)
                print(f"Saving to new '{new_file}'")
                print(f"Data saved in file '{new_file}'")

        #   """ Inaccessible file"""
        except PermissionError:
            print(f"Saving to new '{new_file}'")
            sys.stdout.write(f"[STDERR] Error opening file '{file_name}': "
                             f"[Errno 13] Permission denied: '{file_name}'\n")
            print("Data not saved")
        #   """ Nonexistent file """
    except FileNotFoundError:
        sys.stdout.write(f"[STDERR] Error opening file '{file_name}': "
                         f"[Errno 2] No such file or dicrectory: "
                         F"'{file_name}'\n")
    #   """ Inaccessible file"""
    except PermissionError:
        sys.stdout.write(f"[STDERR] Error opening file '{file_name}': "
                         f"[Errno 13] Permission denied: '{file_name}'\n")


if __name__ == "__main__":
    ft_stream_managment()
