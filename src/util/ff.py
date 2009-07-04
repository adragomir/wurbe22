from __future__ import with_statement

import sys
sys.path.append("./vendor/friendfeed-api/python")
import friendfeed
import simplejson as json
import datetime
import time
import re


__jsdateregexp__ = re.compile(r'"\*\*(new Date\([0-9,]+\))"')
class __JSONDateEncoder__(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return time.mktime(obj.timetuple())
        if isinstance(obj, datetime.date):
            return time.mktime(obj.timetuple())
        return json.JSONEncoder.default(self, obj)

def dumps(obj, *args, **kwargs):
    """ A (simple)json wrapper that can wrap up python datetime and date
    objects into Javascript date objects.
    @param obj: the python object (possibly containing dates or datetimes) for
        (simple)json to serialize into JSON

    @returns: JSON version of the passed object
    """
    return __jsdateregexp__.sub(r'\1', json.dumps(obj, cls=__JSONDateEncoder__, indent=4))


class FriendFeedImport(object):
    def __init__(self, nickname, remotekey):
        self.session = friendfeed.FriendFeed(nickname, remotekey)

    def get_all_home_entries(self):
        start = 0
        num = 100
        get_more = True
        all_entries_now = []
        while get_more == True:
            print "getting entries starting at %d" % start
            result = self.session._fetch_feed("/api/feed/home", start=start, num=num)
            entries = result.get("entries", [])
            all_entries_now += entries
            how_many = len(entries)
            print "got ... %d entries" % how_many 
            if how_many == num:
                start += num
                get_more = True
            else:
                get_more = False
            get_more = False
        return all_entries_now
