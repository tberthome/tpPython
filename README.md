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

Pour l'ensemle de l'application nous avons utilisé le jeu de données sans erreurs fournis dans le fichier 'Climat.xlsx' .

-   Pour notre application nous somme partis sur une interface console qui permet d'accéder aux différentes fonctionnalités créées : <br>
    ![alt text](https://github.com/tberthome/tpPython/blob/main/image/Capture1.PNG?raw=true)

-   Nous pouvons premièrement choisir la partie statistique qui nous affichera des données selon le mois sélectionné : <br>
    ![alt text](https://github.com/tberthome/tpPython/blob/main/image/CaptureMoyenne.PNG?raw=true) <br>
    Pour cette partie nous appliquons la méthode describe() sur la colonne ('mois') sélectionnée par l'utilisateur. Cela nous retourne le total, la moyenne, l'écart-type, la valeur minimum et maximum en excluant les valeurs vide, null ou en erreur pour éviter de fausser le résultat.

-   Nous avons ensuite la partie diagramme ou l'on peut choisir d'afficher sois un seul diagramme pour un mois rentré, des diagrammes pour les 12 mois ou un pour l'année : <br>
    ![alt text](https://github.com/tberthome/tpPython/blob/main/image/CaptureDia.PNG?raw=true) <br>
    Pour cette partie nous avons exclu les valeurs vide, null ou en erreur afin de ne pas fausser les résultats. Pour réaliser les graphiques nous utilisons la librairie matplot qui les génèrent automatiquement en fonction des données en entrées et de la configuration renseignée.

-   Pour finir nous avons une partie sur l'affichage des capitales qui nous affichera dans l'ordre les capitales avec leur différence de moyenne comparé aux fichier à tester. <br>
    ![alt text](https://github.com/tberthome/tpPython/blob/main/image/CaptureCapit.PNG?raw=true) <br>
    Cette déduction est réaliser en calculant la différence de degré de température de chaque mois de chaque capitale européenne avec les données de 'Cimat.xlsx'. On réalise ensuite la somme de ces différences, regroupés par capitale. La capitale ayant la plus petite valeur correspond aux données climatiques de 'Climat.xlsx'. Les températures de références des capitales européennes proviennent du fichier 'city_temperature.csv'. Ces données ont d'abord été traiter et corriger avant de servir :

1. Dans un premier temps on sélectionne uniquement les capitales européennes
2. Ensuite on supprimer les colonnes inutiles : 'Region', 'State', 'Country' pour ne garder que les colonnes : 'Capital', 'Day', 'Month', 'Year' et 'Temperature'
3. On observe et supprime les erreurs dans les températures (-99.0)
4. On sélectionne uniquement l'année 2018 qui correspond aux températures de tests
5. On convertit les températures qui sont en fahrenheit en Celsius
   Ensuite on peut faire les comparaisons avec les données à tester.

## Réponse aux questions

1. Les données corrigées sont elles proches des valeurs sans erreur ?

Pour corriger les données nous avons décidé de prendre les données du jours précédent ainsi que le jours suivant et d'en faire une moyenne. Les données retournées sont assez proches du réel avec des variations de 1 à 2 degrés généralement.

2. A partir de données opendata, retrouver le type de climat. Reprendre les données typiques d'une localisation proche fournies en complément, comparer les écarts. Qu'en concluez vous ?

On remarque des variation entre chaque mois allant de 2 à plus de 8 degrés de différence. On peut donc en conclure que d'un pays proche à l'autre la différence de température est assez importante et/ou que les données climatiques des températures sont très sensibles et peuvent varier d'une station à l'autre.
