from flask import Flask
from flask_mail import Mail, Message

# Initialize Flask app
app = Flask(__name__)

# Flask-Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'joebrian998@gmail.com'
app.config['MAIL_PASSWORD'] = 'kklfqzaqpdxtucbx'  # Ensure this is secure
app.config['MAIL_DEFAULT_SENDER'] = 'susanjames@gmail.com'

# Initialize Flask-Mail
mail = Mail(app)

@app.route('/send-email')
def send_email():
    try:
        # Create a Message object
        msg = Message(
            "Hello from Flask!",  # Email Subject
            recipients=["owuorulare@student.moringaschool.com"],  # Recipient Email
            body="This is a test email sent from a Flask app using Flask-Mail!"  # Email Body
        )
        mail.send(msg)
        return "Email sent successfully!"

    except Exception as e:
        return f"Failed to send email: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
