from flask import Flask, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return "Food App Backend Running"

@app.route('/login', methods=['POST'])
def login():
    if request.form['username']=='admin' and request.form['password']=='1234':
        return redirect('http://127.0.0.1:5500/dashboard.html')
    return "Login Failed"

if __name__=='__main__':
    app.run(debug=True)