# Freshwater Connect Development Guide

This covers how the project is developed. It should include conventions, development workflow, and other choices that were made in the development.

## Version control for notebooks

This project uses the `jupytext` extension to put Jupyter Notebooks under version control. Whenever the notebook is saved, a copy is also saved as `.py` format that is more appropriate for version control systems. 

The `.ipynb` notebook file extension is added to the `.gitignore` file so that it is not tracked at all by version control. As a result, it is *essential* that any Jupyter Notebooks that should be a part of the main repo use `jupytext`.

## Credentials

Because credentials are so important to all of the API calls, they need to be present in the directory. Here, they are stored in `credentials.py`, which is *not* tracked by version control.

## Name Reconcilation

Since the data for this network was sourced from different sources, Github, Hydroshare and Bibtex files, there was an issue of the same person having multiple names across different data channels. This was done by reconciling the names using the Python [FuzzyWuzzy](https://pypi.org/project/fuzzywuzzy/) package. This package uses [Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance) to figure out how similar two strings are.


## Network Layout Coordinates

To create any network visualization in Tableau, one needs to supply the X and Y coordinates for each node plotted on the network. This is generated using the [Fruchterman Reingold layout](https://en.wikipedia.org/wiki/Force-directed_graph_drawing), using the NetworkX python package.
