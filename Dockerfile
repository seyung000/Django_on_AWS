FROM python:3.13-slim

RUN apt update && \
    apt install -y nginx pkg-config default-libmysqlclient-dev build-essential && \
    rm -rf /var/lib/apt/lists/*

COPY ./django_server /app
COPY ./nginx_server/default.conf /etc/nginx/conf.d/default.conf

WORKDIR /app

RUN pip install -r requirements.txt

ENV SECRET_KEY='django-insecure-$tm$963@c8qzd1v^w@9)dxtb!&92wprj2x7((_!&+9++v*s@7u'
ENV DEBUG=True

COPY run.sh .
RUN chmod +x run.sh
CMD ["./run.sh"]