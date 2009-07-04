import optparse
import sys

import config
import ingest
from ingesters import friendfeed
from util import ff, json, short_url
import persistence
from calais import Calais

# TODO: de-hardcode friendfeed import
def calaisify_main(options, args):
    m = persistence.MongoPersistence()
    calais = Calais(config.calais["api_key"], submitter="python-calais demo")
    for d in m.get_non_calaised_entries():
        l = short_url.has(d["title"])
        if len(l):
            for url in l:
                long_url = short_url.find_real(url)
                response = calais.analyze_url(long_url)
                response.print_summary()
                response.print_topics()
                response.print_entities()

        else:
            pass

if __name__ == "__main__":
    calaisify_main(None, None)


