from flask import Flask
from os import environ

app = Flask(__name__)
    
# Initiated by adding "/hello/Ryan" to end of browser URL
@app.route("/hello/<name>")
def hi_person(name):
    html = """
    <h1>Hello {} !</h1>
    <p>Cute kittens!</p>
    """
    return html.format(name.title())
    
@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"
    
# Print Jedi name. First 3 letters of last name, first 2 letters of 1st name
@app.route("/jedi/<first>/<last>")
def jedi_name(first, last):
    first = first.title()
    last = last.title()
    jedi = last[:3] + first[:2]
    return jedi

    
if __name__ == "__main__":
    app.run(host=environ['C9_IP'],
            port=int(environ['PORT']))