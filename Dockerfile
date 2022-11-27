FROM python:3
RUN pip install DateTime
ADD datetime.py /
CMD [ "python3", "./datetime.py" ]
