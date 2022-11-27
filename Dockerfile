FROM python:3
ADD datetime.py /
CMD [ "python3", "./datetime.py" ]
