FROM python:3.10.9-bullseye

COPY chromedriver_linux64/chromedriver chromedriver_linux64/chromedriver
COPY chromedriver_linux64/chromedriver usr/bin/chromedriver

# install google chrome
RUN apt update
RUN apt upgrade
RUN apt install wget
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

RUN apt-get install gdebi-core -y
RUN gdebi -n google-chrome-stable_current_amd64.deb
RUN apt-get install -f 

# For the loss package
# RUN apt-get install chromium -y

# extra libraries
RUN apt-get install -y libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1


# set display port to avoid crash
ENV DISPLAY=:0

RUN ls
RUN cd usr/bin && ls
RUN google-chrome --version


COPY main.py main.py
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


CMD [ "python3",  "main.py" ]
