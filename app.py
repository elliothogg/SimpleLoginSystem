from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup')
def sign_up():
    return render_template('signup.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        if request.form['username'] == 'minamarz' and request.form['password'] == 'kenzo':
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