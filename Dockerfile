FROM openwhisk/actionloop-python-v3.7:6879887

ADD . /opt/COMPSs
ADD ./.ssh /root/.ssh
RUN chmod 600 /root/.ssh/id_rsa

RUN apt update && apt install -y ssh uuid-runtime python-pip default-jdk autotools-dev libtool gfortran xdg-utils build-essential libboost-serialization-dev libboost-iostreams-dev
RUN pip2 install dill guppy


ENV JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64

