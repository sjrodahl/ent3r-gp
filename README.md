# ent3r-gp

## For production

- Set DEBUG = False
- Write a secret key in a file and load it in settings.py
- Set the ALLOWED_HOSTS variable in settings.py
- run python check --deploy for an additional check
- add users by running the command: python manage.py add_users <path to kontaktinfo_mentorer.csv>
- add activities by running the command python.py add_activities <path to mantor_gp_activities.csv>
  
