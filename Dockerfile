FROM python:3 as base

ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
COPY publish-schema-to-postman.py /code/

# Copy schema from local into container
COPY example.yml /code/

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/code/publish-schema-to-postman.py", "example.yml"]
