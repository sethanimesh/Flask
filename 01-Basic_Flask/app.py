from flask import Flask

### WSGI Application
app=Flask(__name__)

@app.route("/")##Decorator
def welcome():
    return "Welcome to my First Flask Application."

if __name__=='__main__':
    app.run(debug=True)