FROM python:3.6
COPY . /stlcgl

RUN pip3 install virtualenv
RUN cd /stlcgl && virtualenv -p python3 env
RUN cd /stlcgl && \
    . env/bin/activate && \
    pip3 install -r requirements2.txt

EXPOSE 8052

CMD ["python3", "usage2.py"]