import json
import steamauthentication as sa
from quart import Quart, render_template, jsonify, request
from quart.utils import run_sync
import asyncio
from werkzeug.datastructures import MultiDict

# quart app
app = Quart(__name__)

@app.route("/")
async def index():
        TFA = sa.get_code()
        return await render_template('index.html', code=TFA["code"], timeLeft=TFA["timeLeft"])

@app.route('/_get_code/')
def _get_code():
    TFA = sa.get_code()
    return jsonify({
        "code"      : TFA["code"],
        "timeLeft"  : TFA["timeLeft"]
    })

async def _load_confirmations():
    task1 = asyncio.create_task(sa.get_client())
    task2 = asyncio.create_task(sa.get_confirmations())
    await asyncio.gather(task1, task2)

@app.route('/_send_confirmations/')
async def _send_confirmations():
    await _load_confirmations()
    confirmations = json.load(open('./out/confirmationFile.json'))
    if len(confirmations) == 0:
        return "<p>No confirmations found.</p>"
    else:
        output = ""
        for c in confirmations:
            lengths = {"sendLength": len(c["itemsSending"]), "receiveLength": len(c["itemsReceiving"])}
            output += await render_template("confirmation.html", confirmation=c, lengths = lengths)
        return output

async def _load_accept():
    taska = asyncio.create_task(sa.get_client())
    taskb = asyncio.create_task(sa.confirm_confirmations())
    await asyncio.gather(taska, taskb)

@app.route('/_accept_confirmations/', methods=["POST"])
async def _accept_confirmations():
    data = await request.form
    dictionary = data.to_dict(flat = False)
    payload = []
    for item in dictionary["data[]"]:
        payload.append({"tradeID": int(item)})
    json.dump(payload, open('./in/payload.json', mode='w'))
    await _load_accept()
    confirmations = json.load(open('./out/confirmationFile.json'))
    if len(confirmations) == 0:
        return "<p>No confirmations found.</p>"
    else:
        output = ""
        for c in confirmations:
            lengths = {"sendLength": len(c["itemsSending"]), "receiveLength": len(c["itemsReceiving"])}
            output += await render_template("confirmation.html", confirmation=c, lengths = lengths)
        return output

async def _load_cancel():
    taskc = asyncio.create_task(sa.get_client())
    taskd = asyncio.create_task(sa.cancel_confirmations())
    await asyncio.gather(taskc, taskd)

@app.route('/_cancel_confirmations/', methods=["POST"])
async def _cancel_confirmations():
    data = await request.form
    dictionary = data.to_dict(flat = False)
    payload = []
    for item in dictionary["data[]"]:
        payload.append({"tradeID": int(item)})
    json.dump(payload, open('./in/payload.json', mode='w'))
    await _load_cancel()
    confirmations = json.load(open('./out/confirmationFile.json'))
    if len(confirmations) == 0:
        return "<p>No confirmations found.</p>"
    else:
        output = ""
        for c in confirmations:
            lengths = {"sendLength": len(c["itemsSending"]), "receiveLength": len(c["itemsReceiving"])}
            output += await render_template("confirmation.html", confirmation=c, lengths = lengths)
        return output


# leave at end of code \/
if __name__ == "__main__":
    app.run(debug='True')
# leave at end of code /\
