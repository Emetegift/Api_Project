## Student Management API

This is a Student Management API built using Flask-Smorest and tested with Insomnia. The API allows users to perform CRUD operations on student records, including adding new students, retrieving student information, updating student records, and deleting students.

### Requirements

- Python 3.7 or above
- Flask-Smorest
- Flask-Migrate
- SQLAlchemy
- PostgreSQL
- Insomnia

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Emetegift/Api_Projectt-api.git
```

2. Create and activate a virtual environment:

```bash
python3 -m venv env
source env/bin/activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Create a PostgreSQL database:

```bash
createdb student_management_api
```

5. Apply database migrations:

```bash
flask db upgrade
```

6. Start the application:

```bash
flask run
```

The application should now be running on http://localhost:5000.

### Usage

The API has the following endpoints:

| Endpoint          | HTTP Method | CRUD Method | Result                               |
|-------------------|-------------|-------------|--------------------------------------|
| /students         | GET         | READ        | Get all students                     |
| /students/{id}    | GET         | READ        | Get a single student by id            |
| /students         | POST        | CREATE      | Add a new student                     |
| /students/{id}    | PUT         | UPDATE      | Update a single student by id         |
| /students/{id}    | DELETE      | DELETE      | Delete a single student by id         |

To test the API, use an API testing tool like Insomnia. Here's an example of how to retrieve all students:

1. Open Insomnia and create a new request.
2. Set the HTTP method to GET and the URL to `http://localhost:5000/students`.
3. Click "Send" to make the request.

The response should be a JSON object containing all student records in the database.

### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### License

[MIT](https://choosealicense.com/licenses/mit/)
