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

# Create a script to set up the SSH key and clone the repository
RUN echo "#!/bin/sh\n\
echo \"$SSH_PRIVATE_KEY\" > /AutoSploit/id_ed25519\n\
chmod 600 /AutoSploit/id_ed25519\n\
echo \"Host github.com\n  IdentityFile /AutoSploit/id_ed25519\n  StrictHostKeyChecking no\" > /root/.ssh/config\n\
git clone git@github.com:robchrob/AutoSploit.git .\n\
pip install -r requirements.txt" > setup_repo.sh && \
    chmod +x setup_repo.sh

# Run the setup script
RUN ./setup_repo.sh

# Set up tokens
RUN mkdir -p etc/tokens && \
    echo "NJbaiyQk3geZnSWTh3sM6ZEmBlxZb7x9" > etc/tokens/shodan.key && \
    echo "1ed16e20-87ec-47ca-b625-9d921e293893" > etc/tokens/censys.key && \
    echo "QsJJlRxpfaRl71CAhNEBvJ2fz0fAs5do" > etc/tokens/censys.id

# Expose the necessary ports
EXPOSE 4444

# Set the entrypoint
CMD [ "./entrypoint.sh" ]
