"""
This main.py module acts as a cli interface to parse the user inputs in command line
and executes related function from dependencies.py module.
"""
# Python standard library imports
import argparse

# Local application imports
from .dependencies import *


def main():
    """
    The main function acts as a CLI to parse input from user and executes the commands and 
    returns result to user on stdout.
    """
    parser = argparse.ArgumentParser(description="Project Dependency Manager")
    parser.add_argument('language', choices=['python', 'cpp'], help="Language of the project")
    parser.add_argument('command', choices=['install', 'uninstall', 'list', 'update', 'lock'], help="Command to execute")
    parser.add_argument('--requirements', '-r', help="Path to requirements file")
    parser.add_argument('--package', '-p', help="Package name")
    parser.add_argument('--lock_file', '-l', help="Name of the lock file")
    parser.add_argument('--venv', '-v', help="Path to the virtual environment")
    args = parser.parse_args()

    try:
        if args.command == 'install':
            if not args.requirements:
                raise ValueError("Missing path to requirements file.")
            install_dependencies(args.language, args.requirements, args.venv)
        elif args.command == 'uninstall':
            if not args.package:
                raise ValueError("Missing package name.")
            uninstall_dependency(args.language, args.package, args.venv)
        elif args.command == 'list':
            list_dependencies(args.language, args.venv)
        elif args.command == 'update':
            if not args.requirements:
                raise ValueError("Missing path to requirements file.")
            update_dependencies(args.language, args.requirements, args.venv)
        elif args.command == 'lock':
            if not args.lock_file:
                raise ValueError("Missing name of the requirements lock file.")
            lock_dependencies(args.language, args.venv, args.lock_file)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
