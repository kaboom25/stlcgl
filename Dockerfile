FROM python:3.6
COPY . /stlcgl

WORKDIR /stlcgl

RUN pip3 install -r requirements2.txt

EXPOSE 8052

CMD ["python3", "usage2.py"]