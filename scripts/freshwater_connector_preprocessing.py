import bibtexparser
from github import Github
import pandas as pd
import networkx as nx
from fuzzywuzzy import fuzz


HS_USERNAME = ""
HS_PASSWORD = ""
GITHUB_KEY = ""

'''
This file creates two csv files to be uploaded to Tableau to create the connector visualization
WHW_edge_collabs : This file contains each connection and also how they are linked and a link to the resource
WHW_XY : This file contains the X and Y coordinates required to place each node ont he visualization
'''


class Collaboration:
    def __init__(self, year, title, authors, medium=None, doi=None):
        self.year = year
        self.title = title
        self.authors = authors
        self.medium = medium
        self.doi = doi

    def __repr__(self):
        return "<year:%s title:%s doi:%s medium:%s authors:%s>" % (self.year, self.title, self.doi, self.medium, self.authors)
    

class Author:
    def __init__(self, name, collaborations):
        self.name = name
        self.collaborations = collaborations
    
    def __repr__(self):
        return "<name:%s collaborations:%s" % (self.name, self.collaborations)


# Go through bib file and create Collaboration objects for journals
def populate_collaborations():
    collaboration_list = list()
    for item in bib_database.entries:
        title = item["title"].replace("{", "").replace("}", "")
        
        if 'doi' in item.keys():
            if 'medium' in item.keys():
                j = Collaboration(item["year"], title, item["author"], item["medium"], item["doi"])
            else:
                j = Collaboration(item["year"], title, item["author"], None, item["doi"])
        else:
            if 'medium' in item.keys():
                j = Collaboration(item["year"], title, item["author"], item["medium"])
            else:
                j = Collaboration(item["year"], title, item["author"])
            
        collaboration_list.append(j)
    return collaboration_list


# Go through the collaboration list and create Author objects
def create_collaboration_edges(author_map, author_list, collaboration):
    for a in author_list:
        if a in author_map.keys():
            author_obj = author_map[a]
            author_obj.collaborations.append(collaboration)
        else:
            collab_list = list()
            collab_list.append(collaboration)
            author_obj = Author(a, collab_list)
            author_map[a] = author_obj


# Go through the collaboration list and create Author objects
def create_journal_edges(author_map, list_of_collaborations):
    for collaboration in list_of_collaborations:
        authors_str = collaboration.authors
        split_authors = authors_str.split(" and ")
        create_collaboration_edges(author_map, split_authors, collaboration)


# Go through the github repo list and create Author objects
def create_github_edges(author_map):
    for repo in g.get_user("waterhackweek").get_repos():
        if "feedstock" not in repo.name:
            if repo.name[:3] == 'whw':
                year = repo.created_at.year
                title = repo.name
                doi = "waterhackweek/" + repo.name
                collabs = ""
                contributors_list = g.get_user("waterhackweek").get_repo(repo.name).get_contributors()
                for person in contributors_list:
                    if person.name != None:
                        collabs += person.name + " and "
                    else:
                        collabs += person.login + " and "    
                    
                collabs = collabs[:-5]
                collaboration = Collaboration(year, title, collabs, "Github", doi)
                split_authors = collabs.split(" and ")
                create_collaboration_edges(author_map, split_authors, collaboration)
        else:
            pass


def create_hydroshare_edges(hs, author_map):
    for res in hs.resources(group="Waterhackweek 2019", public=True):
        if len(res['authors']) > 1:
            dt = pd.to_datetime(res["date_created"])
            year = dt.year
            doi = res['resource_url']
            title = res['resource_title']
            collabs = ""
            contributors_list = res['authors']
            for person in contributors_list:
                collabs += person + " and "
            collabs = collabs[:-5]
            collaboration = Collaboration(year, title, collabs, "Hydroshare", doi)
            create_collaboration_edges(author_map, res["authors"], collaboration)


def create_neighborhood_map(author_map): 
    neighbor_map = {}
    edges_map = {}
    for key in author_map.keys():
        collab_authors = set()
        for item in range(len(author_map[key].collaborations)):
            collabs = author_map[key].collaborations[item].authors
            collab_list = collabs.split(" and ")
            for c in collab_list:
                if c != key:
                    collab_authors.add(c)
                    doi = author_map[key].collaborations[item].doi
                    if doi is None:
                        doi = ""
                    elif author_map[key].collaborations[item].medium == 'Github':
                        doi = "https://github.com/" + doi
                    elif author_map[key].collaborations[item].medium != 'Hydroshare':
                        doi = "https://doi.org/" + doi
                    edges_map[key + "<->" + c] = doi
        neighbor_map[key] = collab_authors
    return neighbor_map, edges_map


from hs_restclient import HydroShare, HydroShareAuthBasic
auth = HydroShareAuthBasic(username=HS_USERNAME, password=HS_PASSWORD)
hs = HydroShare(auth=auth)

g = Github(GITHUB_KEY)

with open('bibfile_small.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)
list_of_journals = populate_collaborations()
author_map = {}
create_journal_edges(author_map, list_of_journals)
create_github_edges(author_map)
create_hydroshare_edges(hs, author_map)
neighbor_map, edges_map = create_neighborhood_map(author_map)
key_list = []
for key in neighbor_map.keys():
    key_list.append(key)

# sort_ratio_dict creates a dictionary like (Name1, Name2) : <val>
# val is the similarity ratio between Name1 and Name2
sort_ratio_dict = {}
for i in range(len(key_list) - 1):
    for j in range(i+1, len(key_list)):
        sort_ratio_dict[(key_list[i], key_list[j])] = fuzz.token_sort_ratio(key_list[i],key_list[j])


# highest is a list of those pair of names that have a token sort ratio greater than 80
highest = [key for key,val in sort_ratio_dict.items() if val > 80]


# Create a consistent name mapping, use the similar names found using fuzzywuzzy string matching, to map all similar
# names to a single name. If any of the values in tuples correspond to usernames (github or hydroshare) then they will
# be dealt using the username_mapping dictionary
name_mapping = {}
for (v1,v2) in highest:
    if v1 not in username_mapping.keys() and v2 not in username_mapping.keys():
        if v1 not in name_mapping.keys() and v2 not in name_mapping.keys():
            name_mapping[v2] = v1

# Equipped with name_mapping and username_mapping, now transform all the values in the neighbor_map 
for key in neighbor_map.keys():
    collabs = neighbor_map[key]
    new_collabs = set()
    for c in collabs:
        if c in name_mapping.keys():
            new_collabs.add(name_mapping[c])
        elif c in username_mapping.keys():
            new_collabs.add(username_mapping[c])
        else:
            new_collabs.add(c)
    neighbor_map[key] = new_collabs

# Now transform all the keys in the neighbor map
neighbor_mapping = {}
for key in neighbor_map.keys():
    val = neighbor_map[key]
    if key in name_mapping:
        new_key = name_mapping[key]
    elif key in username_mapping:
        new_key = username_mapping[key]
    else:
        new_key = key
    if new_key in neighbor_mapping:
        neighbor_mapping[new_key].union(val)
    else:
        neighbor_mapping[new_key] = val

# Modify keys in the edges_map in the same way
edges_mapping = {}
for key in edges_map.keys():
    val = edges_map[key]
    split = key.split("<->")
    if split[0] in name_mapping:
        person1 = name_mapping[split[0]]
    elif split[0] in username_mapping:
        person1 = username_mapping[split[0]]
    else:
        person1 = split[0]

    if split[1] in name_mapping:
        person2 = name_mapping[split[1]]
    elif split[1] in username_mapping:
        person2 = username_mapping[split[1]]
    else:
        person2 = split[1]
    new_key = person1 + "<->" + person2
    
    if new_key in edges_mapping:
        edges_mapping[new_key].append(val)
    else:
        edges_mapping[new_key] = [val]

# Store the neighbor map in a csv file
neighbordf = pd.DataFrame(columns=["Person1", "Person2", "Link", "Collaboration"])

for key in neighbor_mapping.keys():
    neighbor_set = neighbor_mapping[key]
    for neighbor in neighbor_set:
        print(key + "<->" + neighbor)
        link = edges_mapping.get(key + "<->" + neighbor)
        print(link)
        if len(link[0]) == 0 or link is None or link is '':
            continue
        if "github" in link[0]:
            collab = "Github"
        elif "hydroshare" in link[0]:
            collab = "Hydroshare"
        else:
            collab = "Journal"
    neighbordf = neighbordf.append({"Person1": key, "Person2": neighbor, "Link": link, "Collaboration": collab}, ignore_index=True)

neighbordf.to_csv("WHW_edge_collabs.csv")

# Create a csv file for X and Y coordinates

G = nx.Graph()

for key, val in neighbor_mapping.items():
    src = key
    dest_items = val
    for dest in dest_items:
        G.add_node(src)
        G.add_node(dest)
        G.add_edge(src, dest)

pos = nx.layout.fruchterman_reingold_layout(G, center=[20, 20])

name = []
X = []
Y = []
for key in pos:
    val = pos.get(key)
    name.append(key)
    X.append(val[0])
    Y.append(val[1])

df = dict()
df['Name'] = name
df['X'] = X
df['Y'] = Y
data_XY = pd.DataFrame(df)

data_XY.to_csv("WHW_XY.csv")












