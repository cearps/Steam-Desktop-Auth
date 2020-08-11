import json
import steam
import time
import asyncio

config = json.load(open('./input.json')) # Load the config file

# getting auth codes
def get_code():
    output = {"code":"", "timeLeft":0}
    output["code"] = steam.guard.generate_one_time_code(config["shared_secret"])
    output["timeLeft"] = 30 - (int(time.time()) % 30)
    return output

# Client object
class AuthClient(steam.Client):
    async def on_ready(self):
        return


async def get_client():
    global client
    client = AuthClient()
    await client.start(config["username"], config["password"], shared_secret=config["shared_secret"], identity_secret=config["identity_secret"])

async def confirm_finder():
    global confirmations
    fetched = await client._connection._fetch_confirmations()
    confirmations = []
    if fetched: # ensure fetched exists
        for confirmation in fetched.values(): # create list of confirmations with required information
            confirmationID = int(confirmation.id)
            tradeID = confirmation.trade_id
            trade = client.get_trade(tradeID)
            partner = trade.partner
            partnerName = partner.name
            partnerID = partner.id
            itemsSending = []
            for item in trade.items_to_send:
                itemsSending.append(item.name)
            itemsReceiving = []
            for item in trade.items_to_receive:
                itemsReceiving.append(item.name)
            confirmations.append({
                "confirmationID"    :   confirmationID,
                "tradeID"           :   tradeID,
                "partnerName"       :   partnerName,
                "partnerID"         :   partnerID,
                "itemsReceiving"    :   itemsReceiving,
                "itemsSending"      :   itemsSending,
            })
    json.dump(confirmations, open('./out/confirmationFile.json', mode='w'))
    await client.close()

async def get_confirmations():
    await client.wait_until_ready()
    await confirm_finder()

async def confirm_confirmations():
    confirmList = json.load(open('./in/payload.json'))
    await client.wait_until_ready()
    for confirmation in confirmList: # confirm all confirmations in list
        await client._connection.get_and_confirm_confirmation(confirmation["tradeID"])
    await confirm_finder()

async def cancel_confirmations():
    confirmList = json.load(open('./in/payload.json'))
    await client.wait_until_ready()
    for confirmation in confirmList: # cancel all confirmations in list
        trade_id = confirmation["tradeID"]
        confirmation = await client._connection.get_confirmation(trade_id) or await client._connection.fetch_confirmation(trade_id)
        if confirmation is not None:
            await confirmation.cancel()
            return True
    await confirm_finder()
