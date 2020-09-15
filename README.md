# Coffe APP

In this App, we have tow products. coffee machines and coffee pods.
We can list machines and pods.
We can filter based on fields in machines and pods.

# Motivations
it is a python task for performing filtering on coffee and pods products using:

- Django.
- Django Rest Framework.
- Django filters for filtering on fields.
- Djongo to connect to MongoDB.


## Getting Started
### Pre-requisites and Local Development

Developers using this project should already have Python3 and pip3 installed in their local machines.

#### PIP Dependencies

Ensure you are working using your created virtual environment.

To install all dependencies execute this command in the root folder:
```bash
pip3 install -r requirements.txt
```

To run the server, execute this command in the root folder:

```bash
python3 manage.py runserver
```


## API Reference

### Endpoints

#### GET 'api/machines/'

   - Fetches all machines as objects.  
   - Request Arguments: None.
   - Return an array of coffee machines objects.
   
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
#### GET 'api/pods/'

   - Fetches all pods as objects.  
   - Request Arguments: None.
   - Return an array of coffee pods objects.
   
   ```
   
 [
    {
        "id": 1,
        "product_type": "Small coffe pod",
        "coffe_flavor": "Vanilla",
        "pack_size": "1 dozen "
    },
    {
        "id": 2,
        "product_type": "Small coffe pod",
        "coffe_flavor": "Vanilla",
        "pack_size": "3 dozen "
    },
    {
        "id": 3,
        "product_type": "Small coffe pod",
        "coffe_flavor": "Caramel",
        "pack_size": "1 dozen "
    },
    {
        "id": 4,
        "product_type": "Small coffe pod",
        "coffe_flavor": "psl",
        "pack_size": "1 dozen "
    },
    {
        "id": 5,
        "product_type": "Small coffe pod",
        "coffe_flavor": "psl",
        "pack_size": "3 dozen "
    },
  ]
   ```
