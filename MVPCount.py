import requests
import re

def fetch(url):
    response = requests.get(url)
    return response

def updateMemberMVPCount(team, found):
    for name in team.keys():
        if name.lower() in found.lower():
            team[name] += 1

def printMVPList():
    URL = 'https://{gitlab url}/api/v4/groups/486/milestones?private_token={token}'
    team = {'Zam': 0, 'Vantist': 0, 'Henry': 0, 'Ian': 0, 'Phate': 0, 'Jason': 0}

    # fetch milestone data
    milestones = fetch(URL).json()
    for milestone in milestones:
        # fromat: **Sprint MVP - Zam** or ** Sprint MVP - Zam **
        match = re.search(r'Sprint MVP - (\w*)', str(milestone['description']))
        if bool(match):
            foundMember = match.group(1)
            updateMemberMVPCount(team, foundMember)
            print(milestone['title'] + ': ' + foundMember)

    # show team member MVP count
    print(team)

printMVPList()