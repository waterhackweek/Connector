# Connector
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

The Freshwater Waterhackweek Connector is a tool to visualize and summarize connections between researchers in the hydrologic sciences.
This project is currently in the planning and early development phase.

Link to the demonstration [Waterhackweek 2019 visualization](https://public.tableau.com/profile/christina.bandaragoda#!/vizhome/Freshwater_Connector_2019_prototype/Sheet1) on the University of Washington Freshwater website

To run the python code or explore the visualization with NetworkX, click on the badge to launch the Binder software environment.
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/waterhackweek/Connector/master)

## Big picture

The ultimate goal is to produce an interactive network visualization of freshwater scientists. Ideally, it would be similar to the [ERC-citations tool](https://github.com/cns-iu/ERC-Client) hosted on [nanoHUB](https://nanohub.org/erc-citations). It might even make sense to use the ERC tool directly or with some small modifications.

The ERC-citations tool uses a bibtex file input to construct the network. There are positives and negatives to using this approach.

### What works 

- standardized format for Collaborations as a digital object
- can be easily obtained from ORCID
- if web resources like GitHub and Hydroshare have a DOI, then it is easy to include in bibtex

### Known Issues

- any resources that *don't* have an easy bibtex form will have to be translated programmatically to bibtex, which could be difficult to standardize
- it is complicated to include entities like "Waterhackweek" as centralized nodes

## Data

Users' information will be captured through some channel (online form, Waterhackweek application, etc.). This information will include:

- Name
- GitHub username
- ORCID
- HydroShare username

This information will be procured using the respective APIs for Github and Hydroshare, and by parsing through the bibtex file containing journal and paper publications of the WHW participants.

## We welcome feedback in our Github Issues 
Any feedback on the Connector is welcome!
Please post your review on the connector as a Github Issue in the following Q/A format:

- Question 1

Is the visualization intuitive ? Can you interact with all the individual elements ?

- Question 2

Is there anything that is not working as expected?

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

## New Developers: 

1.  Fork, clone, branch  

> git clone https://github.com/waterhackweek/Connector.git

2. You will need a token authorizing your access to the Github repository where you are accessing user data. 

Go to Github Profile. Click through Settings/Developer Settings/Personal Access Token.

Select Scope by checking repo: Full control of private repositories

Generate token

Copy token to file to a safe place NOT in Github directory

3. You will need the HydroShare UserID and Password and Ownership Access to the Group 


## Database

Currently, the data generated for the visualization in Tableau consists of the following tables :

```SQLITE
WHW_XY (Person, X-coordinate, Y-coordinate)
WHW_edge_collabs (Person1, Person2, Link, Collaboration)
```

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/madhasri"><img src="https://avatars0.githubusercontent.com/u/8923832?v=4" width="100px;" alt=""/><br /><sub><b>Madhavi Srinivasan</b></sub></a><br /><a href="https://github.com/waterhackweek/Connector/commits?author=madhasri" title="Code">💻</a> <a href="https://github.com/waterhackweek/Connector/commits?author=madhasri" title="Documentation">📖</a> <a href="#ideas-madhasri" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/Castronova"><img src="https://avatars3.githubusercontent.com/u/4822372?v=4" width="100px;" alt=""/><br /><sub><b>Tony Castronova</b></sub></a><br /><a href="#ideas-Castronova" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://nsf.gov/"><img src="https://avatars3.githubusercontent.com/u/23663503?v=4" width="100px;" alt=""/><br /><sub><b>National Science Foundation</b></sub></a><br /><a href="#financial-nsf-open" title="Financial">💵</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!