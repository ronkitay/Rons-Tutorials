#!/usr/bin/python
# -*- coding: utf-8 -*-

import json


# accounts_with_rep = ['F-AC-1701057','B-C-VT1OY3','F-AC-1306207','F-AC-1123105','B-3-U3XNPI','1-7KLGH','1-NQHFLD','B-C-CD9KFR','B-3-13H55AH','QR-J-5M','AANA-5CUS4I','B-3-13H55AH','F-AC-557747','1-H78TP','F-AC-186160','1-9UFO','1-JAEV0','1-CLRTV','B-C-12O9DLO','B-C-CCUBM9','1-3CROXB','1-6YZCR','B-3-12GK32M','1-6BQBFH','B-C-VT1OY3','B-C-C8KEVD','B-C-CCUBMO','B-C-A13AGL','B-C-CCUBMO','1-3W9XZT','1-BGIGR','F-AC-1730810','1-6BQBFH','1-CXB3','1-RAJNHT','1-HV7K1','B-C-CD9KFR','B-C-CCUBM9','B-3-U3XNPI','AANA-3V70K6']
# result = ''
# counter = 0
# with open('/Users/rkitay/tmp/all_customers.json') as data_file:
#         all_accounts = json.load(data_file)
#
#         for account in all_accounts:
#             if account['accountId'] in accounts_with_rep:
#                 # result = result + str(account['configVersionId']) + "\n"
#                 result = result + str(account['configId']) + "\n"
#                 counter+=1
# print result
#
# print counter

with open ('/Users/rkitay/work/prodo/prodo-dev/hdfs/akamai/csi/reputation/heuristic-overrides.json') as heuristic_overrides:
    heuristics = json.load(heuristic_overrides)['heuristics']
    active_heuristics = list()
    for heuristic, heuristic_conf in heuristics.iteritems():
        if heuristic_conf['status'] == 'ACTIVE':
            active_heuristics.append( (heuristic, heuristic_conf) )

    active_heuristics.sort(key=lambda tup: tup[0])

    for active_heuristic in active_heuristics:
        print active_heuristic

    # for heuristic, heuristic_conf in heuristics.iteritems():
