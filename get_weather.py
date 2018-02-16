#!/usr/bin/env python
# coding: utf-8
 
import json
import urllib.request
 
city = "140010"
url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=%s' % city

def translate_condition(telop):
    translated = telop.replace('のち', '->')\
                      .replace('一時', '+')\
                   	  .replace('時々','.')
    return(translated)

def translate_unit(telop):
    translated = telop.replace('晴れ', 'SU')\
                      .replace('晴', 'SU')\
                      .replace('曇り', 'C')\
                      .replace('曇', 'C')\
                      .replace('雨', 'R')\
                      .replace('暴風雨', 'R')\
                      .replace('大雨', 'R')\
                      .replace('雷雨', 'R')\
                      .replace('雪', 'SN')\
                      .replace('大雪', 'SN')\
                      .replace('暴風雪', 'SN')\
                   	  .replace('時々','.')
    return(translated)
 
def main():
    try:
        print('Obtain the content of %s' % url)
        response = urllib.request.urlopen(url)
        weather = json.loads(response.read())
        telop = weather['forecasts'][0]['telop']
        telop = translate_condition(telop)
        telop = translate_unit(telop)
        print(weather['title'] + " : " + telop)
    finally:
        response.close()

if __name__ == '__main__':
    main()

# vim: et ts=4 sw=4 tw=0
