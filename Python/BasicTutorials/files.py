#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
#
# with open('/Users/rkitay/tmp/bot/data.json') as f:
#     with open('/Users/rkitay/tmp/bot/output.json', 'w') as w:
#         line_num = 0
#         for line in f:
#             line_num += 1
#             rule_in_line = 0
#             record = json.loads(line)
#             rules = record['rules']
#             for rule in rules:
#                 rule_id = rule['id']
#                 if rule_id.__contains__('BOT-') or rule_id.__contains__('3991'):
#                     rule_in_line += 1
#             if rule_in_line > 1:
#                 # print str(line_num) + ':' + str(rule_in_line) + ':' + line
#                 w.write(line)

with open('/Users/rkitay/Google Drive/Avi/black_list_intermediate_1478806253029.json') as f:
    total = 0
    for line in f:
        line_as_json = json.loads(line)
        print line_as_json['ts']

