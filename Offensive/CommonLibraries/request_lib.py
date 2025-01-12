import requests
from requests.auth import HTTPBasicAuth

URL = "https://httpbin.org"

def basic_get():
    response = requests.get(f"{URL}/get")
    print(response.status_code) # print status code

    with open("response.html", "w") as f:
        ...
        #f.write(response.text) # for source code

def more_specific():
    
    values = {'key': 'value', 'key2': 'value2'}
    headers = {'User-Agent': 'Test123'} # might as well change the user agent

    # timeout for raising an error if the response exceeds the time set (in seconds)

    try:
        response2 = requests.get(f"{URL}/get", params=values, headers=headers, timeout=2)
        data = response2.json()  # if a json is yield
        response2.raise_for_status()

    except requests.Timeout:
        print("Time out!")
        
    except requests.HTTPError as err:
        print(f"Nice error: {err}")
        
    except requests.RequestException as err:
        print(f"Error!: {err}")
    else: 
        print("Success!")
        print(f"headers:{response2.request.headers}")
        print(f"URL GET:{response2.url}")
        print(f"source code:{response2.text}")
        
        if 'headers' in data and 'User-Agent' in data['headers']:
            print(f"json: {data['headers']['User-Agent']}")

# using website (post)

def post():
    
    values = {'key': 'value', 'key2': 'value2'}
    payload = values
    response3 = requests.post(f"{URL}/post", data = payload)
    print(f"URL POST:{response3.url}")
    print(f"source code:{response3.text}")

# https://httpbin.org/basic-auth/foo/bar For autentication

def basic_auth(): 
    response4 = requests.get(f"{URL}/basic-auth/foo/bar", auth=HTTPBasicAuth('foo', 'bar')) # auth = (username, pass)
    print(f"Auth response: {response4.text}")

# https://httpbin.org/cookies

def cookies():
    cookies = dict(cookies_are = "working")
    response5 = requests.get(f"{URL}/cookies", cookies=cookies).json()
    print(f"Cookies response: {response5}")

# Uploading files

def uploading_files():
    my_file = {'file': open('ex.txt', 'r')}
    response6 = requests.post(f"{URL}/post", files=my_file)
    print("response 6:", response6.text)

# Playing with session cookies, when it comes to authentication and sessions

def session_cookies():
    set_cookies_url = f"{URL}/cookies/set/my_cookie/cookie_value"
    s = requests.Session()
    response7 = s.get(set_cookies_url)
    print("response 7:", response7.text)
    response7 = s.get(f"{URL}/cookies")
    print("response 7:", response7.text)

# Preparing requests

def preparing_request():
    headers = {'Custom': 'Test123'}
    s = requests.Session()
    req = requests.Request('GET', f"{URL}/get", headers=headers)
    
    # preparing the requests
    prepped = req.prepare()
    
    #set the new headers
    prepped.headers['User-Agent'] = 'Silv'
    
    # add new header
    prepped.headers['New-Header'] = "Pepega Header"
    
    #send the request
    response = s.send(prepped)

    print("response 8:", response.text)
    
# Redirecting logs

def redirect():
    url = "http://github.com"
    response1 = requests.get(url, allow_redirects=False)    
    print("response 9:", response1.url)
    
    # logs of all domains traveled
    response2 = requests.get(url)
    for request in response2.history:
        print("\n[+] Domains:", request.url)
    print("last url:", response2.url)
    
# Sessions using with

def session_with():
    
    with requests.Session() as session:
        
        # crearing session upon logging in
        session.auth = ('silv', 'silv123')
        response1 = session.get(f"{URL}/basic-auth/silv/silv123")
        print("auth1:", response1.text)
        
        response2 = session.get(f"{URL}/basic-auth/silv/silv123")
        print("auth2:", response2.text)


if __name__ == "__main__":
    basic_get()
    more_specific()
    post()
    basic_auth()
    cookies()
    uploading_files()
    session_cookies()
    preparing_request()
    redirect()
    session_with()

