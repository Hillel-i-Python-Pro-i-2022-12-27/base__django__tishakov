### :arrow_forward: Run

Make all actions needed for run homework from zero.

```shell
make d-homework-i-run
```

### :put_litter_in_its_place: Purge

Make all actions needed for run homework from zero.

```shell
make d-homework-i-purge
````

### :hammer_and_wrench: Dev

### Initialize dev

Install dependencies and register pre-commit.

```shell
make init-dev
```


## :whale: Docker

Use services in dockers.
### :arrow_forward: Run

Just run

```shell
make d-run
````

### :stop_button: Stop

Stop services

```shell
make d-stop
```

### :put_litter_in_its_place: Purge

Purge all data related with services

```shell
make d-purge
```

### :crown: Superuser

Create Super User (login:admin, password: admin123)

```shell
make init-dev-i-create-superuser
```

Make migrations

```shell
make migrations
```

Make migrate

```shell
make migrate
```