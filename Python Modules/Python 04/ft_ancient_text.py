import sys
# import typing

def ft_anicent_text() -> None:
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
    #   """ Nonexistent file """
    except FileNotFoundError:
        print(f"Error opening file '{file_name}': "
              f"[Errno 2] No such file or dicrectory: '{file_name}'\n")
    #   """ Inaccessible file"""
    except PermissionError:
        print(f"Error opening file '{file_name}': "
              f"[Errno 13] Permission denied: '{file_name}'\n")


if __name__ == "__main__":
    ft_anicent_text()
