# Contact form 

This app collects messages from everybody granted that their input data meets the criteria specified in the task.

## How I did it
One of the requirements stated that I need to have API and HTML way of data submission, so wanted to stay DRY. I've used serializers as a form with a little bit of customization to suit my needs. 
The form is rendered via function and the data is sent by js func to viewset endpoint that has permissions. Thanks to that admin users can have full control over the data not only in the admin panel but in API/REST GUI also. Additionally, I've added pagination and filtration on the API and in the admin panel for ease of use. 

Code is commended with my thought process and arguments for why I'm doing what I'm doing. 

## How to run it. 

To run this you need to have docker so make sure that you have it 

Download and open the repo in your code editor 
run docker-compose up
This will take care of everything, I've put some commands in 
```
entrypoint.sh
```
file, however, if you don't have applied migrations make sure your docker is running and In a separate terminal opened on the level where the manage.py is, so in the app folder do 
```
docker-compose exec app_django python manage.py test
```
## Admin 
If you want to test out the admin functions open a new terminal and go to the app folder. Make sure your docker is running and input 
```
docker-compose exec app_django python manage.py createsuperuser
```
or if you want to you can put 
```
python manage.py createsuperuser
```
in the command section of the docker-compose 

## Tests
There are test you can run them when the docker is running in new terminal in app folder by 
```
docker-compose exec app_django python manage.py test
```
Thats it, hope you like it