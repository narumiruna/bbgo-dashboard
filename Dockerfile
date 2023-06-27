FROM python:3.9-buster

WORKDIR /workspace

COPY app.py .
COPY bbgo_dashboard bbgo_dashboard
COPY pyproject.toml .
COPY poetry.lock .

RUN pip3 install .

EXPOSE 8501

CMD ["run", "app.py"]
ENTRYPOINT ["streamlit"]
