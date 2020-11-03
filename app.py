from flask import Flask, render_template, request, redirect
import time
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def home():
    file1 = open('somefile.txt', 'r')
    lines = file1.readlines()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    case = lines[0]
    recover = lines[1]
    dead = lines[2]
    crit = lines[3]
    case_treat = lines[4]
    n_case = lines[5]
    return render_template("index.html",time = dt_string, cases = case, death = dead, recovery = recover, mortality = crit, case_today = n_case, cases_treated = case_treat)



if __name__ == "__main__":
    app.run(debug=True)
