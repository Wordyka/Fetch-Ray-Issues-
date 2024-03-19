from fetch_issues import fetch_and_process_issues
from filter_issues import process_issues
from github import Github
import os

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
    print("Issues with linked PRs:")
    for issue_number in issues_with_linked_prs:
        print(issue_number)

if __name__ == "__main__":
    main()