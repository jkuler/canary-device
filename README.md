## DEVICE SENSOR APPLICATION ABSTRACT
<p>When hundreds of thousands of hardware devices are concurrently uploading sensors data, performance, availability, 
and scalability are questions that needed to be answered while designing the infrastructure to sustain the system.</p>
<p>In this scenario, I choose to deploy the system on cloud service where scalability, and high availability can be provided within couple of minutes.  
The following graphic describes an integration infrastructure design where the application will be deployed</p>

<img src="https://storage.googleapis.com/josue-kula-static/design_abstract/josue-kula-Aws-design.svg" width="400" height="400" align="middle" />

## Installing packages
Before running , we need to install required packages from which application component has been built.
``` bash
# Clone the repository
$ git clone https://github.com/jkuler/canary-device.git sensorsdev

# create a virtual environment
$ cd sensorsdev && python3 -m venv virtualenv

# install packages
source ./virtualenv/bin/activate && ./virtualenv/bin/python -m pip install -r requirements.txt
```

## Database

In the architectural blueprint, we suggest that persistent data should be redundant with 2 or more database per availability zone.
However, for demo purpose, I'm using db.sqlite in order to easily run and test the app.
```python
# ../sensorsdev/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
### Make migrations before running the application
``` bash
(virualenv)youser@hostname:~$ cd sensorsdev && ./virtualenv/bin/python manage.py makemigrations

$ ./virtualenv/bin/python manage.py migrate
```
We have to make sure there's a newly created file named db.sqlite at the current directory

## Running sensor locally

```bash
(virualenv)youser@hostname:~$ cd sensorsdev && ./virtualenv/bin/python manage.py runserver
```
## Application config
As you can see at the file requirements .txt, we used django and django-rest-framework to create sensors device app.
In order to have an ubiquitous Datetime across end-user at different geographical location, we need to configure both
the server and django project to use UTC TIMEZONE.
However, for testing purpose, we choose to set the time at New York

```python
 # ../sensorsdev/settings.py
  TIME_ZONE = 'America/New_York'
  USE_TZ = True
``` 
Attention should also be paid at SECRET_KEY and DEBUG config setting that are exposed by default.
In real production ready application, we have to hide our SECRET_KEY and dynamically switch DEBUG
value in dev - production environment.

```python
SECRET_KEY = 'ik!81-q8usbm-oqwui*!oty+^3y$+8q8m#als$$_j)y%667y&5'
DEBUG = False # Debug mode is turned off by default to suggest production ready
``` 

Since the REst API resources in the application do not require authentication and the service functionality requires resources to
handle many request but not too many, we configured the projects to only accept 60 request per minutes (GET, POST, PUT, DELETE)

```python
REST_FRAMEWORK = {
 #....

 'DEFAULT_THROTTLE_RATES': {
        'anon': '60/minute'
    }
}
```





