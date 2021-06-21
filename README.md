# clientLog


## steps

1. create the terraform gcloud build image in your own project
```
cd terraform
gcloud builds submit
```
2. create a service account and give it the project editor permission or bq admin permission
3. give the cloud build default service account(project-number@cloudbuild.gserviceaccount.com) the cloud run admin and service account user permission at least
4. change the substitution in cloudbuild.yaml
    - _BUCKET: specifiy the terraform's state file in gcs
    - _REGION: cloud run's deployment region, default is us-central1
    - _IMAGE_NAME: image name in your project
    - _SA_MAIL: Service account email bind to the cloud run services
```
cd bqtest
gcloud builds submit
```
5. get the cloudrun's url and test it with query parameter and pre define path 
```
cliu@dev2:python/bq $ curl https://bq-query-by-id-gygrgrxnnq-uc.a.run.app/hello
Hello World2!
cliu@dev2:python/bq $ curl https://bq-query-by-id-gygrgrxnnq-uc.a.run.app\?id\=1
"[{'id': '1', 'price': '$1.99', 'product': 'shirt'}, {'id': '1', 'price': '$1.99', 'product': 'shirt'}, {'id': '1', 'price': '$1.99', 'product': 'shirt'}, {'id': '1', 'price': '$1.99', 'product': 'shirt'}]"%
```