# WEBAPP

Esta repositorio se creo para el desarrollo de una web que permita testear un api maas el cual internamente llama a un modelo predictivo:

- Lineas para testear el api
```bash
 curl -H "Content-Type: application/json" -X POST http://docker-fastapi-joenvihe.herokuapp.com/predict -d '{"age":"13","duration":"1","month":"1","date":"1","balance":"1","pout":"1","job":"1","camp":"1","contact":"1","house":"1"}
```

- web:
```bash
https://mlops-webapp.herokuapp.com/
```

## TEST
- Se instalo pytest para realizar pruebas de llamada al api con valores correctos he incorrectos
- Se creo la carpeta **tests** y adiciono el archivo **test_config.py**


## CI/CD

### EN HEROKU
* In the deployment method section, click Github.
* In the connect to Github section, enter the repo name and search. It will find the repo name for you. Then click connect.
* In the automatic deployed section, tick Wait for CI to pass before deploying and click enable the automatic deploy button.
* Then go to account setting → application → Authorizations → create authorization.
* Then enter the description in the box and click create.
* Copy and save the authorization token for future use (We need this in the next step to create secrets).

### Create CI-CD pipeline using GitHub actions
CI-CD pipeline will be created using the GitHub actions. Create a new file inside the **.github/workflows** folder and named it as the ci-cd.yaml. Please note that the file extension of this must be yaml.
We can easily reflect the changes in the model or code through the frontend after implementing the CI-CD pipeline. Because we just need to push the code after **doing the modifications and it will reflect the changes automatically**. That is the advantage of using the CI-CD pipeline for ML model development. Because in ML context, there is a model retraining part that is not included in the normal software development life cycle(We will be discussing the retraining part in the 13th section). We can easily reflect the changes to the model with this approach.
Now we need to create **two secrets inside GitHub as HEROKU_API_TOKEN and HEROKU_API_NAME to do the deployment**.
* Select the repo and click the settings.
* Then click secrets in the left panel.
* Click new repository secrets. Need to create two secrets.
1. name: HEROKU_API_NAME |value: churnmodelprod
2. name: HEROKU_API_TOKEN |value: Authorization token saved in the last step