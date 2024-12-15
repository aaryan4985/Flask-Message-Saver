from flask import Flask, render_template, request, redirect, url_for

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

@app.route('/messages')
def messages():
    with open('messages.txt',"r") as file:
        messages = file.readlines()
    return render_template('messages.html', messages=messages)

@app.route('/clear-messages', methods=['POST'])
def clear_messages():
    open("messages.txt", "w").close()
    return redirect(url_for('messages'))

if __name__ == '__main__':
    app.run(debug=True)
