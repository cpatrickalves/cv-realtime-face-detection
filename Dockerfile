FROM python:3.7-slim

ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

ENV TZ America/Sao_Paulo

WORKDIR /app

ENV PACKAGES \
        libsm6 \
        libxext6 \
        libxrender-dev \
        libglib2.0-0

COPY requirements.txt /tmp/requirements.txt

RUN set -ex \
    && apt-get update -yq \
    && apt-get install -yq --no-install-recommends ${PACKAGES} \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --prefer-binary -r /tmp/requirements.txt \
    && find / -name *.pyc -delete \
    && apt-get clean \
    && mkdir -p /app/uploads \
    && mkdir -p /app/images \
    && mkdir -p /app/cascades \
    && rm -rf \
        /var/lib/apt/lists/* \
        /tmp/* \
        /var/tmp/* \
        /usr/share/man \
        /usr/share/doc \
        /usr/share/doc-base \
        /var/cache/* \
        /var/lib/dpkg/info/* \
        /var/log/*

EXPOSE 80

COPY face_recognition.py app.py /app/
ADD ./uploads /app/uploads
ADD ./images /app/images
ADD ./cascades /app/cascades

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port", "80"]