# BlogDis

Application de blog développée avec **Django**.

## Prérequis
- Python 3.10 ou plus
- Git

## Installation (pour récupérer le projet)

```bash
# 1. Cloner le dépôt
git clone https://github.com/kamanoumichel/BlogDis.git
cd BlogDis

# 2. Créer et activer un environnement virtuel
python -m venv venv
# Windows :
venv\Scripts\activate
# macOS / Linux :
# source venv/bin/activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Appliquer les migrations (la base db.sqlite3 est déjà fournie)
python manage.py migrate

# 5. Lancer le serveur
python manage.py runserver
```

Le site est ensuite accessible sur : http://127.0.0.1:8000/

## Administration

Interface admin : http://127.0.0.1:8000/admin/

> Les identifiants de connexion sont fournis séparément (en privé).
