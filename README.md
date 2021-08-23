# GET GITHUB USER REPOSITORIES TROUGH SQLALCHEMY ORM

This project makes a search for github users repositories and post to an Azure SQL Database using SqlAlchemy ORM.

## Installation

- Clone the repository
- Install _requests_ library using pip:
``` 
pip install requests
```
- Install sqlalchemy library using pip:
``` 
pip install sqlalchemy
```

## Running the code

- Open the project folder in a development tool
- Run the code using Python compiler


The interface asks for a GitHub username on the input:

```
>>> Enter username: 
```

Then the code will search for user's data and try to create a table in the database.
If ecerything goes right, the code will print this message:
```
>>> Table {user}_repos succesfully created!
```

After that the code will post all the GitHub repositories infos into the Azure SQL database, and print this message:
``` 
Data from the github repositories of {user} has been successfully inserted into the table {user}_repos!
```

## More information

You can access the _Requests_ library documentation [here](https://requests.readthedocs.io/en/master/)

You can access the _SqlAlchemy_ library documentation [here](https://www.sqlalchemy.org/)

