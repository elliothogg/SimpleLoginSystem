from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)\

users = {}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        user_name = request.form['username']
        password = request.form['password']
        message = ""
        if user_name in users:
            message = "This username is already in use"
            print(users)
            return render_template('signup.html', message=message)
            
        else:
            users[user_name] = password
            message = "Your account was sucessfully created"
            print(users)
            return render_template('signup.html', message=message)
                       
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user_name = request.form['username']
        password = request.form['password']
        if user_name in users and password == users[user_name]:
            return redirect(url_for('account'))
        else:
            incorrect = "username or password is incorrect"
            return render_template('login.html', value=incorrect)
   
    return render_template('login.html')

    
@app.route('/account')
def account():
    return render_template('account.html')

if __name__ == "__main__":
    app.run(debug=True)