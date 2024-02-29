### API created with fast api for a milk-gathering business

## Documentation

As every fast api program, it uses OpenAPI to document, the route is this:

```
localhost:8000/docs
```

## Commands

### Create a virtual environment

```
python -m venv venv
```

### Activate the virtual environment

```
source venv/bin/activate
```

### Generate requirements
```
pip freeze > requirements.txt
```

### Install requirements
```
pip install -r requirements.txt
```

### Run

```
python -m uvicorn src.api:app --reload
```

## Tables

- User
- Driver
- Milk route
- Payments
- Producer
- Transport costs
- Deductions
