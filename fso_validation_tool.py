# app.py (fichier principal de l'application Streamlit)
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Menu de navigation
page = st.sidebar.radio("Navigation", ["Accueil", "Paramètres"])

if page == "Accueil":
    # ... (code de votre page principale)
st.set_page_config(page_title="Outil de Validation ICMSF FSO", layout="wide")

st.title("Outil de Validation ICMSF FSO")

st.markdown(
    """
    ## Bienvenue !

    Cet outil vous aide à valider vos objectifs de sécurité alimentaire (FSO) en utilisant l'équation ICMSF :

    **H0 - SR + SI ≤ FSO**

    où :

    * **H0:** Niveau de contamination initial
    * **SR:** Réduction obtenue par les mesures de contrôle
    * **SI:** Augmentation de la contamination pendant le stockage et la distribution
    * **FSO:** Objectif de sécurité alimentaire

    Cet outil prend en compte la variabilité de chaque facteur, ce qui vous permet d'évaluer la robustesse de votre processus pour atteindre le FSO.
    """
)

st.sidebar.header("Paramètres d'entrée")

# Définition des paramètres d'entrée pour H0, SR, SI
initial_contamination_mean = st.sidebar.number_input(
    "Moyenne de la contamination initiale (log10 cfu/g)", value=-2.5, step=0.1
)
initial_contamination_sd = st.sidebar.number_input(
    "Écart type de la contamination initiale (log10 cfu/g)", value=0.8, step=0.1
)

reduction_mean = st.sidebar.number_input(
    "Moyenne de la réduction (log10 cfu/g)", value=1.4, step=0.1
)
reduction_sd = st.sidebar.number_input(
    "Écart type de la réduction (log10 cfu/g)", value=0.5, step=0.1
)

increase_mean = st.sidebar.number_input(
    "Moyenne de l'augmentation (log10 cfu/g)", value=2.7, step=0.1
)
increase_sd = st.sidebar.number_input(
    "Écart type de l'augmentation (log10 cfu/g)", value=0.59, step=0.1
)

# Gestion de l'erreur pour fso
fso = st.sidebar.number_input(
    "Objectif de sécurité alimentaire (log10 cfu/g)", value=2.0, step=0.1
)
if not isinstance(fso, (int, float)):
    st.error("Veuillez entrer une valeur numérique valide.")
else:
    # Calcul de la distribution globale
    def calculate_distribution(h0_mean, h0_sd, sr_mean, sr_sd, si_mean, si_sd):
        # Génération d'échantillons aléatoires pour chaque paramètre
        h0_samples = np.random.lognormal(h0_mean, h0_sd, 10000)
        sr_samples = np.random.lognormal(sr_mean, sr_sd, 10000)
        si_samples = np.random.lognormal(si_mean, si_sd, 10000)

        # Calcul des niveaux de contamination finaux
        final_contamination_samples = h0_samples - sr_samples + si_samples

        return final_contamination_samples

    final_contamination_samples = calculate_distribution(
        initial_contamination_mean,
        initial_contamination_sd,
        reduction_mean,
        reduction_sd,
        increase_mean,
        increase_sd,
    )

    # Calcul de la proportion de produits non conformes
    non_compliant_proportion = (
        np.sum(final_contamination_samples > fso) / len(final_contamination_samples)
    )

    # Affichage des résultats
    st.header("Résultats")

    st.markdown(
        f"""
        * **Moyenne de la contamination finale:** {np.mean(final_contamination_samples):.2f} log10 cfu/g
        * **Écart type de la contamination finale:** {np.std(final_contamination_samples):.2f} log10 cfu/g
        * **Proportion de produits non conformes:** {non_compliant_proportion*100:.2f}%
        """
    )

    # Affichage du graphique de la distribution
    st.header("Distribution des niveaux de contamination finale")

    fig, ax = plt.subplots()
    ax.hist(final_contamination_samples, bins=50, edgecolor="black")
    ax.set_xlabel("Contamination finale (log10 cfu/g)")
    ax.set_ylabel("Fréquence")
    ax.axvline(fso, color="red", linestyle="--", label="FSO")
    ax.legend()

    st.pyplot(fig)

    # Explication des résultats
    st.markdown(
        """
        ### Interprétation des résultats

        La distribution montre la probabilité d'obtenir différents niveaux de contamination finale dans votre produit. La ligne rouge en pointillés représente le FSO. La zone sous la courbe à droite du FSO représente la proportion de produits qui ne respectent pas le FSO.

        Cet outil fournit une représentation visuelle de l'impact de la variabilité sur votre processus. Il vous permet d'identifier les domaines potentiels d'amélioration et de quantifier le risque de non-conformité avec le FSO.
        """
    )

    st.markdown(
        """
        ### Avertissement

        Cet outil est fourni à des fins éducatives uniquement. Il ne doit pas être utilisé pour prendre des décisions concernant la sécurité alimentaire sans consulter un professionnel qualifié en sécurité alimentaire.
        """
    )


elif page == "Paramètres":
    st.markdown("## Page des Paramètres")
    import param  # Importe le fichier param.py
    param.main()  # Exécute le code de param.py
