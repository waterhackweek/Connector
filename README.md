# Freshwater Connect

Freshwater Connect is a tool to visualize and summarize connections between researchers in the hydrologic sciences.

This project is currently in the planning and early development phase.

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

## Data flow

Users' information will be captured through some channel (online form, Waterhackweek application, etc.). This information will include:

- Name
- GitHub username
- ORCID
- HydroShare username

These inputs should be stored in a database table for `Users`. The usernames can be used to make API calls to GitHub, ORCID, and HydroShare to retrieve further information.

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

Like GitHub, ORCID already has a public API that can be queried Python. There is even a [Python wrapper for the ORCID API](https://github.com/ORCID/python-orcid) that should make things easier.

### HydroShare

HydroShare also has an API and a [Python client](https://hs-restclient.readthedocs.io/en/latest/) that will allow for easier extraction of a user's HydroShare Resources and collaborators.