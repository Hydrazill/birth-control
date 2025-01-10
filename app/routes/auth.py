
from flask import (
                    flash,
                    redirect,
                    render_template,
                    session,
                    request,
                    url_for,
                )
import logging
import re
from werkzeug.security import (
                                check_password_hash,
                                generate_password_hash,
                            )


from app.models import (
                            Administrateur,
                            Declareur,
                        )

def login():
    if request.method == "POST":
        user = None
        admins = Administrateur.objects()
        for admin in admins:
            if admin.email == request.form["username"] and check_password_hash(admin.password, request.form["password"]):
                logging.debug(f"connexion de l'utilisateur {admin.email}")
                session["user"] = {
                        'email': admin.email,
                        'password': admin.password,
                    }
                session["isAdmin"] = True
                user = admin
                return redirect(url_for("main.main_acceuil"))
        declareurs = Declareur.objects()
        for declareur in declareurs:
            if declareur.email == request.form["username"] and check_password_hash(declareur.password, request.form["password"]):
                logging.debug(f"connexion de l'utilisateur {declareur.lastname}")
                session["user"] = {
                        'firstname': declareur.firstname,
                        'lastname': declareur.lastname,
                        'email': declareur.email,
                        'phonenumber': declareur.phonenumber,
                        'adresse': declareur.adresse,
                        'sexe': declareur.sexe,
                        'password': declareur.password,
                    }
                session["isAdmin"] = False
                user = declareur
                return redirect(url_for("main.main_acceuil"))
        for p in declareurs:
            if check_username(username_save=f"{p.lastname} {p.firstname}", username_test=request.form["username"]) and check_password_hash(p.password, request.form["password"]):
                logging.debug(f"connexion de l'utilisateur {p.lastname}")
                session["user"] = {
                                    'firstname': p.firstname,
                                    'lastname': p.lastname,
                                    'email': p.email,
                                    'phonenumber': p.phonenumber,
                                    'adresse': p.adresse,
                                    'sexe': p.sexe,
                                    'password': p.password,
                                }
                session["isAdmin"] = False
                user = p
                return redirect(url_for("main.main_acceuil"))
        if not user:
            flash("invalid username or password.", 'error')
            return render_template('auth/login.html')
    
    return render_template("auth/login.html")

def register():
    if request.method == "POST":
        password = request.form["password"]
        cpassword = request.form["cpassword"]
        for declareur in Declareur.objects():
            if declareur.email == request.form["email"]: flash("Email already use.", 'error'); return render_template('auth/register.html')
        if len(password) < 8: flash("Password must contains at least 08 characters.", 'error'); return render_template('auth/register.html')
        if not re.search("[A-Z]", password): flash("Password must contains UPPER characters.", 'error'); return render_template('auth/register.html')
        if not re.search("[a-z]", password): flash("Password must contains lower characters.", 'error'); return render_template('auth/register.html')
        if not re.search("[0-9]", password): flash("Password must contains number.", 'error'); return render_template('auth/register.html')
        if not re.search("[!@#$%^&*]", password): flash("Password must contains special characters(!, @, #, $, %, ^, &, *).", 'error'); return render_template('auth/register.html')
        if password != cpassword: flash("Passwords don't match.", 'error'); return render_template('auth/register.html')

        declareur = Declareur(
                            firstname=request.form["firstname"],
                            lastname=request.form["lastname"],
                            email=request.form["email"],
                            phonenumber=request.form["phonenumber"],
                            adresse=request.form["address"],
                            sexe=request.form["sexe"],
                            password=generate_password_hash(password=password),
                        )
        declareur.save()
        logging.debug(f"creation du declareur {declareur.lastname}")
        return redirect(url_for("auth.auth_login"))
    
    return render_template("auth/register.html")

    # fonction annexe
def check_username(username_save="", username_test=""): return True if len(username_save.split()) == len(username_test.split()) and all(username in username_save.split() for username in username_test.split()) else False