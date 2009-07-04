from __future__ import with_statement

import time
import datetime
from util import ff
from config import friendfeed

def run_ff_import():
    f = ff.FriendFeedImport(friendfeed['username'], friendfeed['password'])
    result = f.get_all_home_entries()
    with open("dumps_%s" % time.strftime("%Y%m%d%H%M%S", datetime.datetime.now().timetuple()), "wb+") as f:
        f.write(ff.dumps(result, indent=4))

if __name__ == "__main__":
    run_ff_import()

