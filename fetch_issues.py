import requests

# Function to fetch and process issues
def fetch_and_process_issues(token, owner="ray-project", repo="ray", issue_numbers_file_path="issue_numbers.txt"):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    # Open the file in write mode to clear it or create it if it doesn't exist
    with open(issue_numbers_file_path, 'w') as file:
        pass  # This simply clears the file
    
    # Loop through the first 100 pages of issues
    for page in range(1, 101):
        url = f"https://api.github.com/repos/{owner}/{repo}/issues"
        params = {
            "state": "closed",
            "labels": "bug,core",
            "per_page": 100,
            "page": page
        }
        response = requests.get(url, headers=headers, params=params)
        issues = response.json()

        # Check if we've reached an empty page indicating no more issues
        if not issues:
            print(f"Issues fetched successfully. Saved in "+issue_numbers_file_path)
            print(f"\n\n Filter Issues In Process...")
            break

        # Filter issues by title starting with [core] and write their numbers to a file
        with open(issue_numbers_file_path, 'a') as file:
            for issue in issues:
                if issue['title'].startswith("[core]"):
                    file.write(f"{issue['number']}\n")

# Execute the function
if __name__ == "__main__":
    fetch_and_process_issues()