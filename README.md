# Coffe APP

In this App we have tow producrs. coffe machines and coffe pods.
We can list machines and pods.
We can filter based on fields in machines and pods.

## Getting Started
### Pre-requisites and Local Development

Developers using this project should already have Python3 and pip3 installed in their local machines.

#### PIP Dependencies

Ensure you are working using your created virtual environment.

To install all dependices execute this command in the root folder:

```bash
pip3 install requirements.txt```

To run the server, execute this command in the root folder:

```bash
python3 manage.py runserver
```bash


## API Reference

### Endpoints

#### GET 'api/machines/'

```$ curl -X GET https://localhost/machines```
   - Fetches all machines as objects.  
   - Request Arguments: None.
   - Return an array of coffe machines objects.
   
```
    [
       {
           "id": 1,
           "product_type": "Small machine",
           "model": "base model",
           "water_line_compatible": false
       },
       {
           "id": 2,
           "product_type": "Small machine",
           "model": "premium model",
           "water_line_compatible": false
       },
       {
           "id": 3,
           "product_type": "Small machine",
           "model": "deluxe model",
           "water_line_compatible": true
       },
       {
           "id": 4,
           "product_type": "Large machine",
           "model": "base model",
           "water_line_compatible": false
       },
      ]
```

