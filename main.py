from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="" method="post">
            <label for="rot"> Rotate by: </label>
            <input type="text" name="rot" value="0" />
            <br>
            <textarea type="text" name="text">{0}</textarea>
            <br>
            <input type="submit" />
        </form>
    </body>
</html>
"""

@app.route("/", methods=['post'])

def encrypt():
    text = request.form['text'] #['text']
    rot = request.form['rot']   #['rot']
    rotate = int(rot)
    encrypted_msg = rotate_string(text, rotate)
    return form.format(encrypted_msg)

@app.route("/")
def index():
    return form.format("")

app.run()