FROM python:3
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /usr/support
COPY requirements.txt /usr/support/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /usr/support/

#EXPOSE 8000
#
#CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000"]

#sudo chown -R $USER /home/user/PycharmProjects/support/data


