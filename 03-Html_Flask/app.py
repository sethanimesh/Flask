##Jinja2 template Engine
'''
{%...%} for statements
{{   }} expressions to print output
{#.....#} comments
'''

from flask import Flask, render_template, request, redirect, url_for

app = Flask("__name__")

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score>=50:
        res = "PASS"
    else:
        res = "FAIL"
    return render_template('result.html', result=res)


@app.route("/submit", methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method=="POST":
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        python = float(request.form['python'])
        datascience = float(request.form['datascience'])
        total_score = (science+maths+python+datascience)
    return redirect(url_for("success", score=total_score))

if __name__=="__main__":
    app.run(debug=True)