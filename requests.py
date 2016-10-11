import requests, time
##tcp connection used to communicate with remote server and post data Ray, 
request = requests.get('http://requestb.in/12dhjuy1', data={"Ray":time.time()})

print (request.status_code)
print (request.content)