#!/usr/bin/python
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    import urllib2
    import json
    import sys

    flow_manager_ip = '104.100.164.13'

    if sys.argv.__len__() > 1:
        flow_manager_ip = sys.argv.__getitem__(1)

    url_template = 'http://{}:8083/flowmanager/rest//monitor/data/instances/history/jobId/AccountIndustryMappingJob/timePeriodInDays/1hr/list'
    url = url_template.format(flow_manager_ip)
    print url

    response = urllib2.urlopen(url).read()

    json_response = json.loads(response)

    for data_instance in json_response['dataInstances']:
        if data_instance['dataInstanceStatus'] == 'SKIP':
            print "SKIPPED !!!! %s" % data_instance
        else:
            print "ALL GOOD !!!! %s" % data_instance
