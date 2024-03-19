# Fetch and Filter Ray Framework Issues using Github API

This project is designed to interface with the GitHub API to fetch issues from the `ray-project/ray` repository and filter out those that have linked pull requests. The workflow is divided into separate Python scripts that handle specific tasks.

## Components

- `fetch_issues.py`: This script connects to the GitHub API and retrieves issues that are both closed and labeled with "bug" and "core". It specifically looks for issues with titles that start with "[core]" and records their issue numbers in `issue_numbers.txt`.

- `filter_issues.py`: This script reads the issue numbers from `issue_numbers.txt` and uses the GitHub Search API to identify which of these issues have linked pull requests. It outputs a list of issue numbers that have associated PRs, one per line.

- `main.py`: Serves as the entry point to run the scripts in sequence. First, it executes `fetch_issues.py` to collect the issue numbers, then it runs `filter_issues.py` to filter and display issues with linked PRs.

- `issue_numbers.txt`: A text file that stores issue numbers fetched by `fetch_issues.py`. This file is overwritten each time `fetch_issues.py` runs.

## Setup

To set up and run this project:

1. Make sure Python 3.x is installed on your system.

2. Install the required Python packages:
##
    pip install requests PyGithub

3. Generate a GitHub Personal Access Token (PAT) with the appropriate permissions to read from the repository.

4. Replace the placeholder token in `fetch_issues.py` and `filter_issues.py` with your actual PAT.

## Usage

Run the program via the command line:

##
    python main.py

