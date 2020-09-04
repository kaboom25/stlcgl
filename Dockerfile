FROM python:alpine3.6
COPY . /stlcgl
WORKDIR /stlcgl
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./usage2.py