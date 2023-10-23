import subprocess


def run_migrations():
    try:
        subprocess.run(['python', 'manage.py', 'makemigrations'])

        subprocess.run(['python', 'manage.py', 'migrate'])
    except Exception as e:
        print(f"An error occurred: {e}")
