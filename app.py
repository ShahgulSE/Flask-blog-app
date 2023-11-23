from flask import Flask ,render_template ,request, redirect, url_for # flask -> package Flask-> Class
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import logging
import sys

app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stderr))
app.logger.setLevel(logging.ERROR)


#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://shahgul:mysql@1996@localhost/blogdb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:app@localhost:3307/blogdb'

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

# "{{url_for('static',filename='assets/img/home-bg.jpg')}}"
class Contact(db.Model):
    __tablename__ = 'Contact'  # Explicitly providing the table name
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_num = db.Column(db.String(20))
    msg = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    email = db.Column(db.String(100))
@app.route('/index')  #endpoint
def index():
    return render_template('index.html')
@app.route('/post')  #endpoint
def post():
    return render_template('post.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            # Get data from form
            name = request.form.get('name')
            phone_num = request.form.get('phone_num')
            msg = request.form.get('msg')
            email = request.form.get('email')

            # Create new Contact instance
            new_contact = Contact(
                name=name,
                phone_num=phone_num,
                msg=msg,
                email=email
            )
            
            # Add to the session and commit to the database
            db.session.add(new_contact)
            db.session.commit()

            app.logger.info(f'Added new contact: {name}')
            # Redirect to a new URL, display a success message, or clear the form
            return redirect(url_for('index'))  # Redirect to index page or a 'success' page

        except Exception as e:
            db.session.rollback()
            app.logger.error('Failed to add contact: %s', str(e))
            # Implement your error handling, e.g., show an error message to the user

    return render_template('contact.html')


    
    
@app.route('/about')  #endpoint
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True) #detect change easily
