from v2_flask import app

@app.route('/')
@app.route('/index')
def index():
    return "helloworld"  # temporary placeholder
