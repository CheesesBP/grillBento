from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/home')
def home():
    return 'Grill Bento'

@app.route('/combo/<meat>')
def combo_set(meat):
    return 'Please select the combo for %s' %meat

@app.route('/set/<drink>')
def set_drink(drink):
    return 'Please select the set drink %s' %drink

if __name__ == "__main__":
    app.run()

# app.route(rule,options)
# app.run(host,port,debug,options)

app.debug = True
app.run()
app.run(debug = True)