FROM python:3.8.5

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /car_booking_app

# Set the working directory to /car_booking_app
WORKDIR /car_booking_app

# Copy the current directory contents into the container at /car_booking_app
ADD . /car_booking_app/

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

CMD sh init.sh && pytest && python3 manage.py runserver 0.0.0.0:8000
