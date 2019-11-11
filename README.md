
# Job Monitor Service
Machine Problem: Job Monitor     

 A REST API which handles the job monitoring

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

First you need to install the docker

download docker on https://www.docker.com/

then fork this project
```
git clone https://github.com/J0hnZMT/jobmonitorservice
```
## To Build the docker

type in the command line
```
docker build -t job_monitor .
```
## To run in the docker container

type in the command line
```
docker container run job_monitor
```
## create database

copy and paste in the command line from sql-script.txt
```
CREATE DATABASE test_db
```
## Update the database-url 

update the database-url env in .env
```
DATABASE_URL= postgres://(username in db):(password)@host.docker.internal:5432/test_db
```
## Using the API
using GET
```
http://172.0.0.1:8000/modulelog/
```
using GET with job id
```
http://172.0.0.1:8000/modulelog/<job_id>
```

## Author
**Johnzel Tuddao** - *Initial work* - [J0hnZMT](https://github.com/J0hnZMT)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

