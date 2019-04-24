# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.1.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # GitHub API connections

# This uses the `PyGithub` package

from github import Github
import credentials as cred

# If we are just trying to get public data, we can use regular credentials

g = Github(cred.GITHUB_TOKEN)

# ## Get repo names for a user

repo_list = []
for repo in g.get_user("ChristinaB").get_repos():
    if "feedstock" not in repo.name:
        repo_list.append(repo.name)
    else:
        pass

repo_list

# ## Get orgs for a user
#
# Currently not working: basic users don't have access to other users' organizations.

for org in g.get_user("deppen8").get_orgs():
    print(org.name)

# (Note that nothing gets printed by this statement.)

# ## Get contributors on a repo

# To get contributors to a specific repo...

for person in g.get_user("deppen8").get_repo("pandas-vet").get_contributors():
    print(person.login)

# To get all contributors that a person has worked with..
#
# Notes:
# - This list includes the user
# - Also includes all contributors to forked repos

print("The following list is limited to the first 10 repos for space reasons:")
for repo in g.get_user("deppen8").get_repos()[0:10]:
    for person in repo.get_contributors():
        print(person.login)

# To get repos not including forks, use the following:

for repo in g.get_user("deppen8").get_repos():
    if repo.fork == False:
        for person in repo.get_contributors():
            print(person.login)


