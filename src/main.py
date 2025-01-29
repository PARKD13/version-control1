from datetime import datetime

now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

with open("version.md", "w") as file:
    file.write(f"Current date and time: {timestamp}\n")
