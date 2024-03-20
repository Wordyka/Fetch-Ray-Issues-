from fetch_issues import fetch_and_process_issues
from filter_issues import process_issues
from github import Github
import os
import numpy as np

def normally_distributed_sampling(file_path, sample_size=100, total_pages=10, issues_per_page=100):
    """
    Generates a normally distributed sample of issue numbers from issue_numbers file.

    Args:
        file_path: The path to the file containing issue numbers.
        sample_size: The desired size of the sample.
        total_pages: The total number of pages considered for the pool.
        issues_per_page: The number of issues per page.

    Saves the sampled issue numbers to 'sample_issue_numbers.txt'.
    """
    total_issues = total_pages * issues_per_page
    mean = total_issues / 2
    std_dev = total_issues / 10  # Adjust this for your desired distribution spread

    # Generate normally distributed indices
    indices = np.random.normal(loc=mean, scale=std_dev, size=sample_size)
    indices = np.clip(indices, 0, total_issues - 1).astype(int)  # Clip to valid range and convert to int

    # Read the issue numbers from the file
    with open(file_path, "r") as file:
        issue_numbers = [line.strip() for line in file]

    # Select issues based on the generated indices
    sampled_issues = [issue_numbers[i % len(issue_numbers)] for i in indices]

    # Write the sampled issue numbers to a new file
    with open("sample_issue_numbers.txt", "w") as file:
        for issue in sampled_issues:
            file.write(issue + "\n")

def main():
    # Define the token and repository details
    # Replace 'your_default_token' with a valid token
    token = os.getenv('GITHUB_TOKEN', 'your_default_token') 

    # Define the Github instance
    g = Github(token)
    repo = g.get_repo("ray-project/ray") 

    # Fetch issues and write their numbers to a file
    fetch_and_process_issues(token)
    
    # Read the fetched issue numbers and filter those with linked PRs
    with open("issue_numbers.txt", "r") as file:
        issue_numbers = [int(line.strip()) for line in file]

    # Process the issues to find those with linked PRs
    issues_with_linked_prs = process_issues(g, repo, issue_numbers)

    # Overwrite the file with the numbers of issues that have linked PRs
    with open("issue_numbers.txt", "w") as file:
        for issue_number in issues_with_linked_prs:
            file.write(f"{issue_number}\n")

    # Print the results to the console
    print("\n\n List of issues with linked PRs:")
    for issue_number in issues_with_linked_prs:
        print(issue_number)
    
    # After processing issues, generate a normally distributed sample
    normally_distributed_sampling("issue_numbers.txt")

if __name__ == "__main__":
    main()