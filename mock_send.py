import re
import phonenumbers
from phonenumbers import NumberParseException


def send_message_mock(message_type, recipient, content):
    if message_type.lower() == "email":
        all_okay, msg = send_message_email(recipient, content)
        if all_okay:
            return {"status": "success"}

        return {"status": "failure", "message": msg}

    elif message_type.lower() == "sms":
        all_okay, msg = send_message_sms(recipient, content)
        if all_okay:
            return {"status": "success"}

        return {"status": "failure", "message": msg}

    elif message_type.lower() == "whatsapp":
        all_okay, msg = send_message_whatsapp(recipient, content)
        if all_okay:
            return {"status": "success"}

        return {"status": "failure", "message": msg}

    # can add more cases as per need

    return {"status": "failure", "message": f"Unsupported message type: {message_type}"}


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None


def send_message_email(recipient, content):
    try:
        # check if recipient is email ID
        # we can also use a python library for this check
        if not is_valid_email(recipient):
            return False, "Recipient is not a email ID"

        # we can write code using a library to send an email
        # one of the options is smtplib
        # we can also use an external API, whatever works best
        # based on our constraints, business needs

        return True, "Okay"

    except Exception as err:
        return False, err


def is_valid_phone_number(phone, region="US"):
    try:
        parsed_number = phonenumbers.parse(phone, region)
        return phonenumbers.is_valid_number(parsed_number)

    except NumberParseException:
        return False


def send_message_sms(recipient, content):
    try:
        # check if recipient is a phone number
        # we can also use simple regex here
        if not is_valid_phone_number(recipient):
            return False, "Recipient is not a phone number"

        # we can use an external API, whatever works best
        # based on our constraints, business needs
        # examples: twilio, vonage etc.
        return True, "Okay"

    except Exception as err:
        return False, err


def send_message_whatsapp(recipient, content):
    try:
        # check if recipient is a phone number
        # we can also use simple regex here
        if not is_valid_phone_number(recipient):
            return False, "Recipient is not a phone number"

        # we can use pywhatkit library
        # we can use an external API, whatever works best
        # based on our constraints, business needs
        # examples: twilio
        return True, "Okay"

    except Exception as err:
        return False, err
