import requests

url = 'http://mobile-app.dinglc.com'

service = '/ADPlatformCallbackApi/filterJudian'

result = requests.request('get','{}{}?idfa={}'.format(url, service,'FFFFD02A-B931-4833-87E3-A41E98126185') )

print('{}{}?idfa={}'.format(url, service,'FFFFD02A-B931-4833-87E3-A41E98126185'))