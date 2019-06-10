FROM python:3.6

WORKDIR /srv

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 1234

CMD /bin/bash
