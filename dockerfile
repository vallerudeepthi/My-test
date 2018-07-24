FROM python:2
WORKDIR /usr/src/app
RUN pip install MySQL-python
COPY . .
CMD ["python","./test.py"]

