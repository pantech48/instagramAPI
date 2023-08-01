# Start from a Python image.
FROM python:3.8

# Install your application
COPY . /app
WORKDIR /app

ENV INSTAGRAM_USERNAME="fillip.courte"
ENV INSTAGRAM_PASSWORD="Ll2207157"

RUN apt-get update && apt-get install -y \
  libglib2.0-0 \
  libnss3 \
  libgdk-pixbuf2.0-0 \
  libgtk-3-0 \
  libxss1 \
  libasound2
RUN pip install -r requirements.txt

# install google chrome
ARG CHROME_VERSION="114.0.5735.90-1"
RUN wget --no-verbose -O /tmp/chrome.deb https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}_amd64.deb \
  && apt install -y /tmp/chrome.deb \
  && rm /tmp/chrome.deb

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
