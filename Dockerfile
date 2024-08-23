FROM python:3.9.19-alpine

# Set the working directory inside the container
WORKDIR /code 
COPY requirements.txt /code/
RUN pip install -r requirements.txt 
COPY . /code/
EXPOSE 5000
CMD [ "python", "myapp.py" ]