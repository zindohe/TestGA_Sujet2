# Test Growth Agence

## Français

Un programme en Python permettant de récupérer et stocker dans un Google Sheet à interval régulier toutes les entreprises citées dans un article pris au hasard sur https://www.maddyness.com/?s=MaddyMoney. 

### Prérequis

 - Python 3.7 ou plus récent
 - Un fichier `credentials.json` récupérable ici https://developers.google.com/sheets/api/quickstart/python et à placer dans le dossier `doc`
 - Un compte Google afin d'utiliser l'API Google Sheets et d'accèder au fichier

### Utilisation
```shell script
  py main.py
``` 
Le script va vous demander le jour de la semaine où vous souhaitez qu'il récupère les données, ainsi que l'heure.
 

## English

A Python program that get and write in a Google Sheet at a regular interval every company quoted in a random article on this page : https://developers.google.com/sheets/api/quickstart/python.

### Requirements

 - Python 3.7 or later
 - A file `credentials.json` that you can get here : https://developers.google.com/sheets/api/quickstart/python and you have to put it in the `doc` folder
 - A Google account to use the Google Sheets API and to access the file

### Usage
```shell script
  py main.py
``` 
The script will ask you at what day of the week you want it to run, and at what time.
 