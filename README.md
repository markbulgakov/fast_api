## Service to count occurrences of certain keywords in the received sentences

This simple API is build with FastApi on Python with Docker.

### Installation:

> In the implementation app will create a local SQL DB.  

```
docker build -t occ_api_image .
docker run -d --name occ_api_container -p 80:80 occ_api_image
```

### Request samples:

`/events` – get a sentence(string) and counts the number of the occurrence of the specific keywords
```
curl -X POST 'http://localhost/api/v1/events/' -d '<some text>'
```

`/stats` – get a time interval (in seconds) and will return a JSON with the number of occurrence of the above keywords 
in the received interval time.

```
curl 'http://localhost/api/v1/stats?interval=60' 
``` 

Response example: 
```
{ "email": 2, "security": 1 } 
```
