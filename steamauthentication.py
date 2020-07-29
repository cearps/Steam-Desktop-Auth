import json
from steam.guard import MobileWebAuth
from steam.guard import SteamAuthenticator

secrets = json.load(open('./mysecrets.json')) # Load the auth secrets

sa = SteamAuthenticator(secrets) # initialize SteamAuthenticator

# \/ useful for later on when sending/receiving trade offers
# https://gyazo.com/2871ec76774ad22ed301daf8f4a66351
# /\ useful for later on when sending/receiving trade offers

def get_code():
    return sa.get_code()

def get_time():
    return sa.get_time()

def list_confirmations():
    return sa.generate_confirmation_key(tag='conf')

def get_details(time_stamp):
    return sa.generate_confirmation_key(tag='details', timestamp=time_stamp)

def accept_confirmation(time_stamp):
    return sa.generate_confirmation_key(tag='allow', timestamp=time_stamp)

def decline_confirmation(time_stamp):
    return sa.generate_confirmation_key(tag='cancel', timestamp=time_stamp)
