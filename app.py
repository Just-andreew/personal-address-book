from flask import Flask, render_template, request, redirect, url_for , flash, session 
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'Address_book_Assessment'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))

# Create the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        
        new_contact = Contact(name=name, email=email, phone=phone, address=address)
        db.session.add(new_contact)
        db.session.commit()
        
        return redirect(url_for('index'))
    
    return render_template('add_contact.html')

# Edit Contact Route
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_contact(id):
    contact = Contact.query.get_or_404(id)
    
    if request.method == 'POST':
        if '_flashes' in session:
            session['_flashes'].clear()
        contact.name = request.form['name']
        contact.email = request.form['email']
        contact.phone = request.form['phone']
        contact.address = request.form['address']
        
        db.session.commit()
        flash('Contact updated successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('edit_contact.html', contact=contact)

# Delete Contact Route
@app.route('/delete/<int:id>', methods=['POST'])
def delete_contact(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    flash('Contact deleted successfully!', 'danger')
    return redirect(url_for('index'))

@app.route('/contact/<int:id>')
def view_contact(id):
    contact = Contact.query.get_or_404(id)
    return render_template('view_contact.html', contact=contact)


if __name__ == '__main__':
    app.run(debug=True)
