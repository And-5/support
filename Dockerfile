FROM python:3
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /usr/support
COPY requirements.txt /usr/support/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /usr/support/
