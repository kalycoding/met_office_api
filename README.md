# MetAPI

## Backend Set up Instructions


Dockerize Django Application with docker-compose 

## Requirements

This module requires the following modules/libraries:

* [Docker](https://www.docker.com/get-started)
* [Docker-compose]
* Any version of Linux or Unix OS (Recommended and Optional)

## Installation

1. Install using the following the command
   ```docker-compose up -d --build```


# MetAPI
Download time-series of monthly, seasonal and annual values. Files can be downloaded in rank or year order.

in this project, i'm using the year order statistics data and Max Temp as the parameter,

you can download the Max Temp of the city of your choice. The data is in txt file and need some formatting before loading into the database



## To load metAPI data to database
I setup custom django management command which load the data into the database

I used pandas for loading the data into a dataframe and make some maninuplations, check the management code inside the code folder

1. ```docker-compose exec web python manage.py load_data -m england_data.txt -c England```

* -c args is the city name of the data you are loading
* -m args is the data file you are uploading



* It runs on localhost port 8000

* Swagger URL is /swagger

* To run the test

```docker-compose exec web python manage.py test```

* To see server logs
```docker-compose logs```
  
* To enter docker container shell
```sudo docker exec -ti <CONTAINER_ID> /bin/sh```

## The api endpoints

1. ```/api``` list all the Max Temp data of all regions
2. ```/api/{location}``` list all the Max Temp data of the specified location
