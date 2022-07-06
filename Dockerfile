FROM centos/python-38-centos7

ARG EMPLOYEE_NO
ARG PSWD

ENV EMPLOYEE_NO $EMPLOYEE_NO
ENV PSWD $PSWD

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

VOLUME [ "/screenshots" ]

# for cron #####
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \
systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;

VOLUME [ "/sys/fs/cgroup" ]

RUN yum install -y cronie && yum clean all

RUN rm -rf /etc/localtime
RUN ln -s /usr/share/zoneinfo/Singapore /etc/localtime

RUN crontab -l | { cat; echo "0 9 * * mon,tue,wed,thu,fri /opt/app-root/bin/python /app/selenium-with-headless-chrome.py"; } | crontab -
RUN crontab -l | { cat; echo "0 18 * * mon,tue,wed,thu,fri /opt/app-root/bin/python /app/selenium-with-headless-chrome.py"; } | crontab -

RUN echo EMPLOYEE_NO=$EMPLOYEE_NO >> /etc/environment
RUN echo PSWD=$PSWD >> /etc/environment
# for cron #####

WORKDIR /app

# copy the testing python script
COPY selenium-with-headless-chrome.py .

# CMD [ "python", "selenium-with-headless-chrome.py" ]
CMD ["/usr/sbin/init"]
