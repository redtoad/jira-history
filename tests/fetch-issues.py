
"""
Fetched test data from public JIRA instance and stores it in JSON file.
"""

URL = 'https://jira.atlassian.com/'

from jira import JIRA
from jira_cache import CachedIssues

jira = JIRA(URL)
issues = jira.search_issues("text ~ Python", expand='changelog')
cached = CachedIssues(issues)

with open('issues.json', 'w') as fp:
    cached.dump(fp)
