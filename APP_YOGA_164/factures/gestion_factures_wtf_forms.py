"""
    Fichier : gestion_factures_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjouterFactures(FlaskForm):
    """
        Dans le formulaire "facture_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    montant_factures_regexp = ""
    montant_facture_wtf = StringField("Ajouter le montant de la facture", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(montant_factures_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    date_factures_wtf = DateField("Date de la facture", validators=[InputRequired("Date obligatoire"),
                                                                                 DataRequired("Date non valide")])
    submit = SubmitField("Enregistrer la facture")


class FormWTFUpdateFactures(FlaskForm):
    """
        Dans le formulaire "factures_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    montant_factures_update_regexp = ""
    montant_facture_update_wtf = StringField("Montant du parent ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(montant_factures_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])
    date_facture_update_wtf = DateField("Date de naissance", validators=[InputRequired("Date obligatoire"),
                                                                                 DataRequired("Date non valide")])
    submit = SubmitField("Update parent")


class FormWTFDeleteFactures(FlaskForm):
    """
        Dans le formulaire "factures_delete_wtf.html"

        nom_facture_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_factures".
    """
    montant_facture_delete_wtf = StringField("Effacer ce genre")
    submit_btn_del = SubmitField("Effacer genre")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
