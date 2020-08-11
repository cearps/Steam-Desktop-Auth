# Steam-Desktop-Auth
Script to get Steam TFA codes on your desktop

Confirmation part is not the greatest... it works sometimes

## Requirements
- Ensure you have python 3.8
- py -m pip install -U steamio
- pip install quart

## Setup
1. Ensure all requirements are met.
2. Generate the information for the input.json file with [these steps](https://pastebin.com/rFHRrT88). More info on this [here](https://steam.readthedocs.io/en/stable/api/steam.guard.html).
3. Run quartmain.py (using python)
4. You should then be able to access your Steam Codes and confirmations via localhost:5000

## Preview of UI
![preview image](https://i.gyazo.com/c3719b4469f06b74070ac6b7043070d5.png)
