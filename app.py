from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        
        with open('messages.txt', 'a') as file:
            file.write(f"Name:{name}\nMessage: {message}\n{'-'*50}\n")
            
        return f"<h1>Thanks, {name}!</h1><p>Your message has been saved.</p><a href='/'>Back to Home</a>"

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
