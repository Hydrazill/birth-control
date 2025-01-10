
from flask import (
                    session,
                    url_for,
                    redirect,
                    request,
                    render_template,
                )
import logging
from werkzeug.security import (
                                    generate_password_hash,
                                )

from app.models import (
                            ActeNaiss,
                            Administrateur,
                            Declareur,
                        )
def acceuil():
    if "user" not in session:
        return redirect(url_for("auth.auth_login"))
    if 'declaration--form' in request.form:
        actenaiss = ActeNaiss(
                                firstname=request.form['firstname'],
                                lastname=request.form['lastname'],
                                birthdate=request.form['birthdate'],
                                birthplace=request.form['birthplace'],
                                sexe=request.form['sexe'],
                                
                                # infos pere
                                namefather=request.form['namefather'],
                                birthdatefather=request.form['birthdatefather'],
                                birthplacefather=request.form['birthplacefather'],
                                addressfather=request.form['addressfather'],
                                professionfather=request.form['professionfather'],
                                
                                # infos mere
                                namemother=request.form['namemother'],
                                birthdatemother=request.form['birthdatemother'],
                                birthplacemother=request.form['birthplacemother'],
                                addressmother=request.form['addressmother'],
                                professionmother=request.form['professionmother'],
                                
                                # info declareur
                                firstnamedeclareur=session['user']['firstname'],
                                lastnamedeclareur=session['user']['lastname'],
                            )
        actenaiss.save()
        logging.debug(f"declaration de l'enfant {actenaiss.lastname}")
    actes = []
    if session['isAdmin']:
        actes = ActeNaiss.objects()
    else:
        temp = ActeNaiss.objects()
        for tmp in temp:
            if tmp.firstnamedeclareur == session['user']['firstname'] and tmp.lastnamedeclareur == session['user']['lastname']:
                actes.append(tmp)
    if not session["isAdmin"]:
      return render_template(
                              "acceuil/acceuil.html",
                              username=session["user"]['lastname'] + " " + {session["user"]['firstname'],
                              isAdmin=session["isAdmin"],
                              actes=actes,
                            )
    else render_template(
                          "acceuil/acceuil.html",
                          username=session["user"]['email'],
                          isAdmin=session["isAdmin"],
                          actes=actes,
                        )


    # fonction annexe
def create_admin():
    try:
        admin = Administrateur(
                                email="admin-djiokeng2003@gmail.com",
                                password=generate_password_hash("l0rd_9h057"),
                            )
        admin.save()
        print("creation de l'administrateur:")
        print({
            'id': admin.id,
            'email': admin.email,
        })
        return True
    except:
        return False
