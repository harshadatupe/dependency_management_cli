import argparse
from .dependencies import *

def main():
    parser = argparse.ArgumentParser(description="Project Dependency Manager")
    parser.add_argument('language', choices=['python', 'cpp'], help="Language of the project")
    parser.add_argument('command', choices=['install', 'uninstall', 'list', 'update', 'lock'], help="Command to execute")
    parser.add_argument('--requirements', '-r', help="Path to requirements file")
    parser.add_argument('--package', '-p', help="Package name")
    parser.add_argument('--lock_file', '-l', help="Path to lock file")
    args = parser.parse_args()

    try:
        if args.command == 'install':
            if not args.requirements:
                raise ValueError("Missing path to requirements file.")
            install_dependencies(args.language, args.requirements)
        elif args.command == 'uninstall':
            if not args.package:
                raise ValueError("Missing package name.")
            uninstall_dependency(args.language, args.package)
        elif args.command == 'list':
            list_dependencies(args.language)
        elif args.command == 'update':
            if not args.requirements:
                raise ValueError("Missing path to requirements file.")
            update_dependencies(args.language, args.requirements)
        elif args.command == 'lock':
            if not args.requirements or not args.lock_file:
                raise ValueError("Missing path to requirements file or lock file.")
            with open(args.lock_file, 'w') as lock_file:
                lock_dependencies(args.language, args.requirements, lock_file)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()