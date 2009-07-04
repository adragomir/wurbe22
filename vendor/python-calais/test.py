from calais import Calais
API_KEY = "jw7hufwvybrh6twq4g86aqnx"
calais = Calais(API_KEY, submitter="python-calais demo")
result = calais.analyze_url("http://www.nytimes.com/2009/04/04/business/media/04globe.html?_r=1")
print repr(result)
result.print_summary()
result.print_topics()
result.print_entities()
