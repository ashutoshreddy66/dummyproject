import os
import subprocess
from datetime import datetime, timedelta

# Start date for the graph
start_date = datetime(2024, 7, 1)  # First day of the year

# Cat face pattern
pattern = [
    "0001000",
    "0011100",
    "0111110",
    "0101010",
    "0111110",
    "0011100",
    "0001000",
]

# Loop over the pattern to make commits
for row_index, row in enumerate(pattern):
    for col_index, cell in enumerate(row):
        if cell == "1":  # Make a commit for "1" cells
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
