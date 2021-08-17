#Docker file for EuroAPI(AKA API_Euro)

#Base image
FROM python:3.9.5

#Folder in container
WORKDIR /api

#Copy files to container
ADD . /api/

# install requirements
RUN pip install -r requirements.txt

#program start
CMD ["python","server.py"]