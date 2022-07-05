FROM centos/python-38-centos7

USER 0

# install necessary tools
RUN yum install unzip -y
RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py

# install headless chrome
RUN curl -O https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
RUN yum install google-chrome-stable_current_x86_64.rpm -y

# install selenium
RUN pip install selenium

# download chromedriver
RUN mkdir /opt/chrome
RUN curl -O https://chromedriver.storage.googleapis.com/103.0.5060.53/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip -d /opt/chrome

WORKDIR /app

# copy the testing python script
COPY selenium-with-headless-chrome.py .
RUN python selenium-with-headless-chrome.py
