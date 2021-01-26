import sys, logging, json
import requests
import ipaddress


from unittest.main import main

log = logging.getLogger(__name__)

class IPAddress:
    # moved url inside instead as attribute instead of passing it in, since it's static
    url = 'https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix'

    def __init__(self) -> None:
        pass

    # Function to validate if IP is an actual address    
    def validateIP(ipaddr):
        try:
            ip = ipaddress.ip_address(ipaddr)
            print('%s is a correct IP%s address.' % (ip, ip.version))
        except ValueError:
            print('address/netmask is invalid: %s' % ipaddr)
            return False
        except:
            print('Usage : %s  ip' % sys.argv[0])
            return False
        return True

    # Get json response from url
    def getResponse(url):
        operUrl = requests.get(url)
        if(operUrl.status_code==200):
            # Convert to dictionary
            data = operUrl.json()
            with open('data.txt', 'w') as outfile:
                json.dump(data, outfile)

        else:
            print("Error receiving data", operUrl.getcode())
        return data
    
    def searchResponse(response, addy):
        foundIPAddress = response['data']['resources']['ipv4']
        for address in foundIPAddress:
            if address.split('/')[0] == addy:
                print("It's in here: %s" % addy)
            else:
                pass


# Get user input IP address from sys argv
userInput = sys.argv[1] 

# Is IP address valid? If so, search dict for it
if not IPAddress.validateIP(userInput):
    print('Not a valid ip: %s', userInput)
else:
    IPAddress.searchResponse(IPAddress.getResponse(IPAddress.url), userInput)

print('Hello, ' + userInput)




if __name__ == '__main__':
    main

# Function to confirm I can actually test. Still need to write actual tests for real functions, not math function.
# def madd(x,y):
#     return x + y