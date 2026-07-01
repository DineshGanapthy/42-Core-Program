#EX00
# This way is using a with statment
# import sys
# import typing

# def ft_anicent_text() -> None:
#     """ Open, read and close a file"""
#     try:
#         print("=== Cyber Archives Recovery ===")
#         print(f"Asscessing file '{sys.argv[1]}'\n ---\n")
#         # file_name = "ancient_fragment.txt"
#         # sys.argv[1] == "ancient_fragment.txt"
#         file_name = sys.argv[1]
#         with open(file_name) as file:
#             print(file.read())
#         print(f"\n ---\n File '{file_name}' closed.")
#         # file.open(file_name)
#         # file.close(file_name)
#     #""" Nonexistent file """
#     except FileNotFoundError:
#         print(f"Error opening file {sys.argv[1]}: [Errno 2] No such file or dicrectory: '{file_name}'")
#     #""" Inaccessible file"""
#     except PermissionError:
#     #except Exception:
#         print(f"Error opening file {sys.argv[1]}: [Errno 13] Permission denied: '{file_name}'")

# if __name__ == "__main__":
#     ft_anicent_text()

#EX01

    # new_file = open(file_name, "w")
    #     modified_line = [f"{line.strip('\n')}#\n" for line in lines]
    #     new_file.write(modified_line)
    #     new_file.close()
    #     print(f"\n---\nFile '{file_name}' closed.")

#     import sys
# import typing


# def ft_archive_creation() -> None:
#     """ Open, read and close a file"""
#     try:
#         print("=== Cyber Archives Recovery ===")
#         print(f"Asscessing file '{sys.argv[1]}'")
#         file_name = sys.argv[1]
#         file = open(file_name, "r")
#         content = file.read()
#         print("---\n")
#         print(content)
#         file.close()
#         print(f"\n---\nFile '{file_name}' closed.")

#         file = open(file_name, "r")
#         lines = file.readlines()

#         # new_file = open("hello_world.txt", "w")
#         char_to_append = "#"

#         print("Transformed data:\n---\n")
#         for line in lines:
#             modified_line = line.rstrip("\n") + char_to_append + "\n"
#             # new_file.write(modified_line)
#             print(modified_line, end="")
#         print("---\n")
#         # new_file.close()

#         new_file = input("Enter new file name (or empty): ")
#         if not new_file:
#             print("Not Saving data")
#         else:
#             new_file = open(f"{new_file}", "w")
#             for line in lines:
#                 modified_line = line.rstrip("\n") + char_to_append + "\n"
#                 new_file.write(modified_line)

import sys
# import typing

"""
Everything is in one big try/except block currently
This is bad practice because it's harder to write proper error handling
since the same error has to be handled differently depending on where it's thrown

Separate everything into several try except blocks
- One for reading
- One for writing
"""

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

        #   """ Inaccessible file"""
        except PermissionError:
            sys.stdout.write(f"[STDERR] Error opening file '{file_name}': "
                             f"[Errno 13] Permission denied: '{file_name}'\n")
            print("Data not saved")

           #   """ Nonexistent file """
    except FileNotFoundError:
        sys.stdout.write(f"[STDERR] Error opening file '{file_name}': "
                         f"[Errno 2] No such file or dicrectory: '{file_name}'\n")
    #   """ Inaccessible file"""
    except PermissionError:
        sys.stdout.write(f"[STDERR] Error opening file '{file_name}': "
                         f"[Errno 13] Permission denied: '{file_name}'\n")

    #EX02
    # try:
    #     file = open(file_name, "r")
    #     lines = file.readlines()
    #     char_to_append = "#"

    #     print("Transformed data:\n---\n")
    #     for line in lines:
    #         modified_line = line.rstrip("\n") + char_to_append + "\n"
    #         print(modified_line, end="")
    #     print("---\n")

    #     new_file = input("Enter new file name (or empty): ")
    #     if not new_file:
    #         print("Not Saving data")
    #     else:
    #         new_file_object = open(f"{new_file}", "w")
    #         for line in lines:
    #             modified_line = line.rstrip("\n") + char_to_append + "\n"
    #             new_file_object.write(modified_line)
    #         print(f"Saving to new '{new_file}'")
    #         print(f"Data saved in file '{new_file}'")

    #     #   """ Inaccessible file"""
    # except PermissionError:
    #     sys.stdout.write(f"[STDERR] Error opening file '{file_name}': "
    #                      f"[Errno 13] Permission denied: '{file_name}'\n")
    #     print("Data not saved")


if __name__ == "__main__":
    ft_stream_managment()


#EX03 - It works

def ft_secure_archive(filename) -> tuple: #, action: str, src_file: str) -> None:
    try:
        file_name = filename
        with open(file_name) as file:
            #print(file.read())
            content = file.read()
            #file_name == True
        print("Using 'secure_archieve' to read from a regular file: ")
        return (True, f"'{content}'\n")
        print("Using 'secure_archive' to write previous content to a new file:")
    except FileNotFoundError:
        print("Using 'secure_archive' to read from a nonexistent file: ")
        return (False, f"[Errno 2] No such file or directory: {file_name}")
    except PermissionError:
        print("Using 'secure_archive' to read from an inaccessible file: ")
        return (False, f"[Errno 13] Permission denied: {file_name}")

    

def ft_vault_security() -> None:
    print("=== Cyber Archives Security ===\n")
    print(ft_secure_archive('/not/existing/file'), "\n")
    print(ft_secure_archive('/etc/master.passwd'), "\n")
    print(ft_secure_archive('ancient_fragment.txt'), "\n")
    #results = ft_secure_archive(sys.argv[1]) - non hard code version
    # print(f"{nonexistent_file}\n")
    # print(f"{inaccessible_file}\n")
    # print(f"{regular_file}\n")

if __name__ == "__main__":
    ft_vault_security()

# def ft_secure_archive(filename: str, action: str = "read", content: str = "") -> tuple[bool, str]:
#     try:
#         with open(filename, "a") as input_file:
#             content = input_file.read()
#             # print(content)
#             if not content:
#                 return (file_operation == False)
#             else:
#                 file_operation == True
#         print("Using 'secure_archieve' to read from a regular file: ")
#         return (file_operation, f"'{content}'\n")
#         new_file_object = open(f"{new_file}", "action")
#         for line in lines:
#             new_file_object.write(modified_line)
#             print(f"Saving to new '{new_file}'")
#         print("Using 'secure_archive' to write previous content to a new file:")
#     except FileNotFoundError:
#         print("Using 'secure_archive' to read from a nonexistent file: ")
#         return (False, f"[Errno 2] No such file or directory: {file_name}")
#     except PermissionError:
#         print("Using 'secure_archive' to read from an inaccessible file: ")
#         return (False, f"[Errno 13] Permission denied: {file_name}")

    

# def ft_vault_security() -> None:
#     print("=== Cyber Archives Security ===\n")
#     # print(ft_secure_archive('/not/existing/file', r, ), "\n")
#     # print(ft_secure_archive('/etc/master.passwd',r ,), "\n")
#     print(ft_secure_archive('ancient_fragment.txt', "r", "new_file" ), "\n")
#     #results = ft_secure_archive(sys.argv[1]) - non hard code version
#     # print(f"{nonexistent_file}\n")
#     # print(f"{inaccessible_file}\n")
#     # print(f"{regular_file}\n")

# if __name__ == "__main__":
#     ft_vault_security()