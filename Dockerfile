FROM python:3.8

WORKDIR .

COPY ../requirements.txt .

RUN pip install -r requirements.txt

COPY ../src/ .

ENTRYPOINT ["python",  "fetchUrl.py"]

CMD ["no_config_specified"]