FROM anyakichi/poetry-builder:3.8-full

EXPOSE "8000"

ADD ./ ./

RUN poetry config virtualenvs.in-project true

RUN poetry install
