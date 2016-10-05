#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
Python considers any map or collection as JSON elements. 'Serializing/DeSerializing' them is VERY easy
Read:
 - json.load(data_file) --> Loads an object from a File
 - json.loads(json_as_string) --> Loads an object from a string representing a JSON object
Write:
 - json.dump(json_object, target_file) --> Saved te object into the file
 - json.dumps(json_object) --> Returns the JSON Object in its String representation
"""
import json

from sets import Set

phase = 0


def load_json_from_file(input_file_name):
    with open(input_file_name) as data_file:
        return json.load(data_file)


def save_json_to_file(output_file, json_object):
    with open(output_file, 'w') as outfile:
        json.dump(json_object, outfile)


def print_json_object(json_object):
    print json.dumps(json_object, indent=True, sort_keys=True)


def print_phase():
    global phase
    print '==== Step %d ====' % phase
    phase += 1


tor_details_full_list = load_json_from_file('/Users/rkitay/tmp/tor2/tor_details_full.json')

relays = tor_details_full_list["relays"]
output = Set()

for relay in relays:
    exit_policy = relay["exit_policy"]
    if exit_policy[0] == "reject *:*":
        continue
    # print relay["nickname"]
    if "or_addresses" in relay:
        or_addresses = relay["or_addresses"]
        # print or_addresses
        for ip in or_addresses:
            if '.' in ip:
                ip = ip[0:ip.index(':')]
                output.add(ip)
    if "exit_addresses" in relay:
        exit_addresses = relay["exit_addresses"]
        # print exit_addresses
        for ip in exit_addresses:
            if '.' in ip:
                output.add(ip)

print "all tor addresses size is: " + str (output.__len__())
print output

check_tor_file = open("/Users/rkitay/tmp/tor2/check-tor.ips", "r")
check_tor_lines = check_tor_file.readlines()

for check_tor_ip in check_tor_lines:
    if check_tor_ip in output:
        continue
        # print check_tor_ip + " was found in the onionoo list"
    else:
        print check_tor_ip + " was NOT found in the onionoo list"

# print_phase()
# print type(data)  # Data is a dictionary
# print data
#
# print_phase()
# data['object1']['field2'] = 'new value'
# print data
#
# print_phase()
# data['object2'] = {'fieldX': 'valueY', 'fieldZ': 12940.43}
# print_json_object(data)
#
# print_phase()
# if 'object3' not in data:
#     data['object3'] = {}
# print_json_object(data)
#
# print_phase()
# if 'object2' not in data:
#     data['object2'] = {}
# else:
#     data['object2']['fieldZ'] = 96943.34
# print_json_object(data)
#
# print_phase()
# dummy_json_output_file = '/tmp/dummy_output.json'
# save_json_to_file(dummy_json_output_file, data)
# contents_of_file_i_just_saved = load_json_from_file(dummy_json_output_file)
# print_json_object(contents_of_file_i_just_saved)
#
# print_phase()
# sample_data = [
#     {"action": "Allow", "key": "ALLOW", "rules": 20},
#     {"action": "Alternate Content", "key": "ALT_CONT", "rules": 20},
#     {"action": "Alternate Origin", "key": "ALT_ORG", "rules": 20},
#     {"action": "Get from Cache", "key": "CACHE", "rules": 20},
#     {"action": "Annoy user", "key": "CUSTOM_1234", "rules": 20},
#     {"action": "Distract user", "key": "CUSTOM_5678", "rules": 20},
#     {"action": "Delay the user", "key": "DELAY", "rules": 20},
#     {"action": "DROP", "key": "DROP", "rules": 20},
#     {"action": "Do nothing", "key": "NONE", "rules": 20},
#     {"action": "Slow the user", "key": "SLOW", "rules": 20}
# ]
# print type(sample_data)
# print_json_object(sample_data)
#
# print_phase()
# sample_data[1:3] = []
# print_json_object(sample_data)
