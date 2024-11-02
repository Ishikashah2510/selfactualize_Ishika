from flask import Flask, request, jsonify
from db_setup import db, MessageLog
from mock_send import send_message_mock
import config

# setting up the flask application
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.DATABASE_URI
db.init_app(app)


@app.route('/sendMessage', methods=['POST'])
def send_message():
    data = request.get_json() # collecting payload

    message_type = data.get("type")
    recipient = data.get("recipient")
    content = data.get("content")

    # Validate inputs
    if not message_type or not recipient or not content:
        return jsonify({"status": "failure", "message": "Missing fields"}), 400

    # Send the message (mock function)
    response = send_message_mock(message_type, recipient, content)
    status = response.get("status")
    reason = response.get("message")

    # Log the message in the database
    message_log = MessageLog(
        type=message_type,
        recipient=recipient,
        content=content,
        status=status,
        reason_for_failure=reason
    )
    db.session.add(message_log)
    db.session.commit()

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
