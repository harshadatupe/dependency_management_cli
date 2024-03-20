from utils import handle_error

@handle_error
def backport_changes(mainline_branch):
    try:
        subprocess.run(['git', 'checkout', mainline_branch], check=True)
        subprocess.run(['git', 'pull'], check=True)
        subprocess.run(['git', 'checkout', '-'], check=True)
        print("Changes backported successfully.")
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to backport changes: {e}")

@handle_error
def track_dependency_changes():
    try:
        subprocess.run(['pip', 'list', '--outdated'], check=True)
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to track dependency changes: {e}")