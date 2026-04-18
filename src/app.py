#'/api/v1/details'
#'/api/v1/health'
from flask import Flask
import datetime,socket

app = Flask(__name__)

@app.route("/api/v1/details")
def details():
    return {
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "hostname": socket.gethostname(),
        "message": "You are Great!!",
        "deployed_on": "Kubernetes",
        "deployed_for": "Cloud Platform Engineer"

    }

@app.route("/api/v1/health")
def health():
    return {
        "status": "up"

    },200

if __name__ == "__main__":
    app.run(host="0.0.0.0")