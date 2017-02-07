from flask import Flask, request
from flask_basicauth import BasicAuth

app = Flask(__name__)

FILENAME = "ip"

def read_ip():
    with open(FILENAME, "r") as f:
        ip = f.readline().strip()
    return ip
    
def write_ip(ip):
    with open(FILENAME, "w") as f:
        f.write(ip)

    
@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == "GET":
        try:
            myip = read_ip()
            if len(myip) > 0:
                return myip
            else:
                raise Exception("ip_does_not_exists")
        except Exception as e:
            print e
            return "ip_does_not_exists"
        
    elif request.method == "POST":
        try:
            write_ip(request.form["ip"])
            return "ok_code"           
        except Exception as e:
            print e
            return "bad_req_form"
        
    else:
        return "bad request method"
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")