from tinydb import TinyDB


def create_db():
    db = TinyDB('db.json')
    db.truncate()
    db.insert({'name': 'Order Form', 'order_date': 'date', 'customer_phone': 'phone', 'order_details': 'text'})
    db.insert({'name': 'Subscriber Form', 'subscribe_date': 'date', 'subscriber_email': 'email'})
    db.insert({'name': 'Medical Form', 'examination_date': 'date', 'patient_email': 'email', 'patient_phone': 'phone'})
    db.insert({'name': 'Contact Form', 'contact_email': 'email', 'contact_phone': 'phone'})
    db.insert({'name': 'Contact Form', 'contact_email': 'email', 'contact_phone': 'phone', 'information': 'text'})
    db.insert({'name': 'Client Form', 'client_phone': 'phone', 'description': 'text'})

if __name__ == '__main__':
    create_db()
