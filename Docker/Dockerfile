FROM phocean/msf

COPY "entrypoint.sh" .

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

ARG SSH_PRIVATE_KEY

RUN mkdir -p /root/.ssh && \
    echo "${SSH_PRIVATE_KEY}" > /root/.ssh/id_ed25519 && \
    chmod 600 /root/.ssh/id_ed25519 && \
    echo "Host github.com\n  IdentityFile /root/.ssh/id_ed25519\n  StrictHostKeyChecking no" > /root/.ssh/config && \
    chmod +x entrypoint.sh && \
    git clone git@github.com:NullArray/AutoSploit.git && \
    pip install -r AutoSploit/requirements.txt

EXPOSE 4444
CMD [ "./entrypoint.sh" ]
