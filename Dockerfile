FROM ubuntu:20.04
LABEL maintainer="zzhuang7@my.bcit.ca"
RUN apt-get update -y && apt-get install -y python3 python3-pip
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]