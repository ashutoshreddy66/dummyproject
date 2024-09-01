import os
import subprocess
from datetime import datetime, timedelta

# Define the start date and pattern (rows x columns for simplicity)
start_date = datetime(2024, 9, 1)
pattern = [
    "00100",  # Lights up only the middle block in the first row
    "01110",  # Lights up the middle three blocks in the second row
    "11111",  # Lights up all blocks in the third row
    "01110",  # Lights up the middle three blocks in the fourth row
    "00100"   # Lights up only the middle block in the fifth row
]

# Iterate over the pattern
for i, row in enumerate(pattern):
    for j, cell in enumerate(row):
        if cell == "1":  # Make a commit for "1" cells
            commit_date = start_date + timedelta(days=(i * 7) + j)
            # Create a dummy file and add it to the repo
            with open("dummy_file.txt", "a") as f:
                f.write(f"Commit for {commit_date}\n")
            subprocess.run(["git", "add", "dummy_file.txt"])
            # Make the commit with the specified date
            subprocess.run([
                "git", "commit", "--date", commit_date.strftime("%Y-%m-%dT%H:%M:%S"),
                "-m", f"Commit on {commit_date}"
            ])

# Push the changes to GitHub
subprocess.run(["git", "push"])
