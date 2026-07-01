from dotenv import load_dotenv
import os
import sys

def check_security():
    """Simulates a security check to make sure no secrets are hardcoded"""
    print("Environment security check:")

    #Checks id .env file exists in the directory
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file not found")

    print("[OK] No hardcoded secrets detected")
    print("[OK] Production overrides available\n")

def oracle():
    print("ORACLE STATUS: Reading the Matrix...\n")

    #1. First it will load the env. file if it exists,
    #override_False means if an envirnoment variable already exists in the termainal
    #Python will respect the terminal over the .env file
    load_dotenv(override=False)

    #2. Retrive envirnoment variables with fallback/error handling
    matrix_mode = os.environ.get("MATRIX_MODE")
    database_url = os.environ.get("DATABASE_URL")
    api_key = os.environ.get("API_KEY")
    log_level = os.environ.get("LOG_LEVEL")
    zion_endpoint = os.environ.get("ZION_ENDPOINT")

    #3 Handling missing configuration scenarios (Error Handling)
    required_variables = {
        "MATRIX_MODE": matrix_mode,
        "DATABASE_URL": database_url,
        "API_KEY": api_key
    }

    missing_variables = [var for var, val in required_variables.items() if val is None]

    if missing_variables:
        print("[ERROR] Critical configuration missing!")
        for var in missing_variables:
            print(f" -> Missing variable: {var}")
        print("\nPlease build your .env file or export environment variables.")
        sys.exit(1) #Gracefully exits the program with an error staus

    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")
    if matrix_mode.lower() == "production":
        print("Datebase: Connected to PRODUCTION secure cluster")
        print(f"Log Level: {log_level if log_level else 'INFO'} (Optimized for Production)")
    else:
        print("Datebase: Connected to local instance")
        print(f"Log Level: {log_level if log_level else 'DEBUG'}")

    if api_key:
        print("API Access: Authenticated")

    if zion_endpoint:
        print("Zion Network: Online\n")

    check_security()
    print("The Oracle sees all configurations.")

if __name__ == "__main__":
    oracle()