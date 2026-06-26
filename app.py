from flask import Flask,render_template,request,redirect,url_for,session
app=Flask(__name__); app.secret_key='secret'
users={}
@app.route('/')
def index(): return redirect(url_for('login'))
@app.route('/signup',methods=['GET','POST'])
def signup():
    msg=''
    if request.method=='POST':
        u=request.form['username']; p=request.form['password']; c=request.form['confirm']
        if p!=c: msg='Passwords do not match'
        elif u in users: msg='User exists'
        else: users[u]=p; return redirect(url_for('login'))
    return render_template('signup.html',msg=msg)
@app.route('/login',methods=['GET','POST'])
def login():
    msg=''
    if request.method=='POST':
        u=request.form['username']; p=request.form['password']
        if users.get(u)==p:
            session['user']=u; return redirect(url_for('home'))
        msg='Invalid credentials'
    return render_template('login.html',msg=msg)
@app.route('/home')
def home():
    if 'user' not in session: return redirect(url_for('login'))
    return render_template('home.html',user=session['user'])
@app.route('/logout')
def logout(): session.clear(); return redirect(url_for('login'))
if __name__=='__main__': app.run(debug=True)
