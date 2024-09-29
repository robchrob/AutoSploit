# Use the base image
FROM phocean/msf

# Copy the entrypoint.sh file
COPY "entrypoint.sh" .

# Install necessary packages
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

# Set the working directory
WORKDIR /AutoSploit

# Set the build argument for the private key
ARG SSH_PRIVATE_KEY

# Set up the SSH key and clone the repository
RUN mkdir -p /root/.ssh && \
    echo "${SSH_PRIVATE_KEY}" > /root/.ssh/id_ed25519 && \
    chmod 600 /root/.ssh/id_ed25519 && \
    echo "Host github.com\n  IdentityFile /root/.ssh/id_ed25519\n  StrictHostKeyChecking no" > /root/.ssh/config && \
    git clone git@github.com:robchrob/AutoSploit.git .

# Install the requirements
RUN pip install -r requirements.txt

# Set up tokens
RUN mkdir -p etc/tokens && \
    echo "NJbaiyQk3geZnSWTh3sM6ZEmBlxZb7x9" > etc/tokens/shodan.key && \
    echo "1ed16e20-87ec-47ca-b625-9d921e293893" > etc/tokens/censys.key && \
    echo "QsJJlRxpfaRl71CAhNEBvJ2fz0fAs5do" > etc/tokens/censys.id

# Expose the necessary ports
EXPOSE 4444

# Set the entrypoint
CMD [ "/Autosploit/entrypoint.sh" ]
