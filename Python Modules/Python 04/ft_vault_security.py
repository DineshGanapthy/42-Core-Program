import sys

def secure_archive(filename: str, action: str = "read", content: str = "") -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, 'r') as file:
                data = file.read()
            return (True, data)
        elif action == "write":
            with open(filename, 'w') as file:
                file.write(content)
            return (True, "'Content successfully written to file'") 
        else:
            return (False, f"Invaild action {action}")
        #   """ Nonexistent file """
    except FileNotFoundError:
       return(False, f"[Errno 2] No such file or dicrectory: '{filename}'")
    #   """ Inaccessible file"""
    except PermissionError:
        return(False, f"[Errno 13] Permission denied: '{filename}'")


def ft_vault_security() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    testing = secure_archive("/not/existing/file")
    print(testing , "\n")

    print("Using 'secure_archive' to read from an inaccessible file:")
    testing = secure_archive("/etc/master.passwd")
    print(testing , "\n")

    print("Using 'secure_archive' to read from a regular file:")
    testing = secure_archive("ancient_fragment.txt")
    print(testing , "\n")

    if testing[0] == True:
        print("Using 'secure_archive' to write previous content to a new file:")
        result = secure_archive("new_file_creation.txt", "write", testing[1])
        print(result)
 

if __name__ == "__main__":
    ft_vault_security()

