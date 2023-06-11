"""Gestion des "routes" FLASK et des données pour les enfants.
Fichier : gestion_enfants_crud.py
Auteur : OM 2022.04.11
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_YOGA_164.database.database_tools import DBconnection
from APP_YOGA_164.erreurs.exceptions import *
from APP_YOGA_164.enfants.gestion_enfants_wtf_forms import FormWTFUpdateFilm, FormWTFAddFilm, FormWTFDeleteFilm

"""Ajouter un film grâce au formulaire "enfants_add_wtf.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_add

Test : exemple: cliquer sur le menu "Films/Genres" puis cliquer sur le bouton "ADD" d'un "film"

Paramètres : sans


Remarque :  Dans le champ "nom_enfants_wtf" du formulaire "enfants/films_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python dans le fichier ""
            On ne doit pas accepter un champ vide.
"""


@app.route("/film_add", methods=['GET', 'POST'])
def enfant_add_wtf():
    # Objet formulaire pour AJOUTER un film
    form_add_film = FormWTFAddFilm()
    if request.method == "POST":
        try:
            if form_add_film.validate_on_submit():
                nom_film_add = form_add_film.nom_enfant_add_wtf.data
                prenom_enfants_add = form_add_film.prenom_enfant_add_wtf.data

                valeurs_insertion_dictionnaire = {"value_nom_enfants": nom_film_add, "value_prenom_enfants": prenom_enfants_add}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_film = """INSERT INTO t_enfants (id_enfants,Nom,Prenom) VALUES (NULL,%(value_nom_enfants)s,%(value_prenom_enfants)s)"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_film, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion du nouveau film (id_film_sel=0 => afficher tous les enfants)
                return redirect(url_for('enfants_sante_afficher', id_film_sel=0))

        except Exception as Exception_genres_ajouter_wtf:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{enfant_add_wtf.__name__} ; "
                                            f"{Exception_genres_ajouter_wtf}")

    return render_template("enfants/enfants_add_wtf.html", form_add_film=form_add_film)


"""Editer(update) un film qui a été sélectionné dans le formulaire "parents_telephone_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_update

Test : exemple: cliquer sur le menu "Films/Genres" puis cliquer sur le bouton "EDIT" d'un "film"

Paramètres : sans

But : Editer(update) un genre qui a été sélectionné dans le formulaire "factures_afficher.html"

Remarque :  Dans le champ "nom_enfants_wtf" du formulaire "enfants/films_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python.
            On ne doit pas accepter un champ vide.
"""


@app.route("/film_update", methods=['GET', 'POST'])
def enfant_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_enfants"
    id_film_update = request.values['id_film_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update_film = FormWTFUpdateFilm()
    try:
        print(" on submit ", form_update_film.validate_on_submit())
        if form_update_film.validate_on_submit():
            # Récupèrer la valeur du champ depuis "factures_update_wtf.html" après avoir cliqué sur "SUBMIT".
            nom_film_update = form_update_film.nom_enfants_wtf.data
            duree_film_update = form_update_film.prenom_enfants_wtf.data
            datenaissance_film_update = form_update_film.datenaissance_enfants_wtf.data

            valeur_update_dictionnaire = {"value_id_enfants": id_film_update,
                                          "value_nom_enfants": nom_film_update,
                                          "value_prenom_enfants": duree_film_update,
                                          "value_datenaissance_enfants": datenaissance_film_update
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_nom_film = """UPDATE t_enfants SET Nom = %(value_nom_enfants)s,
                                                            Prenom = %(value_prenom_enfants)s,
                                                            DateNAissance = %(value_datenaissance_enfants)s
                                                            WHERE id_enfants = %(value_id_enfants)s"""
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_nom_film, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Afficher seulement le film modifié, "ASC" et l'"id_film_update"
            return redirect(url_for('enfants_sante_afficher', id_film_sel=id_film_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_enfants" et "intitule_genre" de la "t_parents"
            str_sql_id_film = "SELECT * FROM t_enfants WHERE id_enfants = %(value_id_enfants)s"
            valeur_select_dictionnaire = {"value_id_enfants": id_film_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_film, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_film = mybd_conn.fetchone()
            print("data_film ", data_film, " type ", type(data_film), " genre ",
                  data_film["Nom"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "enfants_update_wtf.html"
            form_update_film.nom_enfants_wtf.data = data_film["Nom"]
            form_update_film.prenom_enfants_wtf.data = data_film["Prenom"]
            # Debug simple pour contrôler la valeur dans la console "run" de PyCharm
            print(f" duree film  ", data_film["Prenom"], "  type ", type(data_film["Prenom"]))
            form_update_film.datenaissance_enfants_wtf.data = data_film["DateNaissance"]

    except Exception as Exception_enfant_update_wtf:
        raise ExceptionFilmUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                     f"{enfant_update_wtf.__name__} ; "
                                     f"{Exception_enfant_update_wtf}")

    return render_template("enfants/enfants_update_wtf.html", form_update_film=form_update_film)


"""Effacer(delete) un film qui a été sélectionné dans le formulaire "parents_telephone_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_delete
    
Test : ex. cliquer sur le menu "film" puis cliquer sur le bouton "DELETE" d'un "film"
    
Paramètres : sans

Remarque :  Dans le champ "nom_enfant_delete_wtf" du formulaire "enfants/enfants_delete_wtf.html"
            On doit simplement cliquer sur "DELETE"
"""


@app.route("/film_delete", methods=['GET', 'POST'])
def enfant_delete_wtf():
    # Pour afficher ou cacher les boutons "EFFACER"
    data_film_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_enfants"
    id_film_delete = request.values['id_film_btn_delete_html']

    # Objet formulaire pour effacer le film sélectionné.
    form_delete_film = FormWTFDeleteFilm()
    try:
        # Si on clique sur "ANNULER", afficher tous les enfants.
        if form_delete_film.submit_btn_annuler.data:
            return redirect(url_for("enfants_sante_afficher", id_film_sel=0))

        if form_delete_film.submit_btn_conf_del_film.data:
            # Récupère les données afin d'afficher à nouveau
            # le formulaire "enfants/enfants_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
            data_film_delete = session['data_film_delete']
            print("data_film_delete ", data_film_delete)

            flash(f"Effacer le film de façon définitive de la BD !!!", "danger")
            # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
            # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
            btn_submit_del = True

        # L'utilisateur a vraiment décidé d'effacer.
        if form_delete_film.submit_btn_del_film.data:
            valeur_delete_dictionnaire = {"value_id_enfants": id_film_delete}
            print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

            str_sql_delete_fk_enfants_sante = """DELETE FROM t_enfants_sante WHERE fk_sante = %(value_id_enfants)s"""
            str_sql_delete_fk_enfants_cours = """DELETE FROM t_enfants_cours WHERE fk_cours = %(value_id_enfants)s"""
            str_sql_delete_film = """DELETE FROM t_enfants WHERE id_enfants = %(value_id_enfants)s"""
            # Manière brutale d'effacer d'abord la "fk_enfants", même si elle n'existe pas dans la "t_enfants_sante"
            # Ensuite on peut effacer le film vu qu'il n'est plus "lié" (INNODB) dans la "t_enfants_sante"
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_delete_fk_enfants_sante, valeur_delete_dictionnaire)
                mconn_bd.execute(str_sql_delete_fk_enfants_cours, valeur_delete_dictionnaire)
                mconn_bd.execute(str_sql_delete_film, valeur_delete_dictionnaire)

            flash(f"Film définitivement effacé !!", "success")
            print(f"Film définitivement effacé !!")

            # afficher les données
            return redirect(url_for('enfants_sante_afficher', id_film_sel=0))
        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_enfants": id_film_delete}
            print(id_film_delete, type(id_film_delete))

            # Requête qui affiche le film qui doit être efffacé.
            str_sql_genres_films_delete = """SELECT * FROM t_enfants WHERE id_enfants = %(value_id_enfants)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_genres_films_delete, valeur_select_dictionnaire)
                data_film_delete = mydb_conn.fetchall()
                print("data_film_delete...", data_film_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "enfants/enfants_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_film_delete'] = data_film_delete

            # Le bouton pour l'action "DELETE" dans le form. "enfants_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_enfant_delete_wtf:
        raise ExceptionFilmDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                     f"{enfant_delete_wtf.__name__} ; "
                                     f"{Exception_enfant_delete_wtf}")

    return render_template("enfants/enfants_delete_wtf.html",
                           form_delete_film=form_delete_film,
                           btn_submit_del=btn_submit_del,
                           data_film_del=data_film_delete
                           )
