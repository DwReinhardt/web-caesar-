from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="" method="post">
            <label for="rot"> Rotate by: </label>
            <input id="rot" type="text" value="0" /><br>
            <textarea name="text" form="" ></textarea><br>
            <input type="submit" />
        </form>
    </body>
</html>
"""

@app.route("/", methods=['post'])

def encrypt():
    text = request.form.text #['text']
    rot = request.form.rot #['rot']
    rotate = int(rot)
    encrypted_msg = caesar.rotate_string(text, rotate)
    return f"<h1> Your encrypted message is: " + encrypted_msg + "</h1>"

@app.route("/")
def index():
    return form

app.run()