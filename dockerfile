FROM python:3.8

RUN apt update && apt install -y \
    gcc g++ \
    python3-dev python3-pip \
    make \
    git \
    build-essential \
    libsm6 libxext6 libxrender-dev libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev libgl1-mesa-glx \
    libomp-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install pip --upgrade

COPY ./requirements.txt /
RUN pip3 install -r /requirements.txt


COPY ./ /app
WORKDIR /app
RUN bash jdk.sh

ENTRYPOINT streamlit run app.py
