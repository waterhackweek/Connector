# Connector

The Freshwater Waterhackweek Connector is a tool to visualize and summarize connections between researchers in the hydrologic sciences.

This project is currently in the planning and early development phase.
Link to the visualization : https://public.tableau.com/profile/christina.bandaragoda#!/vizhome/Freshwater_Connector_2019_prototype/Sheet1

## Big picture

The ultimate goal is to produce an interactive network visualization of freshwater scientists. Ideally, it would be similar to the [ERC-citations tool](https://github.com/cns-iu/ERC-Client) hosted on [nanoHUB](https://nanohub.org/erc-citations). It might even make sense to use the ERC tool directly or with some small modifications.

The ERC-citations tool uses a bibtex file input to construct the network. There are positives and negatives to using this approach.

### Positives

- standardized format
- can be easily obtained from ORCID
- if web resources like GitHub and Hydroshare have a DOI, then it is easy to include in bibtex

### Negatives

- any resources that *don't* have an easy bibtex form will have to be translated programmatically to bibtex, which could be difficult to standardize
- makes it more complicated to include entities like "Waterhackweek" as centralized nodes

## Data

Users' information will be captured through some channel (online form, Waterhackweek application, etc.). This information will include:

- Name
- GitHub username
- ORCID
- HydroShare username

This information will be procured using the respective APIs for Github and Hydroshare, and by parsing through the bibtex file containing journal and paper publications of the WHW participants.

## Issues
Any feedback on the Connector is welcome!
Please post your review on the connector as a Github Issue in the following Q/A format:

- Question 1

Is the visualization intuitive ? Can you interact with all the individual elements ?

- Question 2

Is there something that is not working ?

- Question 3

Any suggestions that can enhance the visualization ?


### GitHub username

GitHub has a fully-featured API that should allow for the following information to be retrieved for any given user:

- public repos that they own
- public repos that they have contributed to
- public GitHub organizations they belong to
- other contributors to public repos they own
- other contributors to public repos they have contributed to
- other members of the GitHub organizations they belong to
- ...more

There are a number of Python wrappers for the GitHub API ([https://developer.github.com/v3/libraries/](https://developer.github.com/v3/libraries/)). It is probably best to use one of these as it should be easier to maintain than using the raw JSON returned by a lower-level library like `requests`.

### ORCID

Like GitHub, ORCID already has a public API that can be queried with Python. There is even a [Python wrapper for the ORCID API](https://github.com/ORCID/python-orcid) that should make things easier.

However, ORCID requires user permission, even for read-only

### HydroShare

HydroShare also has an API and a [Python client](https://hs-restclient.readthedocs.io/en/latest/) that will allow for easier extraction of a user's HydroShare Resources and collaborators.

### Paper Publications

Most of the paper and journal publications are present in the form of bibtex files, which can be easily parsed using the [Bibtexparser](https://bibtexparser.readthedocs.io/en/master/). 

## Database

Currently, the data generated for the visualization in Tableau consists of the following tables :

```SQLITE
WHW_XY (Person, X-coordinate, Y-coordinate)
WHW_edge_collabs (Person1, Person2, Link, Collaboration)
```
