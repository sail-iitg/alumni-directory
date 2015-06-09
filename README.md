## Alumni Directory - SAIL

Alumni directory is a website to allow alumni of an institute to search other's profiles. This project works alongside SAIL database collection drive.

#### Installation
The website runs on Python and Django with MySql database. Visit [MySql](http://www.mysql.com/downloads/) downloads page to install its latest version. Visit [Python](https://www.python.org/downloads/) downloads page to install version **2** of Python.

Django and other requirements can be installed using 'pip', a package manager for Python. To use pip, go to the project's folder to find requirements.txt and run the following command as administrator:

```
pip install -r requirements.txt
```

#### Setting up database
Create a mysql database with a name of your choice (default name is 'alumniDB'). This [tutorial](https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial) by Digital Ocean might be useful. To let the project know the name of the database, it can be specified under DATABASES variable in `directory/settings.py`.

If there is an existing database which needs to be imported into the newly created database, the absolute path to the '.sql' file can be specified under PATH_TO_DATABASE_IMPORT variable in settings.py.

#### Migrating database
Once the database is set up, migrations can be made by running the following command in the project's folder:
```
python manage.py migrate
```
To access Django's admin panel, it requires to create a super user:
```
python manage.py createsuperuser
```

#### All set up!
To run the server in an address and port of your choice, use the following command (without < > symbols):
```
python manage.py runserver <address>:<port>
```

Or to run locally, use:
```
python manage.py runserver
```
In this case, the website can be accessed at 'localhost:8000' in the browser.

##### Django Documentation
For additional support on the project, refer to Django's well-written [documentation](https://docs.djangoproject.com/en/1.8/).
