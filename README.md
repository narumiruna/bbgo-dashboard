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
poetry run sqlacodegen mysql+pymysql://root@localhost:3306/bbgo > bbgo_dashboard/db.py
```
