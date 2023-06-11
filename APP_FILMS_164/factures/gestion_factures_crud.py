"""Gestion des "routes" FLASK et des données pour les factures.
Fichier : gestion_factures_crud.py
Auteur : OM 2021.03.16
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.factures.gestion_factures_wtf_forms import FormWTFAjouterFactures
from APP_FILMS_164.factures.gestion_factures_wtf_forms import FormWTFDeleteFactures
from APP_FILMS_164.factures.gestion_factures_wtf_forms import FormWTFUpdateFactures

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /factures_afficher
    
    Test : ex : http://127.0.0.1:5575/factures_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_factures_sel = 0 >> tous les factures.
                id_factures_sel = "n" affiche le genre dont l'id est "n"
"""


@app.route("/factures_afficher/<string:order_by>/<int:id_factures_sel>", methods=['GET', 'POST'])
def factures_afficher(order_by, id_factures_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_factures_sel == 0:
                    strsql_factures_afficher = """SELECT id_factures, Montant, Date FROM t_factures"""

                    mc_afficher.execute(strsql_factures_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_factures"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du genre sélectionné avec un nom de variable
                    valeur_id_factures_selected_dictionnaire = {"value_id_factures_selected": id_factures_sel}
                    strsql_factures_afficher = """SELECT * FROM t_factures WHERE id_factures = %(value_id_factures_selected)s"""

                    mc_afficher.execute(strsql_factures_afficher, valeur_id_factures_selected_dictionnaire)
                else:
                    strsql_factures_afficher = """SELECT * FROM t_factures"""

                    mc_afficher.execute(strsql_factures_afficher)

                data_genres = mc_afficher.fetchall()

                print("data_genres ", data_genres, " Type : ", type(data_genres))

                # Différencier les messages si la table est vide.
                if not data_genres and id_factures_sel == 0:
                    flash("""La table "t_factures" est vide. !!""", "warning")
                elif not data_genres and id_factures_sel > 0:
                    # Si l'utilisateur change l'id_factures dans l'URL et que le genre n'existe pas,
                    flash(f"L'enfant demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_factures" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données factures affichés !!", "success")

        except Exception as Exception_factures_afficher:
            raise ExceptionGenresAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{factures_afficher.__name__} ; "
                                          f"{Exception_factures_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("factures/factures_afficher.html", data=data_genres)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /factures_ajouter
    
    Test : ex : http://127.0.0.1:5575/factures_ajouter
    
    Paramètres : sans
    
    But : Ajouter un genre pour un film
    
    Remarque :  Dans le champ "montant_facture_html" du formulaire "factures/factures_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/factures_ajouter", methods=['GET', 'POST'])
def facture_ajouter_wtf():
    form = FormWTFAjouterFactures()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                montant_facture_wtf = form.montant_facture_wtf.data
                montant_facture = montant_facture_wtf

                date_facture_wtf = form.date_factures_wtf.data
                date_facture = date_facture_wtf

                valeurs_insertion_dictionnaire = {"value_montant_facture": montant_facture, "value_date_facture": date_facture}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_genre = """INSERT INTO t_factures (id_factures,Montant,Date) VALUES (NULL,%(value_montant_facture)s,%(value_date_facture)s)"""

                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_genre, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('factures_afficher', order_by='DESC', id_factures_sel=0))

        except Exception as Exception_facture_ajouter_wtf:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{facture_ajouter_wtf.__name__} ; "
                                            f"{Exception_facture_ajouter_wtf}")

    return render_template("factures/factures_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /facture_update
    
    Test : ex cliquer sur le menu "factures" puis cliquer sur le bouton "EDIT" d'un "genre"
    
    Paramètres : sans
    
    But : Editer(update) un genre qui a été sélectionné dans le formulaire "factures_afficher.html"
    
    Remarque :  Dans le champ "nom_facture_update_wtf" du formulaire "factures/factures_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/facture_update", methods=['GET', 'POST'])
def facture_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_factures"
    id_facture_update = request.values['id_facture_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdateFactures()
    try:
        print(" on submit ", form_update.validate_on_submit())
        if form_update.validate_on_submit():
            # Récupèrer la valeur du champ depuis "factures_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            name_facture_update = form_update.nom_facture_update_wtf.data
            name_facture_update = name_facture_update
            date_genre_essai = form_update.date_genre_wtf_essai.data

            valeur_update_dictionnaire = {"value_id_genre": id_facture_update,
                                          "value_montant_facture": name_facture_update,
                                          "value_date_genre_essai": date_genre_essai
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_intitulegenre = """UPDATE t_factures SET Date = %(value_montant_facture)s, 
            Montant = %(value_date_genre_essai)s WHERE id_factures = %(value_id_genre)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_intitulegenre, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_facture_update"
            return redirect(url_for('factures_afficher', order_by="ASC", id_factures_sel=id_facture_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_factures" et "intitule_genre" de la "t_factures"
            str_sql_id_genre = "SELECT id_factures, Date, Montant FROM t_factures " \
                               "WHERE id_factures = %(value_id_genre)s"
            valeur_select_dictionnaire = {"value_id_genre": id_facture_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_genre, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_nom_genre = mybd_conn.fetchone()
            print("Montant ", data_nom_genre, " type ", type(data_nom_genre), " genre ",
                  data_nom_genre["Date"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "factures_update_wtf.html"
            form_update.nom_facture_update_wtf.data = data_nom_genre["Date"]
            form_update.date_genre_wtf_essai.data = data_nom_genre["Montant"]

    except Exception as Exception_facture_update_wtf:
        raise ExceptionGenreUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{facture_update_wtf.__name__} ; "
                                      f"{Exception_facture_update_wtf}")

    return render_template("factures/factures_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /facture_delete
    
    Test : ex. cliquer sur le menu "factures" puis cliquer sur le bouton "DELETE" d'un "genre"
    
    Paramètres : sans
    
    But : Effacer(delete) un genre qui a été sélectionné dans le formulaire "factures_afficher.html"
    
    Remarque :  Dans le champ "nom_facture_delete_wtf" du formulaire "factures/factures_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/facture_delete", methods=['GET', 'POST'])
def facture_delete_wtf():
    data_films_attribue_facture_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_factures"
    id_facture_delete = request.values['id_facture_btn_delete_html']

    # Objet formulaire pour effacer le genre sélectionné.
    form_delete = FormWTFDeleteFactures()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("factures_afficher", order_by="ASC", id_factures_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "factures/factures_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_films_attribue_facture_delete = session['data_films_attribue_facture_delete']
                print("data_films_attribue_facture_delete ", data_films_attribue_facture_delete)

                flash(f"Effacer le genre de façon définitive de la BD !!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_genre": id_facture_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_factures = """DELETE FROM t_factures WHERE id_factures = %(value_id_genre)s"""
                # Manière brutale d'effacer d'abord la "fk_genre", même si elle n'existe pas dans la "t_enfants_sante"
                # Ensuite on peut effacer le genre vu qu'il n'est plus "lié" (INNODB) dans la "t_enfants_sante"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_factures, valeur_delete_dictionnaire)

                flash(f"Genre définitivement effacé !!", "success")
                print(f"Genre définitivement effacé !!")

                # afficher les données
                return redirect(url_for('factures_afficher', order_by="ASC", id_factures_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_genre": id_facture_delete}
            print(id_facture_delete, type(id_facture_delete))

            # Requête qui affiche tous les enfants_sante qui ont le genre que l'utilisateur veut effacer
            str_sql_genres_films_delete = """SELECT id_factures, Montant, Date FROM t_factures WHERE id_factures = %(value_id_genre)s"""


            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_genres_films_delete, valeur_select_dictionnaire)
                data_films_attribue_facture_delete = mydb_conn.fetchall()
                print("data_films_attribue_facture_delete...", data_films_attribue_facture_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "factures/factures_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_films_attribue_facture_delete'] = data_films_attribue_facture_delete

                # Opération sur la BD pour récupérer "id_factures" et "intitule_genre" de la "t_factures"
                str_sql_id_genre = "SELECT id_factures, Montant, Date FROM t_factures WHERE id_factures = %(value_id_genre)s"

                mydb_conn.execute(str_sql_id_genre, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "nom genre" pour l'action DELETE
                data_nom_genre = mydb_conn.fetchone()
                print("data_nom_genre ", data_nom_genre, " type ", type(data_nom_genre), " genre ",
                      data_nom_genre["Montant"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "factures_delete_wtf.html"
            form_delete.nom_facture_delete_wtf.data = data_nom_genre["Montant"]

            # Le bouton pour l'action "DELETE" dans le form. "factures_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_facture_delete_wtf:
        raise ExceptionGenreDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{facture_delete_wtf.__name__} ; "
                                      f"{Exception_facture_delete_wtf}")

    return render_template("factures/factures_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_films_associes=data_films_attribue_facture_delete)
