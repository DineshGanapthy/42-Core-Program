import sys
import os
import site


def construct() -> None:
    v_path = os.environ.get('VIRTUAL_ENV')

    if v_path:
        # If we have a vitural environment, we are in the construct
        print("\nMATRIX STATUS: Welcome to the construct\n\n"
              f"Current Python: {sys.executable}\n"
              f"Vitual Environment: {os.path.basename(v_path)}\n"
              f"Environment path: {v_path}\n\n"
              "SUCCESS: You're in an isolated environment!"
              "Safe to install packages without affecting"
              "the global system.\n\n"
              "Package installation path:")
        if site.getsitepackages():
            print(f"{site.getsitepackages()[0]}")
        else:
            print('N/A')
        
    else:
        # We are outside the vitual environment/
        print("\nMATRIX STATUS: You're still plugged in\n\n"
              f"Current Python: {sys.executable}\n"
              f"Vitual Environment: None detected \n\n"
              "WARNING: You're in the global environment!\n"
              "The machines can see everything you install.\n\n"
              "To enter the construct, run:\n"
              "python -m venv matrix_env\n"
              "source matrix_env/bin/activate # On Unix"
              "matrix_env\Scripts\activate # On Windows\n\n"
              "Then run this program again."
        )


if __name__ == "__main__":
    construct()


