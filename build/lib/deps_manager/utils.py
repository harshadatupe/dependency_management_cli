import sys

def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    return wrapper
