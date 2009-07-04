from util import lru
import pycurl

@lru_cache(maxsize=10000)
def find_real(short_url):
    conn = pycurl.Curl()
    conn.setopt(pycurl.URL, "http://bit.ly/rgCbf")
    conn.setopt(pycurl.FOLLOWLOCATION, 1)
    conn.setopt(pycurl.CUSTOMREQUEST, 'HEAD')
    conn.setopt(pycurl.NOBODY, True)
    conn.perform()
    a = conn.getinfo(pycurl.EFFECTIVE_URL)
    return a
