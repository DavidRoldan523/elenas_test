# -------------------------ELENAS TEST---------------------------------

#### PLEASE README! Using **main** branch

### STACK USED

- DOCKER - DJANGO - POSTGRESQL

### ENDPOINTS AVAILABLES

- **BASE_URL** = "localhost:8000/api/"

| PARAMS QUERY | USE FOR |
| ---- | ---- |
| ?per_page=0 | get all documents without pagination |
| ?per_page=5&page=1 | get documents paginates per 5 items |
| ?search="some description | get only documents that contains this description 

| RESOURCE | ROUTE | METHOD HTTP|
| ---- | ---- | ---- |
| Health Check      | "health-check/"     | POST     |
| User      | BASE_URL + "auth/register/"     | POST     |
| User      | BASE_URL + "auth/login/"     | POST     |
| Employers | BASE_URL + "employers/"     |  GET    |
| Employers | BASE_URL + "employers/?per_page=0"     |  GET    |
| Employers | BASE_URL + "employers/?per_page=5&page=1"     |  GET    |
| Employers | BASE_URL + "employers/"     |  POST    |
| Tasks     | BASE_URL + "tasks/"    | GET     |
| Tasks     | BASE_URL + "tasks/?per_page=0" | GET     |
| Tasks     | BASE_URL + "tasks/?per_page=5&page=1" | GET     |
| Tasks     | BASE_URL + "tasks/?search='some description'" | GET     |
| Tasks     | BASE_URL + "tasks/"    | POST     |
| Tasks     | BASE_URL + "tasks/<int:pk>/"    | GET     |
| Tasks     | BASE_URL + "tasks/<int:pk>/"    | PUT     |
| Tasks     | BASE_URL + "tasks/<int:pk>/"    | DELETE     |


### DEPLOYMENT PROJECT

Using these commands:



Using for build container of project

```bash
docker-compose build
```

```bash
docker-compuse up
```



Using token JWT for authenticate user on endpoints

```python
Authorization: Bearer TOKEN
```

### TDD DEPLOYMENT AND USE COVERAGE

Using these commands for run test (TDD) on project

```bash
docker-compose run web pytest --cov
```
