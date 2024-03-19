from fetch_issues import fetch_and_process_issues
from filter_issues import process_issues

def main():
    # Fetch issues and write their numbers to a file
    fetch_and_process_issues()
    
    # Read the fetched issue numbers and filter those with linked PRs
    with open("issue_numbers.txt", "r") as file:
        issue_numbers = [int(line.strip()) for line in file]

    issues_with_linked_prs = process_issues(issue_numbers)
    print("Issues with linked PRs:")
    for issue_number in issues_with_linked_prs:
        print(issue_number)

if __name__ == "__main__":
    main()
    