"""
    Fichier : gestion_enfants_sante_crud.py
    Auteur : OM 2021.05.01
    Gestions des "routes" FLASK et des données pour l'association entre les enfants et les parents.
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *

"""
    Nom : films_genres_afficher
    Auteur : OM 2021.05.01
    Définition d'une "route" /films_genres_afficher
    
    But : Afficher les enfants avec les parents associés pour chaque film.
    
    Paramètres : id_genre_sel = 0 >> tous les enfants.
                 id_genre_sel = "n" affiche le film dont l'id est "n"
                 
"""


@app.route("/films_genres_afficher/<int:id_film_sel>", methods=['GET', 'POST'])
def films_genres_afficher(id_film_sel):
    print(" films_genres_afficher id_film_sel ", id_film_sel)
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                strsql_genres_films_afficher_data = """SELECT id_enfants, Nom, Prenom, DateNaissance,
                                                            GROUP_CONCAT(Allergie) as EnfantsSante FROM t_enfants_sante
                                                            RIGHT JOIN t_enfants ON t_enfants.id_enfants = t_enfants_sante.fk_enfants
                                                            LEFT JOIN t_sante ON t_sante.id_sante = t_enfants_sante.fk_sante
                                                            GROUP BY id_enfants"""

                if id_film_sel == 0:
                    # le paramètre 0 permet d'afficher tous les enfants
                    # Sinon le paramètre représente la valeur de l'id du film
                    mc_afficher.execute(strsql_genres_films_afficher_data)
                else:
                    # Constitution d'un dictionnaire pour associer l'id du film sélectionné avec un nom de variable
                    valeur_id_film_selected_dictionnaire = {"value_id_enfants_selected": id_film_sel}
                    # En MySql l'instruction HAVING fonctionne comme un WHERE... mais doit être associée à un GROUP BY
                    # L'opérateur += permet de concaténer une nouvelle valeur à la valeur de gauche préalablement définie.
                    strsql_genres_films_afficher_data += """ HAVING id_enfants= %(value_id_enfants_selected)s"""

                    mc_afficher.execute(strsql_genres_films_afficher_data, valeur_id_film_selected_dictionnaire)

                # Récupère les données de la requête.
                data_genres_films_afficher = mc_afficher.fetchall()
                print("data_genres ", data_genres_films_afficher, " Type : ", type(data_genres_films_afficher))

                # Différencier les messages.
                if not data_genres_films_afficher and id_film_sel == 0:
                    flash("""La table "t_enfants" est vide. !""", "warning")
                elif not data_genres_films_afficher and id_film_sel > 0:
                    # Si l'utilisateur change l'id_enfants dans l'URL et qu'il ne correspond à aucun film
                    flash(f"Le film {id_film_sel} demandé n'existe pas !!", "warning")
                else:
                    flash(f"Données enfants et parents affichés !!", "success")

        except Exception as Exception_films_genres_afficher:
            raise ExceptionFilmsGenresAfficher(f"fichier : {Path(__file__).name}  ;  {films_genres_afficher.__name__} ;"
                                               f"{Exception_films_genres_afficher}")

    print("films_genres_afficher  ", data_genres_films_afficher)
    # Envoie la page "HTML" au serveur.
    return render_template("enfants_sante/enfants_sante_afficher.html", data=data_genres_films_afficher)


"""
    nom: edit_enfants_sante_selected
    On obtient un objet "objet_dumpbd"

    Récupère la liste de tous les parents du film sélectionné par le bouton "MODIFIER" de "enfants_sante_afficher.html"
    
    Dans une liste déroulante particulière (tags-selector-tagselect), on voit :
    1) Tous les parents contenus dans la "t_parents".
    2) Les parents attribués au film selectionné.
    3) Les parents non-attribués au film sélectionné.

    On signale les erreurs importantes

"""


@app.route("/edit_enfants_sante_selected", methods=['GET', 'POST'])
def edit_enfants_sante_selected():
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                strsql_genres_afficher = """SELECT id_sante, Allergie FROM t_sante ORDER BY id_sante ASC"""
                mc_afficher.execute(strsql_genres_afficher)
            data_genres_all = mc_afficher.fetchall()
            print("dans edit_enfants_sante_selected ---> data_genres_all", data_genres_all)

            # Récupère la valeur de "id_enfants" du formulaire html "enfants_sante_afficher.html"
            # l'utilisateur clique sur le bouton "Modifier" et on récupère la valeur de "id_enfants"
            # grâce à la variable "id_film_genres_edit_html" dans le fichier "enfants_sante_afficher.html"
            # href="{{ url_for('edit_enfants_sante_selected', id_film_genres_edit_html=row.id_enfants) }}"
            id_film_genres_edit = request.values['id_film_genres_edit_html']

            # Mémorise l'id du film dans une variable de session
            # (ici la sécurité de l'application n'est pas engagée)
            # il faut éviter de stocker des données sensibles dans des variables de sessions.
            session['session_id_film_genres_edit'] = id_film_genres_edit

            # Constitution d'un dictionnaire pour associer l'id du film sélectionné avec un nom de variable
            valeur_id_film_selected_dictionnaire = {"value_id_enfants_selected": id_film_genres_edit}

            # Récupère les données grâce à 3 requêtes MySql définie dans la fonction genres_films_afficher_data
            # 1) Sélection du film choisi
            # 2) Sélection des parents "déjà" attribués pour le film.
            # 3) Sélection des parents "pas encore" attribués pour le film choisi.
            # ATTENTION à l'ordre d'assignation des variables retournées par la fonction "genres_films_afficher_data"
            data_genre_film_selected, data_genres_films_non_attribues, data_genres_films_attribues = \
                genres_films_afficher_data(valeur_id_film_selected_dictionnaire)

            print(data_genre_film_selected)
            lst_data_film_selected = [item['id_enfants'] for item in data_genre_film_selected]
            print("lst_data_film_selected  ", lst_data_film_selected,
                  type(lst_data_film_selected))

            # Dans le composant "tags-selector-tagselect" on doit connaître
            # les parents qui ne sont pas encore sélectionnés.
            lst_data_genres_films_non_attribues = [item['id_sante'] for item in data_genres_films_non_attribues]
            session['session_lst_data_genres_films_non_attribues'] = lst_data_genres_films_non_attribues
            print("lst_data_genres_films_non_attribues  ", lst_data_genres_films_non_attribues,
                  type(lst_data_genres_films_non_attribues))

            # Dans le composant "tags-selector-tagselect" on doit connaître
            # les parents qui sont déjà sélectionnés.
            lst_data_genres_films_old_attribues = [item['id_sante'] for item in data_genres_films_attribues]
            session['session_lst_data_genres_films_old_attribues'] = lst_data_genres_films_old_attribues
            print("lst_data_genres_films_old_attribues  ", lst_data_genres_films_old_attribues,
                  type(lst_data_genres_films_old_attribues))

            print(" data data_genre_film_selected", data_genre_film_selected, "type ", type(data_genre_film_selected))
            print(" data data_genres_films_non_attribues ", data_genres_films_non_attribues, "type ",
                  type(data_genres_films_non_attribues))
            print(" data_genres_films_attribues ", data_genres_films_attribues, "type ",
                  type(data_genres_films_attribues))

            # Extrait les valeurs contenues dans la table "t_genres", colonne "intitule_genre"
            # Le composant javascript "tagify" pour afficher les tags n'a pas besoin de l'id_parents
            lst_data_genres_films_non_attribues = [item['Allergie'] for item in data_genres_films_non_attribues]
            print("lst_all_genres gf_edit_enfants_sante_selected ", lst_data_genres_films_non_attribues,
                  type(lst_data_genres_films_non_attribues))

        except Exception as Exception_edit_enfants_sante_selected:
            raise ExceptionEditGenreFilmSelected(f"fichier : {Path(__file__).name}  ;  "
                                                 f"{edit_enfants_sante_selected.__name__} ; "
                                                 f"{Exception_edit_enfants_sante_selected}")

    return render_template("enfants_sante/enfants_sante_modifier_tags_dropbox.html",
                           data_genres=data_genres_all,
                           data_film_selected=data_genre_film_selected,
                           data_genres_attribues=data_genres_films_attribues,
                           data_genres_non_attribues=data_genres_films_non_attribues)


"""
    nom: update_genre_film_selected

    Récupère la liste de tous les parents du film sélectionné par le bouton "MODIFIER" de "enfants_sante_afficher.html"
    
    Dans une liste déroulante particulière (tags-selector-tagselect), on voit :
    1) Tous les parents contenus dans la "t_parents".
    2) Les parents attribués au film selectionné.
    3) Les parents non-attribués au film sélectionné.

    On signale les erreurs importantes
"""


@app.route("/update_genre_film_selected", methods=['GET', 'POST'])
def update_genre_film_selected():
    if request.method == "POST":
        try:
            # Récupère l'id du film sélectionné
            id_film_selected = session['session_id_film_genres_edit']
            print("session['session_id_film_genres_edit'] ", session['session_id_film_genres_edit'])

            # Récupère la liste des parents qui ne sont pas associés au film sélectionné.
            old_lst_data_genres_films_non_attribues = session['session_lst_data_genres_films_non_attribues']
            print("old_lst_data_genres_films_non_attribues ", old_lst_data_genres_films_non_attribues)

            # Récupère la liste des parents qui sont associés au film sélectionné.
            old_lst_data_genres_films_attribues = session['session_lst_data_genres_films_old_attribues']
            print("old_lst_data_genres_films_old_attribues ", old_lst_data_genres_films_attribues)

            # Effacer toutes les variables de session.
            session.clear()

            # Récupère ce que l'utilisateur veut modifier comme parents dans le composant "tags-selector-tagselect"
            # dans le fichier "genres_films_modifier_tags_dropbox.html"
            new_lst_str_genres_films = request.form.getlist('name_select_tags')
            print("new_lst_str_genres_films ", new_lst_str_genres_films)

            # OM 2021.05.02 Exemple : Dans "name_select_tags" il y a ['4','65','2']
            # On transforme en une liste de valeurs numériques. [4,65,2]
            new_lst_int_enfants_sante_old = list(map(int, new_lst_str_genres_films))
            print("new_lst_enfants_sante ", new_lst_int_enfants_sante_old, "type new_lst_enfants_sante ",
                  type(new_lst_int_enfants_sante_old))

            # Pour apprécier la facilité de la vie en Python... "les ensembles en Python"
            # https://fr.wikibooks.org/wiki/Programmation_Python/Ensembles
            # OM 2021.05.02 Une liste de "id_parents" qui doivent être effacés de la table intermédiaire "t_enfants_sante".
            lst_diff_genres_delete_b = list(set(old_lst_data_genres_films_attribues) -
                                            set(new_lst_int_enfants_sante_old))
            print("lst_diff_genres_delete_b ", lst_diff_genres_delete_b)

            # Une liste de "id_parents" qui doivent être ajoutés à la "t_enfants_sante"
            lst_diff_genres_insert_a = list(
                set(new_lst_int_enfants_sante_old) - set(old_lst_data_genres_films_attribues))
            print("lst_diff_genres_insert_a ", lst_diff_genres_insert_a)

            # SQL pour insérer une nouvelle association entre
            # "fk_enfants"/"id_enfants" et "fk_sante"/"id_parents" dans la "t_enfants_sante"
            strsql_insert_enfants_sante = """INSERT INTO t_enfants_sante (id_enfants_sante, fk_sante, fk_enfants)
                                                    VALUES (NULL, %(value_fk_sante)s, %(value_fk_enfants)s)"""

            # SQL pour effacer une (des) association(s) existantes entre "id_enfants" et "id_parents" dans la "t_enfants_sante"
            strsql_delete_genre_film = """DELETE FROM t_enfants_sante WHERE fk_sante = %(value_fk_sante)s AND fk_enfants = %(value_fk_enfants)s"""

            with DBconnection() as mconn_bd:
                # Pour le film sélectionné, parcourir la liste des parents à INSÉRER dans la "t_enfants_sante".
                # Si la liste est vide, la boucle n'est pas parcourue.
                for id_genre_ins in lst_diff_genres_insert_a:
                    # Constitution d'un dictionnaire pour associer l'id du film sélectionné avec un nom de variable
                    # et "id_genre_ins" (l'id du genre dans la liste) associé à une variable.
                    valeurs_film_sel_genre_sel_dictionnaire = {"value_fk_enfants": id_film_selected,
                                                               "value_fk_sante": id_genre_ins}

                    mconn_bd.execute(strsql_insert_enfants_sante, valeurs_film_sel_genre_sel_dictionnaire)

                # Pour le film sélectionné, parcourir la liste des parents à EFFACER dans la "t_enfants_sante".
                # Si la liste est vide, la boucle n'est pas parcourue.
                for id_genre_del in lst_diff_genres_delete_b:
                    # Constitution d'un dictionnaire pour associer l'id du film sélectionné avec un nom de variable
                    # et "id_genre_del" (l'id du genre dans la liste) associé à une variable.
                    valeurs_film_sel_genre_sel_dictionnaire = {"value_fk_enfants": id_film_selected,
                                                               "value_fk_sante": id_genre_del}

                    # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
                    # la subtilité consiste à avoir une méthode "execute" dans la classe "DBconnection"
                    # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "DBconnection"
                    # sera interprété, ainsi on fera automatiquement un commit
                    mconn_bd.execute(strsql_delete_genre_film, valeurs_film_sel_genre_sel_dictionnaire)

        except Exception as Exception_update_genre_film_selected:
            raise ExceptionUpdateGenreFilmSelected(f"fichier : {Path(__file__).name}  ;  "
                                                   f"{update_genre_film_selected.__name__} ; "
                                                   f"{Exception_update_genre_film_selected}")

    # Après cette mise à jour de la table intermédiaire "t_enfants_sante",
    # on affiche les enfants et le(urs) genre(s) associé(s).
    return redirect(url_for('films_genres_afficher', id_film_sel=id_film_selected))


"""
    nom: genres_films_afficher_data

    Récupère la liste de tous les parents du film sélectionné par le bouton "MODIFIER" de "enfants_sante_afficher.html"
    Nécessaire pour afficher tous les "TAGS" des parents, ainsi l'utilisateur voit les parents à disposition

    On signale les erreurs importantes
"""


def genres_films_afficher_data(valeur_id_film_selected_dict):
    print("valeur_id_film_selected_dict...", valeur_id_film_selected_dict)
    try:

        strsql_film_selected = """SELECT id_enfants, Nom, Prenom, DateNaissance, GROUP_CONCAT(id_sante) as EnfantsSante FROM t_enfants_sante
                                        INNER JOIN t_enfants ON t_enfants.id_enfants = t_enfants_sante.fk_enfants
                                        INNER JOIN t_sante ON t_sante.id_sante = t_enfants_sante.fk_sante
                                        WHERE id_enfants = %(value_id_enfants_selected)s"""

        strsql_genres_films_non_attribues = """SELECT id_sante, Allergie FROM t_sante WHERE id_sante not in(SELECT id_sante as idGenresFilms FROM t_enfants_sante
                                                    INNER JOIN t_enfants ON t_enfants.id_enfants = t_enfants_sante.fk_enfants
                                                    INNER JOIN t_sante ON t_sante.id_sante = t_enfants_sante.fk_sante
                                                    WHERE id_enfants = %(value_id_enfants_selected)s)"""

        strsql_genres_films_attribues = """SELECT id_enfants, id_sante, Allergie FROM t_enfants_sante
                                            INNER JOIN t_enfants ON t_enfants.id_enfants = t_enfants_sante.fk_enfants
                                            INNER JOIN t_sante ON t_sante.id_sante = t_enfants_sante.fk_sante
                                            WHERE id_enfants = %(value_id_enfants_selected)s"""

        # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
        with DBconnection() as mc_afficher:
            # Envoi de la commande MySql
            mc_afficher.execute(strsql_genres_films_non_attribues, valeur_id_film_selected_dict)
            # Récupère les données de la requête.
            data_genres_films_non_attribues = mc_afficher.fetchall()
            # Affichage dans la console
            print("genres_films_afficher_data ----> data_genres_films_non_attribues ", data_genres_films_non_attribues,
                  " Type : ",
                  type(data_genres_films_non_attribues))

            # Envoi de la commande MySql
            mc_afficher.execute(strsql_film_selected, valeur_id_film_selected_dict)
            # Récupère les données de la requête.
            data_film_selected = mc_afficher.fetchall()
            # Affichage dans la console
            print("data_film_selected  ", data_film_selected, " Type : ", type(data_film_selected))

            # Envoi de la commande MySql
            mc_afficher.execute(strsql_genres_films_attribues, valeur_id_film_selected_dict)
            # Récupère les données de la requête.
            data_genres_films_attribues = mc_afficher.fetchall()
            # Affichage dans la console
            print("data_genres_films_attribues ", data_genres_films_attribues, " Type : ",
                  type(data_genres_films_attribues))

            # Retourne les données des "SELECT"
            return data_film_selected, data_genres_films_non_attribues, data_genres_films_attribues

    except Exception as Exception_genres_films_afficher_data:
        raise ExceptionGenresFilmsAfficherData(f"fichier : {Path(__file__).name}  ;  "
                                               f"{genres_films_afficher_data.__name__} ; "
                                               f"{Exception_genres_films_afficher_data}")
