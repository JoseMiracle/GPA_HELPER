# Pull base image
FROM python:3.12.2-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set work directory called `app`
RUN mkdir -p /code
WORKDIR /code

# Install dependencies
COPY requirements.txt /tmp/requirements.txt

RUN set -ex && \
pip install --upgrade pip && \
pip install -r /tmp/requirements.txt && \
rm -rf /root/.cache/

# Copy local project
COPY . /code/

# Set the port number as an environment variable
ARG PORT=80
ENV PORT $PORT

# Expose the given port
EXPOSE $PORT

# Copy start.sh and give execution permissions
COPY start.sh /code/start.sh
RUN chmod +x /code/start.sh

CMD ["/code/start.sh"]