FROM python:3.5

RUN apt update \
    && apt install -y --no-install-recommends \
        libpulse-dev \
        swig \
        libasound2-dev \
        build-essential \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

#ENV PULSE_SERVER=unix:/usr/src/app/pulseaudio/socket
ADD test* /usr/src/app/


CMD ["python", "test.py"]