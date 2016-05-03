# FYP-Web - FLIN1
---
Website Part for News Update System

#### Basic Structure

The web server is built based on Django 1.9

Frontend webpage written in HTML *(Django Template)* + CSS+JS *(Bootstrap 2.0)*

---
#### Install Instruction

1. Make sure Python version >= 2.6

2. Install Server & Django & Database
`sudo apt-get install apache2 django postgresql python-psycopg2`

3. Properly Set Postgresql and Psycopg2, see [PostgreSql Wiki](https://wiki.debian.org/PostgreSql) for details

4. Install phpPgAdmin if you want UI for DB

5. Copy all codes to /var/www/ , all settings are included in the code

---
#### Places to Modify in Setting:

*fypsite/fypsite/settings.py*, line 80: change access information for your DB

*fypsite/mainapp/views.py*, line 13-14: change the Python ENV Path and Path to the crawling script

---
#### Misc:

For a short time, our DB is available at 54.201.171.89

To access DB: `http://54.201.171.89/phppgadmin/`

*ALL User&Pass is FYP*