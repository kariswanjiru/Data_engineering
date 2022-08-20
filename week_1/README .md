# Week One
## Code Snippets
This are some code snippets to be able to perform of of the tasks.
- Ingesting Data
    - This is a code snippet of what i learnt, see below:
```
URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"
python ingest_data.py \
    --user=postgres \
    --password=password \
    --host=loaclhost \
    --port=5432 \
    --db=ny_taxi \
    --table_name=ny_taxi_trips \
    --url=${URL}
```
  - Create SSH keys
    - This is a code snippet of what i learnt, see below:
  ```
  ssh-keygen -t rsa -f C:\Users\WINDOWS_USER\.ssh\KEY_FILENAME -C USERNAME -b 2048
  
  ```
  - Run postgresql on Docker
    - This is a code snippet of what i learnt, see below:
  ````
  docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTRGRES_DB="ny_taxi" \
    -v "C:/Users/USER/Documents/python_scripts/data_engineering_practice/ny_taxi_postgres_data":/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres:14
    
  ````
  - Run pgAdmin on Docker
    - This is a code snippet of what i learnt, see below:
   ```
   docker run -it \
      -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
      -e PGADMIN_DEFAULT_PASSWORD="root" \
      -p 8080:80 \
      dpage/pgadmin4
  
   ```
  - Map ports and networks using Docker
    - This is a code snippet of what i learnt, see below:
  ````
  docker run -it \
    --network=pg-network \
    taxi_ingest:v001 \
        --user=postgres \
        --password=password \
        --host=loaclhost \
        --port=5432 \
        --db=ny_taxi \
        --table_name=ny_taxi_trips \
        --url=${URL}
        
  ````
  - Configure GCP SSH Keys
    - This is a code snippet of what i learnt, see below:
      ````
      ssh -i ~/.ssh/gcp user@ipUrl
      
      ````
  - [Create VM gcp Instance.](https://cloud.google.com/compute/docs/connect/add-ssh-keys)
  - Terraform
  ````
  terraform init
  ````
  ````
  terraform plan
  ````
  
  ````
   terraform apply
  ````
  
  ````
  terraform destroy
