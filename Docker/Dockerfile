FROM phocean/msf


RUN apt-get update && \
    apt-get install -y gnupg && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3B4FE6ACC0B21F32 && \
    echo "deb http://archive.ubuntu.com/ubuntu/ bionic main universe" >> /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y \
        git \
        python-dev \
        python-pip \
        apache2

COPY "entrypoint.sh" .

ARG SSH_PRIVATE_KEY

RUN mkdir -p /root/.ssh && \
    echo "${SSH_PRIVATE_KEY}" > /root/.ssh/id_ed25519 && \
    chmod 600 /root/.ssh/id_ed25519 && \
    echo "Host github.com\n  IdentityFile /root/.ssh/id_ed25519\n  StrictHostKeyChecking no" > /root/.ssh/config && \
    chmod +x entrypoint.sh && \
    git clone git@github.com:robchrob/AutoSploit.git && \
    pip install -r AutoSploit/requirements.txt

# Set up tokens
RUN mkdir -p AutoSploit/etc/tokens && \
    echo "NJbaiyQk3geZnSWTh3sM6ZEmBlxZb7x9" > AutoSploit/etc/tokens/shodan.key && \
    echo "1ed16e20-87ec-47ca-b625-9d921e293893" > AutoSploit/etc/tokens/censys.id && \
    echo "QsJJlRxpfaRl71CAhNEBvJ2fz0fAs5do" > AutoSploit/etc/tokens/censys.key

EXPOSE 4444
CMD [ "./entrypoint.sh" ]
