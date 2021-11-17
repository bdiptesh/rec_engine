#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 06:41:30 2021

@author: ravi.kolluri
"""

from lib.rec_engine import Recommendation, pd  # pylint: disable=E0401
df_catalog = pd.read_csv("../data/input/catalog.csv")
df_uid = pd.read_csv("../data/input/users.csv")
reco = Recommendation(df_catalog, df_uid, 3)
final_recommendation = reco.rec()