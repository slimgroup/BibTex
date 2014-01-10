#!/usr/bin/python

import fileinput
import re

monthContainers = [
        r'\s*month\s*=',
        r'\s*optmonth\s*='
]

month_full_string = [
        'January', 'February', 'March', 'April', 'May', 'June', 'July',
        'August', 'September', 'October', 'November', 'December'
]

month_three_string = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

month_int = range(1,13) # number for months in the year, prob won't need

month_int_string = [
        '01', '02', '03', '04', '05', '06',
        '07', '08', '09', '10', '11', '12'
]

month_int_string_alt = [
        '1', '2', '3', '4', '5', '6',
        '7', '8', '9', '10', '11', '12'
]

countMonth = 0
count_full = 0
count_int_string = 0
count_int_string_alt = 0

month_key_debug = []
optmonth_debug = []
for line in fileinput.input(inplace=1):
    for monthContainer in monthContainers:
        if re.match(monthContainer,line,re.I):
            # convert
            countMonth += 1
            month_in_container = \
                re.search(
                        r'[\{][\s]*([^\s\/\}]+)[^\s]*[\s]*[\}]*',
                        line,re.I).group(1)
                # This basically fetches anything in between the braces.
            full_string = False
            three_string = False
            optmonth_debug.append(month_in_container)
            for key, month in enumerate(month_full_string):
                if month == month_in_container:
                    count_full += 1
                    full_string = True
                    line = "  month = {{{month}}},\n".format(month=month_int_string[key])
                    month_key_debug.append((fileinput.lineno(),line,month_in_container))
            if not(full_string):
                for key, month in enumerate(month_three_string):
                    if month == month_in_container:
                        count_int_string += 1
                        int_string = True
                        line = \
                            "  month = {{{month}}},\n".format(month=month_int_string[key])
                        month_key_debug.append((fileinput.lineno(),line,month_in_container))
            if (not(three_string) and not(full_string)):
                for key, month in enumerate(month_int_string_alt):
                    if month == month_in_container:
                        count_int_string_alt += 1
                        line = \
                            "  month = {{{month}}},\n".format(month=month_int_string[key])
                        month_key_debug.append((fileinput.lineno(), line,month_in_container))
            for key, month in enumerate(month_int_string): # this is for the MM/YYYY stuff
                if month == month_in_container:
                    count_int_string_alt += 1
                    line = \
                        "  month = {{{month}}},\n".format(month=month_int_string[key])
                    month_key_debug.append((fileinput.lineno(), line,month_in_container))
    print line, # comma is there to prevent double linebreak
fileinput.close()
# print ("Found {} month instances".format(countMonth))
# print count_full, count_int_string, count_int_string_alt
# print month_key_debug
print optmonth_debug
