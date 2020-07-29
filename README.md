# Steam-Desktop-Auth
Script to get Steam TFA codes on your desktop

I plan on adding a part to do confirmations as well.

## Requirements
- Ensure you have python 3.6
- python -m pip install -U steam[client]
- python -m pip install -U steam

## Setup
1. Ensure all requirements are met.
2. Generate token.json file with [these steps](https://pastebin.com/rFHRrT88). More info on this [here](https://steam.readthedocs.io/en/stable/api/steam.guard.html).
3. Run main.py
4. You should then be able to access your Steam Codes via localhost:5000
