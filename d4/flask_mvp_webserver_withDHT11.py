from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    with open("log.txt", "a") as f:
        f.write("humidity = %s, temp = %s " % (request.args["field1"], request.args["field2"]))
        f.write("\n")
        return 'Thanks'

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
