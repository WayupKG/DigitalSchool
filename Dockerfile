FROM python:3.10-alpine3.16

COPY requirements.txt /temp/requirements.txt
RUN pip3 install -r /temp/requirements.txt

COPY src /var/www/el-school
WORKDIR /var/www/el-school

EXPOSE 8000

RUN adduser --disabled-password el-user
USER el-user