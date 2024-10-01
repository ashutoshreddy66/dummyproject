import os
import subprocess
from datetime import datetime, timedelta

# Start date for the graph
start_date = datetime(2024, 11, 1)  # Start from the first day of the year

# Pac-Man pattern
pattern = [
    "0000222",
    "0002222",
    "0022200",
    "0222220",
    "0222220",
    "0022200",
    "0000000",
]

# Loop through the pattern to make commits
for row_index, row in enumerate(pattern):
    for col_index, cell in enumerate(row):
        if cell == "2":  # Make a commit for "1" cells
            commit_date = start_date + timedelta(weeks=col_index, days=row_index)
            # Create a dummy file and add a commit
            with open("dummy_file.txt", "a") as f:
                f.write(f"Commit for {commit_date}\n")
            subprocess.run(["git", "add", "dummy_file.txt"])
            subprocess.run([
                "git", "commit", "--date", commit_date.strftime("%Y-%m-%dT%H:%M:%S"),
                "-m", f"Commit on {commit_date}"
            ])

# Push the changes to GitHub
subprocess.run(["git", "push", "--set-upstream", "origin", "main"])
