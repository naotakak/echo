from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route("/")
def home():
    print "\n\n\n"
    print "***DIAG: this Flask obj***"
    print app
    print "***DIAG: request.obj***"
    print request
    print "***DIAG: request.args***"
    print request.args

    return render_template('template.html')

@app.route("/welcome")
def welcome():
    return render_template('welcome.html', name = request.args['name'], method = request)

if (__name__ == "__main__"):
    app.debug = True
    app.run()
