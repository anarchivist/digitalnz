#!/usr/bin/env python

# Copyright (C) 2009 Philip Lindsay
#
# This file is part of the digitalnz Python module.
#
# digitalnz is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# digitalnz is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with digitalnz.  If not, see <http://www.gnu.org/licenses/>.

# examples/digitalnz_search.py - sample commandline app to search DigitalNZ

import sys

import digitalnz

if __name__ == "__main__":
    try:
        search_term = sys.argv[1]
    except IndexError:
        print "Usage: %s <search_term>" % sys.argv[0]

    dnz = digitalnz.request.DigitalNZAPI(api_key="<insert_api_key_here>")
    results = dnz.search(search_text=search_term)

    data = results.data

    print "Results found:", data['result_count']

    for result in data['results']:
        print result['title']
        print result['display_url']
        print
