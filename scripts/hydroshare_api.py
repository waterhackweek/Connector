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

# imports
import credentials as cred
from hs_restclient import HydroShare, HydroShareAuthBasic

auth = HydroShareAuthBasic(username=cred.HS_USERNAME, password=cred.HS_PASSWORD)
hs = HydroShare(auth=auth)

for res in hs.resources(creator="ChristinaBandaragoda", public=True):
    print(res['authors'])

ct_user = 0
for res in hs.resources(creator="ChristinaBandaragoda", public=True):
#     print(res['resource_id'])
    ct_user += 1

ct_user


