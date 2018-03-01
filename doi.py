import urllib
import requests

api_url = 'http://api.elsevier.com/content/serial/title?'
issn='0309-0566'
const = '&field=dc:title,SJR,SNIP&view=STANDARD&apikey=XXX&httpAccept=application/json'
url = api_url + urllib.parse.urlencode({'issn': issn}) + const
json_data = requests.get(url).json()

title = json_data['serial-metadata-response']['entry'][0]['dc:title']
snip = json_data['serial-metadata-response']['entry'][0]['SNIPList']['SNIP'][0]['$']
sjr = json_data['serial-metadata-response']['entry'][0]['SJRList']['SJR'][0]['$']
print(url)
print(title)
print('SNIP: '+snip)
print('SJR: '+sjr)