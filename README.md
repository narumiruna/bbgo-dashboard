# bbgo-dashboard

初步構想

![image](https://github.com/narumiruna/bbgo-dashboard/assets/4680567/0a40325a-799b-42bb-a5a8-540cebddc87d)

## Installation

```sh
pip install poetry
poetry install
```

## generate db model

```sh
pip install sqlacodegen
sqlacodegen mysql+pymysql://root@localhost:3306/bbgo > bbgo_dashboard/db/model.py
```

## ~~~run dagster~~~

```sh
export MYSQL_USERNAME=
export MYSQL_PASSWORD=
export MYSQL_HOST=
export MYSQL_PORT=
export MYSQL_DATABASE=

poetry run dagster dev
```

## run streamlit

```sh
poetry run streamlit run app.py
```