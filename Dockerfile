FROM python:3.10.9-bullseye

COPY main.py main.py
COPY requirements.txt requirements.txt
COPY chromedriver_linux64/chromedriver chromedriver_linux64/chromedriver
RUN pip3 install -r requirements.txt

# install google chrome
RUN apt update
RUN apt upgrade
RUN apt install wget
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

RUN apt-get install gdebi-core -y
RUN gdebi google-chrome-stable_current_amd64.deb
RUN apt-get install -f 
RUN ls
RUN cd chromedriver_linux64 && ls
RUN cd usr/bin && ls

# For the loss package
RUN apt-get install chromium -y
RUN ls
RUN cd usr/bin && ls

# set display port to avoid crash
ENV DISPLAY=:0

CMD [ "python3",  "main.py" ]
