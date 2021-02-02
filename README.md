# Projet | Analyse de données météorologique

## Consignes

Utiliser par exemple Python Scipy pour les parties mathématiques

-   Pour l’ échantillon SI, calculez la moyenne par mois, l'écart type par mois, la valeur min/max par mois et par année
-   Tracer les courbes de chaque mois avec une bibliothèque graphique python
-   Assembler les courbes sur un seul graphique (J1 -> J365)
-   Présenter la valeur lue en parcourant la courbe à l'aide du pointeur
-   Présenter les valeurs précédentes par mois et par année, par mois glissant de 30 jours centré sur la valeur lue
-   Recommencez avec le jeu SI-erreur après avoir corrigé les valeurs en erreur. Précisez vos méthodes. Les données corrigées sont elles proches des valeurs sans erreur ?
-   A partir de données opendata, retrouver le type de climat. Reprendre les données typiques d'une localisation proche fournies en complément, comparer les écarts. Qu'en concluez vous ?
-   De quelle la capitale européenne avez vous eu les données.

Outils : à utiliser Python + matplotlib, Jupyter éventuellement. Pas de R ni d’autre langage autorisés Evaluation:
Démonstration des solutions techniques et argumentation sur les méthodes utilisées

## Configuration

Python et pip doivent être installés

Depuis un noveau répertoire, cloné le dépot et lancer la commande : pip install -r requirements.txt ou py -m pip install -r requirements.txt

Télécharger le jeu de données 'Climat.xlsx' (Fournis avec les consignes) et 'city_temperature.csv' (https://www.kaggle.com/sudalairajkumar/daily-temperature-of-major-cities?select=city_temperature.csv) et déplacer les à la racine de votre répertoire

Lancer ensuite la ligne de commande 'py tp.py' pour exécuter le programme

## Fonctionnement

Des choix vous sont proposés afin d'accéder aux différentes fonctionnalités.

1. Vous pouvez afficher la moyenne (med), l'écart-type (std), la valeur minimum (min) et maximum (max) du mois que vous renseigner.

2. Vous accéder aux graphiques

-   Vous affichez le graphique du mois renseigné
-   Vous affichez les graphiques de chaque mois
-   Vous affichez le graphique sur une année

3. Vous afficher la capitale européenne correspondante aux température du fichier 'Climat.xlsx'.

## Démarche

Pour notre application nous somme partis sur une interface console qui nous propose plusieur alternative.
![alt text](https://github.com/tberthome/tpPython/blob/main/image/Capture1.PNG?raw=true)

Nous pouvons premièrement choisir la partie statistique qui nous enverra des données par mois sur le fichier à tester.

![alt text](https://github.com/tberthome/tpPython/blob/main/image/CaptureMoyenne.PNG?raw=true)

Nous avons ensuite la partie diagramme ou l'on peut choisir d'afficher sois un seul diagramme pour un mois rentré, des diagrammes pour les 12 mois ou un pour l'année.

![alt text](https://github.com/tberthome/tpPython/blob/main/image/CaptureDia.PNG?raw=true)

Pour finir nous avons une partie sur l'affichage des capitales qui nous affichera dans l'ordre les capitales avec leur différence de moyenne comparé aux fichier à tester.

![alt text](https://github.com/tberthome/tpPython/blob/main/image/CaptureCapit.PNG?raw=true)

Cette déduction est réaliser en calculant la différence de degré de température de chaque mois de chaque capitale européenne avec les données de 'Cimat.xlsx'. On réalise ensuite la somme de ces différences, regroupés par capitale. La capitale ayant la plus petite valeur correspond aux données climatiques de 'Climat.xlsx'.

## Réponse aux questions

1. Les données corrigées sont elles proches des valeurs sans erreur ?

Pour corriger les données nous avons décidé de prendre les données du jours précédent ainsi que le jours suivant et d'en faire une moyenne. Les données retournées sont assez proches du réel.


