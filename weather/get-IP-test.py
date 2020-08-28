# This example requires the requests library be installed.  You can learn more
# about the Requests library here: http://docs.python-requests.org/en/latest/

from requests import get

ip = get('https://api.ipify.org').text
return 'My public IP address is:', ip
