import json
import time
from steam.guard import MobileWebAuth
from steam.guard import SteamAuthenticator

secrets = json.load(open('./mysecrets.json')) # Load the auth secrets

sa = SteamAuthenticator(secrets) # initialize SteamAuthenticator

timeOne = time.strftime('%H:%M:%S', time.gmtime(sa.get_time()))

codeOne = sa.get_code()
codeTwo = sa.get_code()

while codeOne == codeTwo:
    codeTwo = sa.get_code()

timeOne = sa.get_time()
codeOne = sa.get_code()
codeTwo = sa.get_code()

while codeOne == codeTwo:
    codeTwo = sa.get_code()

timeTwo = sa.get_time()

print('Difference is ' + str(time.strftime('%H:%M:%S', time.gmtime(timeTwo - timeOne))))
print('time 1 is ' + str(timeOne) + ' or ' + str(time.strftime('%H:%M:%S', time.gmtime(timeOne))))
print('time 2 is ' + str(timeTwo) + ' or ' + str(time.strftime('%H:%M:%S', time.gmtime(timeTwo))))
