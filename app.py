from flask import Flask, render_template, request, redirect, url_for, make_response





app = Flask(__name__)





# Home route
@app.route('/')
def home():
    return render_template('mein-konto.html')




# Werbetreibende route
@app.route('/werbetreibende/')
def werbetreibende():
    return render_template('werbetreibende.html')




# Werbung teilen" -> Submenu (Weiterleitung) route
@app.route('/weiterleitung/')
def weiterleitung():
    return render_template('weiterleitung.html')




# Werbung teilen" -> Submenu (Upload) route
@app.route('/upload/')
def upload():
    return render_template('upload.html')





# Admin" ->Submenu (Overview) route
@app.route('/overview/')
def overview():
    return render_template('overview.html')





# Admin" -> Submenu (Einstellungen) route
@app.route('/einstellungen/')
def einstellungen():
    return render_template('einstellungen.html')





# Mein Profil route
@app.route('/mein-profil/')
def mein_profil():
    return render_template('mein-profil.html')





# Umfrage route
@app.route('/umfrage/')
def umfrage():
    return render_template('umfrage.html')




# Sign out route
@app.route('/sign-out/')
def sign_out():
    return render_template('mein-konto.html')




# Login route
@app.route('/login/')
def login():
    return render_template('login.html')





# Registration route
@app.route('/registration/')
def registration():
    return render_template('registration.html')





if __name__ == '__main__':
    app.run(debug = True)
