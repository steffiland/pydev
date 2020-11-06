FROM python:3

WORKDIR /src
ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .
EXPOSE 5000 5678
#CMD [ "python", "./server.py" ]
CMD ["flask", "run"]