import os
from flask import Flask, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER']= os.getenv("SERVER")
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.getenv("USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("API_KEY")
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

@app.route("/crash", methods = ['POST'] )
def send_crash_log():
    msg = Message('crash log', sender = os.getenv("USERNAME"), recipients = [os.getenv("RECIPIENT")])
    msg.body = request.get_data()
    mail.send(msg)
    return ""

if __name__ == "__main__":
    app.run(host='0.0.0.0')
