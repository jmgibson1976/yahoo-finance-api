import json
import os

file_name = 'finance.yahoo.com.har.json'
file      = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".." + os.sep + "..", file_name)

with open(file) as datafile:
    data = json.load(datafile)

    # loop entries node
    for entry in data['log']['entries']:
        
        # set some common variables
        url: str = entry['request']['url']
        method: str = entry['request']['method']

        # exclusions
        if method == 'GET' \
            and url.find('video.') == -1 \
            and url.find('video-api.') == -1 \
            and url.find('edgecast-vod') == -1 \
            and url.find('edgecast-cf-prod') == -1 \
            and url.find('yahoodns') == -1 \
            and url.find('media.') == -1 \
            and url.find('innovid.') == -1 \
            and url.find('googlesyndication') == -1 \
            and url.find('guce.yahoo.com') == -1 \
            and url.find('.js') == -1 \
            and url.find('wss:') == -1 \
            and url.find('geo.') == -1 \
            and url.find('udc.') == -1 \
            and url.find('.html') == -1 \
            and url.find('.css') == -1 \
            and url.find('.svg') == -1 \
            and url.find('.png') == -1 \
            and url.find('.jpg') == -1 \
            and url.find('.yimg') == -1 \
            and url.find('.woff2') == -1 \
            and url.find('.gif') == -1 \
            and url.find('adcount') == -1 \
            and url.find('scorecardresearch') == -1:
            
            # print remaining urls
            print(f'{method}: {url}')
            print('')