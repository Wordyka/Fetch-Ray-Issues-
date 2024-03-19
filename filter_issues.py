from github import Github
import time

def check_and_wait_for_rate_limits(g, search=False):
    """
    Check the GitHub API rate limits and wait if we're close to hitting them.
    This prevents the script from being blocked due to exceeding the rate limits.
    
    :param search: A boolean indicating whether to check the search API's rate limit.
    """
    # Fetch the current rate limit status from GitHub
    rate_limit = g.get_rate_limit()
    remaining = rate_limit.core.remaining if not search else rate_limit.search.remaining
    reset_time = rate_limit.core.reset if not search else rate_limit.search.reset
    current_time = time.time()
    
    # If we're close to the rate limit, wait until the reset time plus a buffer
    if remaining < 10:  # Using 10 as a buffer to avoid hitting the limit
        wait_time = max(reset_time.timestamp() - current_time, 0) + 10  # Adding 10 seconds as an extra buffer
        # print(f"Approaching rate limit. Waiting for {int(wait_time)} seconds.")
        time.sleep(wait_time)

def search_prs_mentioning_issue(g, repo, issue_number):
    """
    Search for pull requests mentioning a given issue number using GitHub's Search API.
    Includes rate limit checks specifically for the search API.
    
    :param issue_number: The number of the issue to search mentions for.
    :return: The issue number if linked PRs are found, None otherwise.
    """
    # Check and wait if we're close to the search API rate limit before making a search request
    check_and_wait_for_rate_limits(g, search=True)
    
    # Perform the search query
    prs = g.search_issues(f'{issue_number} type:pr repo:ray-project/ray')
    pr_numbers = [pr.number for pr in prs]
    if pr_numbers:
        print(f"Issue {issue_number} has linked PR(s): {', '.join(map(str, pr_numbers))}")
        return issue_number
    return None

def process_issues(token, issue_numbers):
    """
    Process a list of issue numbers to find and print those that have linked PRs.
    
    :param issue_numbers: A list of issue numbers to process.
    :return: A list of issue numbers that have linked PRs.
    """
    g = Github(token)
    repo = g.get_repo("ray-project/ray")
    issues_with_linked_prs = []
    for issue_number in issue_numbers:
        # Check and wait if we're close to the core API rate limit before fetching each issue
        check_and_wait_for_rate_limits(g)
        result = search_prs_mentioning_issue(g, repo, issue_number)
        if result:
            issues_with_linked_prs.append(result)
    return issues_with_linked_prs
