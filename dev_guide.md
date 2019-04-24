# Freshwater Connect Development Guide

This covers how the project is developed. It should include conventions, development workflow, and other choices that were made in the development.

## Version control for notebooks

This project uses the `jupytext` extension to put Jupyter Notebooks under version control. Whenever the notebook is saved, a copy is also saved as `.py` format that is more appropriate for version control systems. 

The `.ipynb` notebook file extension is added to the `.gitignore` file so that it is not tracked at all by version control. As a result, it is *essential* that any Jupyter Notebooks that should be a part of the main repo use `jupytext`.

## Credentials

Because credentials are so important to all of the API calls, they need to be present in the directory. Here, they are stored in `credentials.py`, which is *not* tracked by version control.
