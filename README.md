# WEBAPP

Esta repositorio se creo para el desarrollo de una web que permita testear un api maas el cual internamente llama a un modelo predictivo:

- Lineas para testear el api
```bash
 curl -H "Content-Type: application/json" -X POST http://docker-fastapi-joenvihe.herokuapp.com/predict -d '{"age":"13","duration":"1","month":"1","date":"1","balance":"1","pout":"1","job":"1","camp":"1","contact":"1","house":"1"}
```

- web:
w