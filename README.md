## DEVICE SENSOR APPLICATION ABSTRACT
<p>When hundreds of thousands of hardware devices are concurrently uploading sensors data, performance, availability, 
and scalability are questions that needed to be answered while designing the infrastructure to sustain the system.</p>
<p>In this scenario, I choose to deploy the system on cloud service where scalability, and high availability can be provided within couple of minutes.  
The following graphic describes an integration infrastructure design where the application will be deployed</p>

<img src="https://00e9e64bac8c14528b3efd337bfa8c615acf7f58d6aa53fecf-apidata.googleusercontent.com/download/storage/v1/b/josue-kula-static/o/design_abstract%2Fjosue-kula-aws-design.png?qk=AD5uMEsiScUkK8nDz7Q-yDRqEi5bBmGgpLPeOd_XrRk50e4D0GZZx8wn6Cdj7kARLT8v0V2_oqywx1GdF5Em8Ib6lbaTgDNqmdq7K9pplxqweakTl7pBRytM9Uy6yQ-aQRzev9to2a_pcu-CzTas8FDtrHigqwe27mdUD93aMuRvGy_hKhct2X0yc5QyRLhKdWwT7CxIrGqNhlcaeotnSktow6qlTWq6FF5WhgKKjiXXJ9hcSWM7oT8QSNs1958aW0WnguU_dJtG1ftkW0JETwsyBKcOddGPDw7VzYIhcq1VjLAaC1eZUs2KXHhZPFjPExru5aWppiGOe-pttyovvIvBzjRsqb8EBcABwyM_cjTgV_rV2yXsW0MC7-HtoPeOnbAkKeYvCxnIDrIWfZGcChAtGAJ-9CPyg9eqI1LCuUZ2jEQcSFi7cmyQI5YrXaRHr85Dtnh_SUo1i51yt7sSY7qHiU1owOwtMnRXlGKg9O3vjq_2vzQjb-Ixk6tfZk6SZ58f62tn08sqX-kP5M9DsmoJrUenrAYRGpBBK6_mjhefhuMT2pIp37y4hEh72eq4M18Y95JbIYfIJ-N1gz0D227dBQMoxbXIWXFEn_Q7lS_uV4XfLF9m8hcl9roT0ZPwDWgHyZD6bw3wsiHEELWKP8ztkOe-2OkMZbgpWwvbdRK1q3Jb8soprFocTistaogj5Us3P-HIJbAJEeC7o5HpvolsLWZMi8YYzXtk4rLA0wLG6pCVl7i8Mp4sv-WVKgB5eIDwteCW6DXOx_mjRI2WIRNsJtH2eNXs5x6UoDd4Q0KVU1wzM81NqeZ-BS88_iOj-UjCoWDfbaNnJI3kiVJn9MS9uaXA1VSrIg" width="400" height="400" align="middle" />

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

In architecture abstract, we suggest that persistent data should be redundant with 2 or more database per availability zone.
However, for demo purpose, I'm using db.sqlite in order to easily run and test the app.
```python
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
We have to make sure there's a newly created file db.sqlite at the current directory







