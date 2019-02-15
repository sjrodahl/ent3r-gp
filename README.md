# ent3r-gp

## Set up project using docker-compose

- Clone the repo and navigate to its root folder.
- Run the following commands:

```
docker-compose build

docker-compose run djangoapp python3 ent3r_gp/manage.py makemigrations pages # Initiate the database tables
docker-compose run djangoapp python3 ent3r_gp/manage.py migrate              # Apply the changes to the database
docker-compose run djangoapp python3 ent3r_gp/manage.py createsuperuser      # Create root user. Follow prompts to set username and password

# Add the activities from the provided csv-file
docker-compose run djangoapp python3 ent3r_gp/manage.py add_activities mentor-gp-activities.csv
# Add the users from the provided csv-file
docker-compose run djangoapp python3 ent3r_gp/manage.py add_users kontaktinfo_mentorer.csv
# Add the mentor pairs. Note that the last names need to correspond to the users registered in the app.
docker-compose run djangoapp python3 ent3r_gp/manage.py add_pairs mentorpar.csv

#Start the application in detached mode
docker-compose up -d
```


## For production

- Set DEBUG = False
- Write a secret key in a file and load it in settings.py
- Set the ALLOWED_HOSTS variable in settings.py
- run python check --deploy for an additional check
- add users by running the command: python manage.py add_users <path to kontaktinfo_mentorer.csv>
- add activities by running the command python.py add_activities <path to mantor_gp_activities.csv>
  
