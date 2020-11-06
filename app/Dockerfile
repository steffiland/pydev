FROM python:3.9
#RUN pip install --upgrade pip

RUN useradd --create-home appman
USER appman
COPY requirements.txt .
COPY requirements-dev.txt .

# variant A: pip install in user context
ENV PATH="/home/appman/.local/bin:${PATH}"
# variant B: use a venv for pip install
#ENV VIRTUAL_ENV=/opt/venv
#RUN python3 -m venv $VIRTUAL_ENV
#ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --no-cache-dir -r requirements.txt 
# --upgrade
RUN pip install --no-cache-dir -r requirements-dev.txt
# --upgrade

WORKDIR /src
COPY --chown=appman:appman src/ .
EXPOSE 5000 5678
#CMD [ "python", "./server.py" ]
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["flask", "run"]