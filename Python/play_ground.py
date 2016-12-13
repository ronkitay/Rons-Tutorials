#!/usr/bin/python
# -*- coding: utf-8 -*-

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
from sets import Set

VIRGINIA_FLOW_MANAGER = '173.223.226.4'

SAN_JOSE_FLOW_MANAGER = '104.100.164.13'

if __name__ == '__main__':

    import urllib2
    import json
    import sys

    # flow_manager_ip = VIRGINIA_FLOW_MANAGER
    flow_manager_ip = SAN_JOSE_FLOW_MANAGER

    # job_id = 'etp_LookbackEventsJob'
    # job_id = 'PadawanReplicationMRJob'
    # job_id = 'PadawanIndexerMRJob'
    job_id = 'ExporterJob'
    # job_id = 'NatRepositoryJob'

    time_period = '1day'
    # time_period = '2hr'

    if sys.argv.__len__() > 1:
        flow_manager_ip = sys.argv.__getitem__(1)

    if sys.argv.__len__() > 2:
        job_id = sys.argv.__getitem__(2)

    if sys.argv.__len__() > 3:
        time_period = sys.argv.__getitem__(3)

    url_template = 'http://{}:8083/flowmanager/rest//monitor/data/instances/history/jobId/{}/timePeriodInDays/{}/list'
    url = url_template.format(flow_manager_ip, job_id, time_period)

    # url_template = 'http://{}:8083/flowmanager/rest/monitor/job/configuration/jobId/{}/get'
    # url = url_template.format(flow_manager_ip, job_id)

    print url

    response = urllib2.urlopen(url).read()

    json_response = json.loads(response)
    print json_response
    # print 'stopped: %s' % json_response['stopped']

    already_replayed = Set()

    # already_replayed.add(323310)
    # already_replayed.add(323782)
    # already_replayed.add(323802)
    # already_replayed.add(323933)
    #
    # print 'already_replayed: %s' % already_replayed
    #
    to_replay = []

    for data_instance in json_response['dataInstances']:
        if data_instance['dataInstanceStatus'] == 'FAILED_AFTER_RETRY':
            id = data_instance['id']
            flow_id = data_instance['flowId']
            if flow_id.__contains__('Pci'):
                if id in already_replayed:
                    print str(id) + " already replayed"
                else:
                    print json.loads(data_instance['error'])['stackTrace']
                    to_replay.append(id)
                    print str(id) + " failed for flowID: " + flow_id

    print 'to_replay: %s' % to_replay
        # metadata = json.loads(data_instance['metadata'])
        # paths = metadata['additionalDataJsonNode']['heuristicOutputPaths']
        #
        # for path in paths:
        #     print path