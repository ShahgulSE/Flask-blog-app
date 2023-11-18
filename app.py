from flask import Flask ,render_template # flask -> package Flask-> Class

app = Flask(__name__)
# "{{url_for('static',filename='assets/img/home-bg.jpg')}}"

@app.route('/index')  #endpoint
def index():
    return render_template('index.html')
@app.route('/post')  #endpoint
def post():
    return render_template('post.html')
@app.route('/contact')  #endpoint
def contact():
    return render_template('contact.html')
@app.route('/about')  #endpoint
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True) #detect change easily
