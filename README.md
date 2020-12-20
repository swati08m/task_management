# import database(mongo)
mongorestore -d {{db_name}} db_dump/taskmanagement


# Execute task_management app
python manage.py runserver --settings=task_management.settings.local
