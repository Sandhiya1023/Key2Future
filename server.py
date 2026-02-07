from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
CORS(app)

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        data = request.json
        user_email = data['email']
        user_message = data['message']
        
        # Email configuration (using Gmail SMTP)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "akashcanand71100@gmail.com"  # Replace with your Gmail
        sender_password = "dvcg qgep atnp nbnj"  # Replace with your Gmail app password
        recipient_email = "akashcanand71100@gmail.com"
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = "Helpdesk Request from Course System"
        
        body = f"""
        New helpdesk message received:
        
        From: {user_email}
        Message: {user_message}
        
        Sent from Course Database System
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        
        return jsonify({"success": True, "message": "Email sent successfully!"})
        
    except Exception as e:
        return jsonify({"success": False, "message": f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)