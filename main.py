import json
import subprocess
import steamauthentication as sa
from flask import Flask, request, render_template

# flask app
app = Flask(__name__)

@app.route("/")
def index():
        code = sa.get_code()
        timeLeft = 30 - (sa.get_time() % 30)
        return render_template('index.html', code=code, timeLeft=timeLeft)


# leave at end of code \/
if __name__ == "__main__":
    app.run(debug='True')
# leave at end of code /\
