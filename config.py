import os

DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///messages_store.db")

# we can set configurations for sending email, sms, whatsapp etc. messages.
