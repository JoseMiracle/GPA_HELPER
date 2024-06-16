# Base image
FROM python:3.12.2-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /buddy

RUN addgroup --system django \
    && adduser --system --ingroup django django


COPY --chown=django:django ./devops/server.sh /server.sh
RUN sed -i 's/\r$//g' /server.sh
RUN chmod +x /server.sh


ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD . .