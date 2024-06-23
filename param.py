import streamlit as st

def main():
    st.title("Explication des Paramètres")

    st.markdown(
        """
        ## Comprendre les Paramètres du Modèle ICMSF

        Voici une explication détaillée des paramètres utilisés dans l'outil de validation ICMSF FSO. Ces paramètres sont essentiels pour évaluer la sécurité microbiologique de votre processus de fabrication alimentaire.

        ### 1. Moyenne de la contamination initiale (log10 cfu/g)

        * **Signification:** Représente la moyenne du nombre de micro-organismes présents sur la matière première au début du processus de fabrication.
        * **Exemple:** Une valeur de -2,70 signifie qu'en moyenne, il y a 10^-2,70 cfu (unités formant colonie) par gramme de matière première.
        * **Définition:** L'industriel peut obtenir cette valeur en effectuant des tests microbiologiques sur des échantillons représentatifs de sa matière première. Il doit tenir compte des variations saisonnières, des sources d'approvisionnement et d'autres facteurs.

        ### 2. Écart type de la contamination initiale (log10 cfu/g)

        * **Signification:** Mesure la variabilité de la contamination initiale d'un lot de matière première à l'autre.
        * **Exemple:** Une valeur de 0,60 signifie qu'il y a une variabilité significative dans la contamination initiale.
        * **Définition:** L'industriel peut calculer cet écart type en analysant les données de ses tests microbiologiques sur la matière première. 

        ### 3. Moyenne de la réduction (log10 cfu/g)

        * **Signification:** Représente la réduction moyenne du nombre de micro-organismes obtenue par les mesures de contrôle appliquées dans le processus de fabrication.
        * **Exemple:** Une valeur de 1,40 signifie que le processus de fabrication réduit en moyenne le nombre de micro-organismes d'un facteur de 10^1,40.
        * **Définition:** L'industriel peut obtenir cette valeur en effectuant des études de validation de ses mesures de contrôle.

        ### 4. Écart type de la réduction (log10 cfu/g)

        * **Signification:** Mesure la variabilité de la réduction obtenue par les mesures de contrôle d'un lot de produit à l'autre.
        * **Définition:** L'industriel peut calculer cet écart type en analysant les données de ses études de validation de ses mesures de contrôle.

        ### 5. Moyenne de l'augmentation (log10 cfu/g)

        * **Signification:** Représente la croissance moyenne des micro-organismes qui peut se produire pendant le stockage et la distribution du produit.
        * **Définition:** L'industriel peut obtenir cette valeur en effectuant des études de croissance des micro-organismes dans des conditions de stockage et de distribution similaires à celles du produit.

        ### 6. Écart type de l'augmentation (log10 cfu/g)

        * **Signification:** Mesure la variabilité de la croissance des micro-organismes pendant le stockage et la distribution d'un lot de produit à l'autre.
        * **Définition:** L'industriel peut calculer cet écart type en analysant les données de ses études de croissance des micro-organismes.

        ### 7. Objectif de sécurité alimentaire (log10 cfu/g)

        * **Signification:** Niveau maximum de contamination acceptable dans le produit final pour garantir la sécurité alimentaire.
        * **Définition:**  L'objectif de sécurité alimentaire est défini par l'industriel en fonction des exigences réglementaires, des risques microbiologiques associés au produit et des risques pour la santé du consommateur.

        ### En Résumé

        L'industriel doit définir avec précision ces paramètres en se basant sur des données scientifiques et des tests rigoureux. Ces données lui permettent d'évaluer la robustesse de son processus de fabrication et de garantir que son produit respecte les objectifs de sécurité alimentaire.
        """
    )
