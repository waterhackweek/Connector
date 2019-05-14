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

# # ORCID API connections

import orcid
import credentials as cred

api = orcid.PublicAPI(cred.ORCID_CLIENT_ID, cred.ORCID_CLIENT_SECRET, sandbox=True)
search_token = api.get_search_token_from_orcid()
search_token

search_results = api.search('orcid:0000-0003-3768-4277', access_token=search_token)


