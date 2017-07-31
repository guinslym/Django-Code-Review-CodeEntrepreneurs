### Code Review
This application will help users to choose a course. A user will be able to View all the courses available and he is able to register to a course. 

### Installation

Continuum anaconda
```shell
conda create -n django1_11 python=3.5
activate django1_11

#remove django1_11 # for deleting the virtual environment
```
virtualenv 
```
which python3
>> /usr/local/bin/python3
virtualenv django1_11 --python=/usr/local/bin/python3
````
```
pip install -r requirements/development.txt --no-cache-dir
```

Running Test
```
py.test
```

Server
```
python manage.py runserver
```

## Project Folder
```
(django1_11) λ tree /A
Folder PATH listing
Volume serial number is 86FE-9FB3
C:.
+---applications
|   +---elearning
|   |   +---migrations
|   |   +---templates
|   |   |   +---course_registration
|   |   |   +---elearning
|   |   |   +---friends
|   |   |   +---robots_and_errors
|   |   |   \---userprofile
|   |   +---templatetags
|   |   +---tests
|   |   |   +---functionnal
|   |   |   +---unittest
|   |   +---utils
|   |   +---views
+---fixtures
+---logs
+---main
+---media
+---requirements
+---settings
+---static
+---TODO-wireframe-ERD
+---utils

The most important folder are **main** and **settings**

```
	**application**: contains all the applications (in this case only contains one app called elearning)
	**fixtures**: may or may not contains my fixtures
	**logs**: contains my logs
	**main**: THIS IS THE PROJECT FOLDER
	**media**: contains my media files
	**requirements**: contains my requirements
	**settings**: CONTAINS MY SETTINGS FOR DIFFERENTS ENVIRONMENT
	**static**: contains my static
	**wireframe-erd-todo**: contains my todo wireframe


### User password
```
username:codereview
password:okyoutube
````

### Admin password
```
username:mycodereview
password:okyoutube
```
