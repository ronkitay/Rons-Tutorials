#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv


def is_production(current_row):
    return current_row[2] == "prod"


def is_url_matching(current_row):
    return url_matchers.__contains__(current_row[0]) and current_row[3] == "url"


def is_case_sensitive(current_row):
    return current_row[4] == "yes"


def is_user_agent_matching(current_row):
    return user_agent_matchers.__contains__(current_row[0]) and current_row[3] == "user_agent"


def add_value_to_list(map_of_categories_to_values, the_category, value):
    if the_category.startswith("xss"):
        the_category = 'xss'

    fixed_value = value.replace("[\\]", "[\\\\]")
    if the_category not in map_of_categories_to_values:
        map_of_categories_to_values[the_category] = []
    map_of_categories_to_values[the_category].append(fixed_value)


if __name__ == '__main__':
    url_matchers = ['sqli', 'phpi', 'xss_url', 'pt', 'cmdi', 'rfi', 'javai']
    user_agent_matchers = ['xss_ua']
    url_patterns_case_sensitive = {}
    url_patterns_case_insensitive = {}
    user_agent_patterns_case_insensitive = {}
    d = dict()
    f = file('/Users/rkitay/work/threat-research-team/waf_lite/signatures.txt')
    data = csv.reader(filter(lambda row: row[0] != '#', f), delimiter='\t')
    for row in data:
        if is_production(row):
            if is_url_matching(row):
                if is_case_sensitive(row):
                    add_value_to_list(url_patterns_case_sensitive, row[0], row[1])
                else:
                    add_value_to_list(url_patterns_case_insensitive, row[0], row[1])
            if is_user_agent_matching(row):
                if is_case_sensitive(row):
                    print("missing scenario!!!")
                else:
                    add_value_to_list(user_agent_patterns_case_insensitive, row[0], row[1])
    f.close()

    print ("")
    print ("url.match:")
    print ("  - type: RE2")
    print ("    values:")

    for (category, values) in url_patterns_case_sensitive.iteritems():
        print ("      " + category + ":")
        for case_sensitive_url in values:
            print ("        - '" + case_sensitive_url + "'")

    # print ("")
    # print ("\turl.case.insensitive.match:")
    print ("  - type: RE2")
    print ("    manipulations:")
    print ("      - 'to.lower-case'")
    print ("    values:")
    for (category, values) in url_patterns_case_insensitive.iteritems():
        print ("      " + category + ":")
        for case_insensitive_url in values:
            print ("        - '" + case_insensitive_url.lower().replace("a-za-z", "a-z") + "'")

    print ("")
    print ("user-agent.match:")
    print ("  - type: RE2")
    print ("    manipulations:")
    print ("      - 'to.lower-case'")
    print ("    values:")
    for (category, values) in user_agent_patterns_case_insensitive.iteritems():
        print ("      " + category + ":")
        for case_insensitive_user_agent in values:
            print ("        - '" + case_insensitive_user_agent + "'")

