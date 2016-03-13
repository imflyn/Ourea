from django.core.context_processors import csrf
from django.shortcuts import render_to_response
import urllib, urllib2
import time
import json
import traceback


def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('step.html', c)


def help(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('help.html', c)


def submit(request):
    try:
        id = request.POST['id']
        steps = request.POST['steps']
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        keycontentjson = [
            {
                "date": time.time(),
                "calories": 0,
                "activeValue": 3256,
                "steps": steps,
                "pm2d5": 0,
                "duration": 0,
                "distance": 0,
                "report": "[]"
            }
        ]
        list = json.dumps(keycontentjson)
        url = "http://pl.api.ledongli.cn/xq/io.ashx"
        parameters = {'action': 'profile',
                      'pc': 'c7ab7103335374f968af2974577ad899a393cb',
                      'cmd': 'updatedaily',
                      'uid': id,
                      'list': list,
                      }
        data = urllib.urlencode(parameters)
        request = urllib2.Request(url, data)
        for key in headers:
            request.add_header(key, headers[key])
        urllib2.urlopen(request)
    except:
        traceback.print_exc()
        return render_to_response("../../ourea/templates/500.html")
        pass
    return render_to_response('success.html')
