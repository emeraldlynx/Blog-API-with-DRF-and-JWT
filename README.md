# **Blog API DRF + JWT**
In this project realized Django Rest Framework application with JSON Web Token authentication.<br>
Auth API has users registration, login and obtaining JWT and refreshing JWT.<br>
The entities of users, messages and comments fully support CRUD queries.<br>

## Why JWT?<br>
JSON Web Token authentication method provides security. This way much safer than basic, session or token-in-db authentication.<br>

## Permissions
- Each `User` can change only own data.<br>
- Unauthorized users can view lists by each entity and `Post` and `Comment` details.<br>
- Only account's owner can view account details.<br>

## Documentation
### **Postman** [documentation](https://documenter.getpostman.com/view/9084501/U16kqQPr)
### **OpenAPI** page allowed at `http://example.com/openapi/` and **schema** by the `./blog/static/openapi/schema.yml`

---

## Clone project
```sh
$ git clone https://github.com/emeraldlynx/blog-drf.git
```

## Build and run
### **Docker**
Start docker
```sh
$ sudo dockerd
```
Build and run app
```sh
$ docker-compose up
```

***Also you can manually install all dependencies with `reqiurements.txt` file:***<br>
```sh
$ pip install -r requirements.txt
```
