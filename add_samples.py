from app import app, db, Contact

with app.app_context():
    # Clear and recreate tables
    db.drop_all()
    db.create_all()
    
    # Add samples
    samples = [
        Contact(name="Alice Johnson", email="alice@example.com", phone="555-0101", address="123 Main St"),
        Contact(name="Bob Smith", email="bob@example.com", phone="555-0102", address="456 Oak Ave"),
        Contact(name="Charlie Brown", email="charlie@example.com", phone="555-0103", address="789 Pine Rd"),
        Contact(name="Diana Prince", email="diana@example.com", phone="555-0104", address="321 Elm St"),
        Contact(name="Evan Wright", email="evan@example.com", phone="555-0105", address="654 Maple Dr"),
        Contact(name="Fiona Green", email="fiona@example.com", phone="555-0106", address="987 Cedar Ln"),
        Contact(name="George King", email="george@example.com", phone="555-0107", address="135 Birch Blvd"),
        Contact(name="Hannah Lee", email="hannah@example.com", phone="555-0108", address="246 Willow Way"),
        Contact(name="Ian Frost", email="ian@example.com", phone="555-0109", address="864 Spruce Ct"),
        Contact(name="Jenny Lopez", email="jenny@example.com", phone="555-0110", address="975 Redwood Pl")
    ]
    
    db.session.add_all(samples)
    db.session.commit()
    print("Database initialized with 10 contacts!")