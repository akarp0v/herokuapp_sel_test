FROM python:3.9.5-slim

WORKDIR /congenica_task

COPY herokuapp herokuapp/

COPY conftest.py test_tasks_1_2_4.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update \
    && apt-get install --yes wget \
    && apt-get install --yes unzip \
    && apt-get install --yes curl \
    && rm -rf /var/lib/apt/lists/*

RUN wget -O /tmp/google-chrome-stable_current_amd64.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get update \
    && apt-get install --yes /tmp/google-chrome*.deb

RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/`curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ \
    && rm -rf /tmp/*

CMD pytest -vs --headless=yes
