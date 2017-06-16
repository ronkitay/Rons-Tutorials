#!/usr/bin/python
# -*- coding: utf-8 -*-


import json
from collections import OrderedDict
from sets import Set

# crs_categories = OrderedDict()
# with open ('/Users/rkitay/tmp/padas/1.json') as file_to_load:
#     krs = json.load(file_to_load)
#     rules = krs['rules']
#     for rule in rules:
#         rule_id = rule['ruleId']
#         rule_versions = rule['ruleVersions']
#         max_version = -1
#         max_rule_version = None
#         for rule_version in rule_versions:
#             if int(rule_version['self']['version']) > max_version:
#                 max_rule_version = rule_version
#         risk_score_group = None
#         if len(max_rule_version['riskScoreGroups']) == 1:
#             risk_score_group = max_rule_version['riskScoreGroups'][0]
#         else:
#             for current_risk_score_group in max_rule_version['riskScoreGroups']:
#                 if current_risk_score_group['name'] != 'IN':
#                     risk_score_group = current_risk_score_group
#                     break
#
#         # print risk_score_group
#
#         risk_score_group_name = risk_score_group['name']
#         if risk_score_group_name == "DDOS":
#             risk_score_group_name = "RiskGroups"
#         crs_categories[rule_id] = risk_score_group_name
#
#     risk_score_groups = krs['riskScoreGroups']
#     for risk_score_group in risk_score_groups:
#         risk_score_group_name = risk_score_group['name']
#         if risk_score_group_name == "DDOS":
#             risk_score_group_name = "RiskGroups"
#         risk_score_group_versions = risk_score_group['riskScoreGroupVersions']
#         last_risk_score_group_version = risk_score_group_versions[len(risk_score_group_versions)-1]
#         baseline_group_name = last_risk_score_group_version['baselineGroupName']
#         crs_categories[baseline_group_name] = risk_score_group_name
#
#
# for key, value in crs_categories.iteritems():
#     print '{} = {}'.format(key, value)


# krs_categories = OrderedDict()
# with open ('/Users/rkitay/tmp/padas/41.json') as file_to_load:
#     krs = json.load(file_to_load)
#     rules = krs['rules']
#     for rule in rules:
#         rule_id = rule['ruleId']
#         rule_versions = rule['ruleVersions']
#         max_version = -1
#         max_rule_version = None
#         for rule_version in rule_versions:
#             if int(rule_version['self']['version']) > max_version:
#                 max_rule_version = rule_version
#         risk_score_group = None
#         if len(max_rule_version['riskScoreGroups']) == 1:
#             risk_score_group = max_rule_version['riskScoreGroups'][0]
#         else:
#             for current_risk_score_group in max_rule_version['riskScoreGroups']:
#                 if current_risk_score_group['name'] != 'IN':
#                     risk_score_group = current_risk_score_group
#                     break
#
#         # print risk_score_group
#
#         risk_score_group_name = risk_score_group['name']
#         if risk_score_group_name == "DDOS":
#             risk_score_group_name = "RiskGroups"
#         krs_categories[rule_id] = risk_score_group_name
#
#     risk_score_groups = krs['riskScoreGroups']
#     for risk_score_group in risk_score_groups:
#         risk_score_group_name = risk_score_group['name']
#         if risk_score_group_name == "DDOS":
#             risk_score_group_name = "RiskGroups"
#         risk_score_group_versions = risk_score_group['riskScoreGroupVersions']
#         last_risk_score_group_version = risk_score_group_versions[len(risk_score_group_versions)-1]
#         baseline_group_name = last_risk_score_group_version['baselineGroupName']
#         krs_categories[baseline_group_name] = risk_score_group_name
#
#
# for key, value in krs_categories.iteritems():
#     print '{} = {}'.format(key, value)
#

import json
import os


import csv


def do_round(value):
    if value.startswith('2017'):
        return value
    else:
        return str(int(float(value)))


with open('/Users/rkitay/tmp/NBC/reports/SummaryApr23-1017AM-das-rounded.csv', 'w') as output_file:
    output = csv.writer(output_file)
    with open('/Users/rkitay/tmp/NBC/reports/SummaryApr23-1017AM-das.csv', 'r') as input_file:
        input_csv = csv.reader(input_file)
        for row in input_csv:
            if len(row) > 0 and row[0].startswith('2017'):
                row = map(do_round, row)
                # print row
            # else:
            output.writerow(row)

# output = OrderedDict()
# with open('/Users/rkitay/tmp/nbc-das/das_nbc_1491814800-1hr.csv', 'r') as input_file:
# # with open('/Users/rkitay/tmp/nbc/das_5min_events_by_policy.csv', 'r') as input_file:
#     input_csv = csv.reader(input_file)
#
#     for row in input_csv:
#         if row[0] != 'OK':
#             policy = row[6]
#             count = int(row[13])
#
#             if policy not in output:
#                 output[policy] = 0
#
#             output[policy] += count
#
# keys = sorted(output.keys())
#
# with open('/Users/rkitay/tmp/nbc-das/das_nbc_1491814800-1hr-aggregated.csv', 'w') as output_file:
# # with open('/Users/rkitay/tmp/nbc/das_5min_events_by_policy-aggergated.csv', 'w') as output_file:
#     for key in keys:
#         output_file.write("{},{}\n".format(key, output[key]))
# #

# input_file_name = '/Users/rkitay/work/csi/csi-prod/spark-apps/chewbacca-apps/chewbacca-csi/chewbacca-csi-app-it/src/test/resources/padasawan-test-data/test-data.json'
# input_file_name = '/Users/rkitay/tmp/asnums.json'
# unique_lines = Set()
# data_series = {}
#
# import csv
#
# with open('/Users/rkitay/tmp/asnums.csv', 'w') as output_file:
#     output = csv.writer(output_file)
#     with open(input_file_name, 'r') as input_file:
#         total_egress_count = 0
#         for line in input_file:
#             line_json = json.loads(line)
#             print line_json
#             output.writerow([line_json['asnum'], line_json['ispName']])


        # ts = line_json['epoch']
        # if 1483412400000 <= ts:
        #     distinct_actions = line_json['waf_action'].split(',') # filter(lambda action: action.startswith("2"), line_json['waf_action'].split(','))
        #     total_egress_count = line_json['total_egress_count']
        #     epoc = line_json['epoch']
        #
        #     if epoc not in data_series:
        #         data_series[epoc] = 0
        #
        #     data_series[epoc] += total_egress_count * len(distinct_actions)
            # for action in distinct_actions:
            #     if action not in data_series:
            #         data_series[action] = 0
            #
            #     data_series[action] += total_egress_count
                # print ("{} {}".format(action, total_egress_count))

        # line_json.pop('total_egress_bytes', None)
        # line_json.pop('total_egress_count', None)
        # print(line_json)
        # unique_lines.add(str(line_json))
        # if line_json['deny_rules'] == 'BOT-ANOMALY-HEADER':
        #         if 'BOT-ANOMALY-HEADER' not in data_series:
        #             data_series['BOT-ANOMALY-HEADER'] = 0
        #
        #         total_egress_count = line_json['total_egress_count']
        #
        #         non_deny_rules = line_json['non_deny_rules'].split(':')
        #
        #         data_series['BOT-ANOMALY-HEADER'] += total_egress_count
        #         for ndr in non_deny_rules:
        #             if ndr not in data_series:
        #                 data_series[ndr] = 0
        #             data_series[ndr] += total_egress_count
        #
        #         print line

    # print ("file has {} lines".format(unique_lines.__len__()))
    # print data_series
    #
    # sorted_data_series = []
    # for key, value in data_series.iteritems():
    #     sorted_data_series.append((key, value))
    #
    # sorted_data_series = sorted(sorted_data_series, key=lambda item: item[0])
    # print sorted_data_series


# import json
# import os

# input_file_name = '/Users/rkitay/work/csi/csi-qa/spark-apps/chewbacca-apps/chewbacca-csi/chewbacca-csi-app-it/src/test/resources/padasawan-test-data/test-data.json'
# temp_file_name = '/Users/rkitay/work/csi/csi-qa/spark-apps/chewbacca-apps/chewbacca-csi/chewbacca-csi-app-it/src/test/resources/padasawan-test-data/test-data.json-new'
# with open(input_file_name, 'r') as input:
#     with open(temp_file_name, 'w') as output:
#         index = 0
#         for line in input:
#             line_json = json.loads(line)
#             index += 1
#             if index % 6 == 0:
#                 line_json['content_type'] = 'html'
            # line_json['non_deny_rules'] = 'IPBLOCK'
            # line_json['deny_rules'] = '-'
            # line_json['slow_post_indicator'] = '-'
            # line_json['action'] = 'ALERT'
            # line_json['waf_action'] = '2'
            # if index % 2 == 0:
            #     line_json['non_deny_rules'] = '3900005:981318'
            #     line_json['deny_rules'] = '-'
            #     line_json['slow_post_indicator'] = '-'
            #     line_json['action'] = 'ALERT'
            #     line_json['waf_action'] = '2(monitor),2'
            # if index % 5 == 0:
            #     line_json['non_deny_rules'] = '3900006:3900023:3900037:650093:981173'
            #     line_json['deny_rules'] = 'BOT-ANOMALY-HEADER'
            #     line_json['slow_post_indicator'] = '-'
            #     line_json['action'] = 'DENY'
            #     line_json['waf_action'] = '2(monitor),2(monitor),2(monitor),2,2,3(serve_alt_2082)'
            # if index % 7 == 0:
            #     line_json['non_deny_rules'] = '3900000:3900005:3900006:3900008:3900012'
            #     line_json['deny_rules'] = 'BOT-ANOMALY-HEADER'
            #     line_json['slow_post_indicator'] = 'W'
            #     line_json['action'] = 'DENY'
            #     line_json['waf_action'] = '2(monitor),2(monitor),2(monitor),2(monitor),2(monitor),3(serve_alt_723)}'
            #
#             json.dump(line_json, output)
#             output.write('\n')
#
#
# os.remove(input_file_name)
# os.rename(temp_file_name, input_file_name)





# start_time = 1483401600000
# millis_in_hour = 1000 * 60 * 60
# millis_in_bucket = 1000 * 60 * 5
# for hour in range(2, 14):
#     time = start_time + hour * millis_in_hour
#     for bucket in range (0, 10):
#         offset = bucket * millis_in_bucket
#         bucket_time = time + offset
#         print (bucket_time)
#     print ('done with {}'.format(time))




# import json
# import csv
#
# with open('/Users/rkitay/Desktop/1483610963_97047.csv') as raw_file:
#     with open('/Users/rkitay/Desktop/1483610963_97047_real.csv', 'w') as output_file:
#         output = csv.writer(output_file)
#         for line in raw_file:
#             if line.startswith('"{'):
#                 actual_json_string = line[1:-2].replace('""', '"')
#                 json_obj = json.loads(actual_json_string)
#                 output.writerow([json_obj['st'], json_obj['et'], ';'.join(json_obj['POLICIES']), json_obj['counterId'], json.dumps(json_obj['filter'])])

#
# import json
#
# virginia_ips = json.load(open('/private/tmp/nat-repository.7Vq/virginia'))['nats']
#
# nat_ttls = {}
# for ip in virginia_ips:
#     nat_ttls[ip['ip']] = ip['ts']
#
#
# import time
# millis = int(round(time.time() * 1000))
#
# buckets = [0] * 35
# millis_in_day = 1000 * 60 * 60 * 24
#
# with open('/private/tmp/nat-repository.7Vq/ips_in_virginia_but_not_in_sanjose') as not_in_sj:
#     for ip_not_in_sj in not_in_sj:
#         ip_not_in_sj = ip_not_in_sj.strip()
#         ttl = nat_ttls[ip_not_in_sj]
#         diff = millis-ttl
#         # print (diff)
#         offset_in_days = diff / millis_in_day
#         buckets[offset_in_days] += 1
#
# print (buckets)
#
# buckets_sums = [0] * 35
#
# sum = 0
# for i in range(34, -1, -1):
#     sum += buckets[i]
#     buckets_sums[i] = sum
#
# print (buckets_sums)




#### CSV #####

# import csv
#
#
# not_a_list_yet = [1]
#
# print "not_a_list_yet is of type {0}, Its content is {1}".format(not_a_list_yet.__class__, not_a_list_yet)
#
# not_a_list_yet.append(2)
#
# print "not_a_list_yet is of type {0}, Its content is {1}".format(not_a_list_yet.__class__, not_a_list_yet)
#
#
# f = open('/tmp/ron.csv','w')
# csv_header_writer = csv.DictWriter(f, ['time', 'ip', 'url'], "")
# csv_header_writer.writeheader()
#
# d = dict()
# d["time"] = 'aaa'
# d["ip"] = 'bbb'
# d["url"] = 'ccc'
#
# csv_header_writer.writerow(d)
#
#
#
# csv_writer = csv.writer(f)
# csv_writer.writerow(['hello', 'world', 'this is\na strange thing'])
#
# f.close()

#### REST + JSON Parsing #####
# from sets import Set
#
# VIRGINIA_FLOW_MANAGER = '173.223.226.4'
#
# SAN_JOSE_FLOW_MANAGER = '104.100.164.13'
#
# if __name__ == '__main__':
#
#     import urllib2
#     import json
#     import sys
#
#     # flow_manager_ip = VIRGINIA_FLOW_MANAGER
#     flow_manager_ip = SAN_JOSE_FLOW_MANAGER
#
#     # job_id = 'etp_LookbackEventsJob'
#     # job_id = 'PadawanReplicationMRJob'
#     # job_id = 'PadawanIndexerMRJob'
#     job_id = 'ExporterJob'
#     # job_id = 'NatRepositoryJob'
#
#     time_period = '1day'
#     # time_period = '2hr'
#
#     if sys.argv.__len__() > 1:
#         flow_manager_ip = sys.argv.__getitem__(1)
#
#     if sys.argv.__len__() > 2:
#         job_id = sys.argv.__getitem__(2)
#
#     if sys.argv.__len__() > 3:
#         time_period = sys.argv.__getitem__(3)
#
#     url_template = 'http://{}:8083/flowmanager/rest//monitor/data/instances/history/jobId/{}/timePeriodInDays/{}/list'
#     url = url_template.format(flow_manager_ip, job_id, time_period)
#
#     # url_template = 'http://{}:8083/flowmanager/rest/monitor/job/configuration/jobId/{}/get'
#     # url = url_template.format(flow_manager_ip, job_id)
#
#     print url
#
#     response = urllib2.urlopen(url).read()
#
#     json_response = json.loads(response)
#     print json_response
#     # print 'stopped: %s' % json_response['stopped']
#
#     already_replayed = Set()
#
#     # already_replayed.add(323310)
#     # already_replayed.add(323782)
#     # already_replayed.add(323802)
#     # already_replayed.add(323933)
#     #
#     # print 'already_replayed: %s' % already_replayed
#     #
#     to_replay = []
#
#     for data_instance in json_response['dataInstances']:
#         if data_instance['dataInstanceStatus'] == 'FAILED_AFTER_RETRY':
#             id = data_instance['id']
#             flow_id = data_instance['flowId']
#             if flow_id.__contains__('Pci'):
#                 if id in already_replayed:
#                     print str(id) + " already replayed"
#                 else:
#                     print json.loads(data_instance['error'])['stackTrace']
#                     to_replay.append(id)
#                     print str(id) + " failed for flowID: " + flow_id
#
#     print 'to_replay: %s' % to_replay
#         # metadata = json.loads(data_instance['metadata'])
#         # paths = metadata['additionalDataJsonNode']['heuristicOutputPaths']
#         #
#         # for path in paths:
        #     print path
#
# for num in range(1, 21):
#     print '{ "index": "' + str(num) + '", "ip": "172.24.188.' + str(num + 1) + '"},'
#
# import argparse
#
# parser = argparse.ArgumentParser()
# sub_parsers = parser.add_subparsers(dest='command')
# default_parser = sub_parsers.add_parser('')
# default_parser.add_argument('machineId', metavar='<Machine Id>')
# default_parser.add_argument('machineIndex', metavar='<Machine Index>')
# sub_parsers.add_parser('list')
# sub_parsers.add_parser('envs')
#
# parser.print_help()
#
# args = parser.parse_args(args=['', '1', '2'])
#
# print args



import random

for x in range(1, 21):
    replica1 = chr(65 + random.randint(0, 2))
    replica2 = chr(65 + random.randint(0, 2))
    while replica1 == replica2:
        replica2 = chr(65 + random.randint(0, 2))
    print "{},{},{};{}".format(x, random.randint(1000, 500000), replica1, replica2)

