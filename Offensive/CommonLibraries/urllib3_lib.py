import urllib3
import json

#urllib3.disable_warnings(urllib3.exceptions.InsecurePlatformWarning)

HTTP = urllib3.PoolManager() # Define connection handler
# HTTP = urllib3.PoolManager(cert_reqs = 'CERT_NONE') Define connection handler, and ignore SSL signature
URL = "https://httpbin.org"

def get():
    response = HTTP.request(
        'GET', 
        f'{URL}/get'
    )
    print(response.data.decode())    
    
def post():
    data = {'key': 'value'}
    encoded_data = json.dumps(data).encode() #turn dict into a json string
    
    # U can either specify body or fields, but not both
    response = HTTP.request(
        'POST',
        f'{URL}/post',
        body = encoded_data,
        headers = {'Content-Type': 'application/json'}
    ) #when it comes to json data
    response2 = HTTP.request(
        'POST',
        f'{URL}/post',
        fields = data
    )
    print(response.data.decode()) 
    print(response2.data.decode())
    
def headers():
    response = HTTP.request(
        'GET',
        f'{URL}/get',
        headers={'New-Header': 'Content'})
    print(response.data.decode())
    
def redirect():
    response = HTTP.request(
        'GET',
        f'{URL}/redirect/1',
        redirect = False
    )
    print(response.status) # status code
    #print(dir(response)) printing all attributes
    print(response.get_redirect_location()) # prints the destination
    
def ssl_signature():
    response = HTTP.request(
        'GET', 
        'https://54.162.208.243', 
        redirect = False
    )
    print(response.data.decode())
    
if __name__ == "__main__":
    get()
    post()
    headers()
    redirect()
    ssl_signature()
    