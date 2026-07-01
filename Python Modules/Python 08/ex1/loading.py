import sys
import importlib

NEEDED_PACKAGES = ["pandas","numpy","requests","matplotlib"]

DISAPLY_MESSAGES = {
    "pandas":  "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "requests": "Network access ready",
    "matplotlib": "Visualization ready"
}

def check_dependencies():
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    missing = []
    for package in NEEDED_PACKAGES:
        try:
            module = importlib.import_module(package)
            version = getattr(module, "__version__", "unknown version")
            if package in DISAPLY_MESSAGES:
                message = DISAPLY_MESSAGES[package]
                print(f"[ok] {package} ({version}) - {message}")
        except ImportError:
            print(f"[MISSING] {package}")
            missing.append(package)
    if missing:
        print("\nSome dependencies are missing.")
        print("Install using pip package:")
        print(" pip install -r requirements.txt\n")
        print("Or you may use Poetry:")
        print(" poetry install")
        sys.exit(1)


def run_analysis():
    import numpy as np 
    import pandas as pd 
    import matplotlib.pyplot as plt
    print("\nAnalyzing Matirx data...")
    print("Processing 1000 data points...")
    data = np.random.rand(1000)
    data2 = pd.DataFrame(data, columns=["Signal"])
    print("Generating visualization...")
    plt.figure()
    plt.plot(data2["Signal"])
    plt.title("Matrix Signal Analysis")
    plt.xlabel("Index")
    plt.ylabel("Signal Value")
    plt.savefig("matrix_analysis.png")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")

if __name__ == "__main__":
    check_dependencies()
    run_analysis()