import requests

#request access the Api code of a website
def http_request(url):
    res = requests.get(url)
    return res

# return True if the status of the website passed 200-399 and False if Failed 400-599
def status(request_url):
    if 200 <= request_url.status_code <400:
        print(f'Success : {request_url.status_code}')
        return True
    else:
        print(f'FAILED : {request_url.status_code}')
        return False
    