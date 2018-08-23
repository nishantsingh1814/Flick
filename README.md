# Flick

# Django+React+Redux+Celery+PostGre

# Installation
for running the project you just need to copy this executable file to your ubuntu system https://github.com/nishantsingh1814/react-test/blob/master/Flick.sh
and run chmod u+x Flick.sh in command line from where you have copied this file. and then you just need to execute the file by ./Flick.sh and it'll do the setup required and start the project at http://127.0.0.1:8000 further directons are given below

3 supervisor services will be started i.e. 

1. flick (the main django react server)
2. celery (celery for async tasks)
3. flick_redis 

you can stop these service by: 
sudo supervisorctl stop < service_name >

When you first start the project you need to hit http://127.0.0.1:8000/group in a browser window or postman so that the downloading of group and images starts asynchronously 

![alt Login](https://raw.githubusercontent.com/nishantsingh1814/Flick/master/Screenshots/group_download.png)

Then go to http://127.0.0.1:8000 you will see the below page for login 
but first you need to signup so click on sigup it will get you to signup page

![alt Login](https://raw.githubusercontent.com/nishantsingh1814/Flick/master/Screenshots/Login.png)

![alt Login](https://raw.githubusercontent.com/nishantsingh1814/Flick/master/Screenshots/Signup.png)

After logging in you will see th below group page

![alt Login](https://raw.githubusercontent.com/nishantsingh1814/Flick/master/Screenshots/Groups.png)

Click on group and it will take you to Galllery page shown below which will show all the images in that group
![alt Login](https://raw.githubusercontent.com/nishantsingh1814/Flick/master/Screenshots/Gallery.png)

also it's infinite scrollable
![alt Login](https://raw.githubusercontent.com/nishantsingh1814/Flick/master/Screenshots/InfiniteScroll.png)

click on any image it will show you more details about that image
![alt Login](https://raw.githubusercontent.com/nishantsingh1814/Flick/master/Screenshots/Image.png)

Click on overview will show the charts of no. of api calls made by user in each of his session and also the chart of top 9 photo's comments count v/s sum of all other photo's comments count
![alt Login](https://raw.githubusercontent.com/nishantsingh1814/Flick/master/Screenshots/Overview.png)

#To get images of any other group than the one available in project 
you can go to Flick/flick/flick/views.py
and change or add the groupid from flickr in to class DownloadGroups > groupIds

More updates will come soon!!!
