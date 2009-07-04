import re
import cjson
import datetime

def date_encoder(d):
    assert isinstance(d, datetime.date)
    return 'new Date(Date.UTC(%d,%d,%d))' % (
            d.year, 
            d.month-1, 
            d.day, 
            d.hour, 
            d.minute, 
            d.second
        )
    
re_date=re.compile('^new Date\(.*?\)')

def date_decoder(json_stream, idx):
    json_stream = json_stream[idx:]
    m = re_date.match(json_stream)
    if not m: raise 'cannot parse JSON string as Date object: %s'%json_stream[idx:]
    args = cjson.decode('[%s]' % json_stream[9:m.end() - 2])
    dt = datetime.date(*args)
    return (dt, m.end()) # must return (object, character_count) tuple

def dumps(obj):
    return cjson.encode(obj, extension = date_encoder)

def loads(ioish):
    return cjson.decode(ioish)

