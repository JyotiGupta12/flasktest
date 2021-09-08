from flask import Flask, request, url_for,flash,redirect
# adding html template
from flask import render_template
import random
app = Flask(__name__)

@app.route('/')
@app.route('/rpsGame', methods = ["GET","POST"])
def rpsGame():
    comp_list = ["paper", "rock", "scissor"]
    comp_value = random.choice(comp_list)
    if request.method == "POST":
        user_item = request.form['item']
        return render_template('rpsGameOutput.html',user_item = user_item,comp_value = comp_value)
    return render_template('rpsGameSetup.html')

if __name__ == '__main__':
    # sess.init_app(app)
    app.run(debug=True, port=90,host = "0.0.0.0")
    # to run on cmd
