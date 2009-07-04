import optparse
import sys

import config
import ingest
from ingesters import friendfeed
from util import ff
import persistence

# TODO: de-hardcode friendfeed import
def import_main(options, args):
    if options.flavor == 'friendfeed':
        i = ingest.Ingester(persistence.MongoPersistence())
        flavor_object = friendfeed.FriendFeedInput()
        f = ff.FriendFeedImport(config.friendfeed['username'], config.friendfeed['password'])
        result = f.get_all_home_entries()
        flavor_object.data = result
        i.ingest(flavor_object)
    else:
        print "Not implemented !"

if __name__ == "__main__":

    parser = optparse.OptionParser("usage: %ingest flavor [args]")
    parser.add_option("-f", "--flavor", dest="flavor",
                  default="friendfeed", type="string",
                  help="where to import the data from")
    (options, args) = parser.parse_args()
    import_main(options, args)

