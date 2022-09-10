from unicodedata import name
from flask import Flask
app = Flask(__name__)

@app.route('/home/<name>')
def home_view(name):
    return 'Grill Bento %s' %name
# app.add_url_rule('/','hello',home_view) == app.route('/home')

if __name__ == "__main__":
    app.run()

# app.route(rule,options)
# app.run(host,port,debug,options)

app.debug = True
app.run()
app.run(debug = True)