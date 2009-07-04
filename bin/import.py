import optparse
import sys

import config
import ingest
from ingesters import friendfeed
from util import ff, json
import persistence

# TODO: de-hardcode friendfeed import
def import_main(options, args):
    if options.flavor == 'friendfeed':
        i = ingest.Ingester(persistence.MongoPersistence())
        flavor_object = friendfeed.FriendFeedInput()
        if options.file is not None:
            result = json.loads(open(options.file, "rb+").read())
        else:
            f = ff.FriendFeedImport(config.friendfeed['username'], config.friendfeed['password'])
            result = f.get_all_home_entries()
        flavor_object.data = result
        i.ingest(flavor_object)
    else:
        print "Not implemented !"

if __name__ == "__main__":

    parser = optparse.OptionParser("usage: %ingest [args]")
    parser.add_option("-w", "--where", dest="flavor",
                  default="friendfeed", type="string",
                  help="where to import the data from")
    parser.add_option("-f", "--file", dest="file",
                  default=None, type="string",
                  help="File for input")
    (options, args) = parser.parse_args()
    print repr(args)
    print repr(options)
    import_main(options, args)

