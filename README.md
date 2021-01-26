# Json Data Search from input IP address

## Goal
We would like a python script written, with the appropriate unit tests, that will complete the following operations:

    Takes an IP address as a command line argument
    Gets json data from the RIPE network coordination center link
    Use the ['data']['resources']['ipv4'] block in the json above to determine whether the IP provided on the CLI is in any of the CIDRs
    Output a Pass/Fail result based on the presence of the IP address in the CIDR ranges


### Resources
[To check if IP is valid address](https://www.w3resource.com/python-exercises/python-basic-exercise-139.php)
Found this, [ipaddress](https://docs.python.org/3/library/ipaddress.html), for validation instead of socket.