FROM python:3.8.2

ENV WORKDIR /app/

WORKDIR ${WORKDIR}

COPY Pipfile Pipfile.lock ${WORKDIR}

RUN pip install -U pip &&  \
    pip install pipenv --no-cache-dir && \
    pipenv install --system --ignore-pipfile --deploy

COPY . $WORKDIR

CMD ["python", "main.py"]
