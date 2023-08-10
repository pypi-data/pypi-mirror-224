import requests
import json
import sys
import os

node_base_url = "http://localhost:3000"
    
def get_url_to_html(url):
    request_url = node_base_url + "/convert?url="+url
    response = requests.get(request_url)
    res = json.loads(response.text)
    if ('message' in res):
        return  sys.stderr.write(res['message'])
    else :
        return res
    
def url_to_filename(url):
    # Remove protocol and split by '/'
    parts = url.split('//')[-1].split('/')
    
    # Remove any query parameters or fragments
    parts[-1] = parts[-1].split('?')[0]
    parts[-1] = parts[-1].split('#')[0]
    
    # Join parts with underscores
    filename = '_'.join(parts)
    
    return filename


def store_txt_html(input, ouptut):
    try:
        if not os.path.exists(ouptut):
            os.makedirs(ouptut)
        with open(input, 'r') as file:
            if(file):
                contents = file.read()
                urls = contents.split("\n")
                for url in urls:
                    htmlFile =  get_url_to_html(url) 
                    with open(ouptut+'/' +(url_to_filename(url)) + '.html', "w", encoding='utf-8') as file:
                        # utf8_bytes = htmlFile["html"].encode('utf-8', errors='ignore')
                        # htmlFile["html"] = utf8_bytes.decode('utf-8')
                        if(htmlFile["html"]):
                            file.write( htmlFile["html"])
                return { "success" : True , "message" : "Processed successfully." }
            else:
                return { "success" :  False , "message" : "File not exist." }
    except Exception as e:
        return e


print(store_txt_html('test.txt','html5'))

