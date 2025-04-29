FROM python:3.9

WORKDIR /app

# Copy files
COPY app.py .
COPY playbook.yml .
COPY ansible.cfg .

# Install required packages
RUN apt-get update && \
    apt-get install -y docker.io && \
    pip install flask ansible docker docker-py && \
    ansible-galaxy collection install community.docker

CMD ["python", "app.py"]

