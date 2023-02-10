Funnel
============

core:

It's a Django Application which contains views, urls, models and connectivity to the database.

`python manage.py makemigration`

This command will generate a set of migration files based on the changes you've made to your models.

Once you've generated the migrations, you can apply the changes to your database by running the following command:

`python manage.py migrate`

This will create the necessary tables in your database to match the models you've defined in your Django project.
