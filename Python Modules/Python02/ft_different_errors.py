def garden_operations(error_code: int) -> None:
    """ Error Types """
    if (error_code == 0):
        int("abc")
    elif (error_code == 1):
        10/0
    elif (error_code == 2):
        open("missing.txt")
    elif (error_code == 3):
        "abc" + 2


def test_error_types() -> None:
    """Catching Erros"""
    print("=== Garden Error Types Demo ===")
    # tests = ["0", "1", "2", "3", "4"]
    for i in range(5):
        print(f"Testing Operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully\n")
        except ValueError as e:
            print("Caught ValueError:", e)
        except ZeroDivisionError as e:
            print("Caught ZeroDivisionError:", e)
        except FileNotFoundError as e:
            print("Caught FileNotFoundError:", e)
        except TypeError as e:
            print("Caught TypeError:", e)
    print("All error types tested successfully")


if __name__ == "__main__":
    test_error_types()
