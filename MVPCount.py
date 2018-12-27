import requests
import re

def fetch(url):
    response = requests.get(url)
    return response

def updateMemberMVPCount(team, found):
    if not found in team:
        team[found] = 0
    for name in team.keys():
        if name.lower() in found.lower():
            team[name] += 1

def printMVPList():
    URL = 'https://{gitlab url}/api/v4/groups/486/milestones?private_token={token}'
    beginningMilestoneId = 0
    team = {}

    # fetch milestone data
    milestones = fetch(URL).json()
    for milestone in milestones:
        # count only after beginningMilstoneId
        if milestone['iid'] < beginningMilstoneId:
            continue

        # fromat: Sprint MVP - Zam
        match = re.search(r'Sprint MVP - (\w*)', str(milestone['description']))
        if bool(match):
            foundMember = match.group(1)
            updateMemberMVPCount(team, foundMember)
            print(milestone['title'] + ': ' + foundMember)

    # show team member MVP count
    print(team)

printMVPList()