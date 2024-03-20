# Fetch and Filter Ray Framework Issues using Github API

This project is designed to interface with the GitHub API to fetch issues from the `ray-project/ray` repository and filter out those that have linked pull requests. The workflow is divided into separate Python scripts that handle specific tasks.

## Components

- `fetch_issues.py`: Retrieves closed issues labeled "bug" and "core" from the GitHub repository. It looks specifically for issues whose titles start with "[core]" and records their numbers in `issue_numbers.txt`.

- `filter_issues.py`: Reads issue numbers from `issue_numbers.txt` and searches for linked pull requests using the GitHub Search API. The results are output to the console.

- `main.py`: The entry point for running the scripts. It sequentially executes `fetch_issues.py` and `filter_issues.py`, carrying out the issue fetching and filtering process. Additionally, it performs a normally distributed random sampling of the filtered issue numbers and saves the sample to `sample_issue_numbers.txt`.

- `issue_numbers.txt`: A generated text file that serves as a record of issue numbers fetched by `fetch_issues.py`.

- `sample_issue_numbers.txt`: The output file containing a sample of issue numbers selected through normally distributed random sampling.


## Setup

To set up and run this project:

1. Make sure Python 3.x is installed on your system.

2. Install the required Python packages:
```bash
pip install requests PyGithub numpy
```

3. Generate a GitHub Personal Access Token (PAT) with the appropriate permissions to read from the repository.

4. Replace the placeholder token in `main.py` with your actual PAT.

## Usage

Run the program via the command line:
```bash
python main.py
```

