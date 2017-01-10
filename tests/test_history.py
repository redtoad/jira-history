import datetime
import os

import jira_cache
import pytest

import jira_history
import jira_history.history

TEST_DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'issues.json')


@pytest.fixture
def testdata():
    data = jira_cache.CachedIssues.load(open(TEST_DATA))
    return {item.key: item for item in data}


def test_add_history(testdata):
    issue = testdata['JRA-7321']
    assert not hasattr(issue, 'history')
    jira_history.add_history(issue)
    assert hasattr(issue, 'history')


def test_at_now_returns_current_values(testdata):
    issue = testdata['JRA-7321']
    jira_history.add_history(issue)
    values = issue.history.at(datetime.datetime.now())
    assert values == jira_history.history.Changelog._clone_resource(issue)


def test_at_creation_time_returns_initial_values(testdata):
    issue = testdata['JRA-7321']
    jira_history.add_history(issue)
    values = issue.history.at(jira_history.history.to_datetime(issue.fields.created))
    assert values != jira_history.history.Changelog._clone_resource(issue)
