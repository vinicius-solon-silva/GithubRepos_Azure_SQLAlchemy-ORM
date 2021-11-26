import list_repos
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker


github_user = list_repos.user
list_repos.user = list_repos.user.replace('-', '')

# Setting credentials for connection to database
print("\n--Enter your Azure username and password--")
username = input('Username: ')
password = input('Password: ')

print("\n--Enter your Azure server and database name--")
server_name = input('Server name: ')
db_name = input('Database name: ')

# Creating engine for connection
engine = create_engine(f'mssql+pymssql://{username}:{password}@{server_name}.database.windows.net:1433/{db_name}', echo=False)

# Starting a session with connection engine
Sessions = sessionmaker(bind=engine)
session = Sessions()

# Declaring base and class, for table to be created in database
Base = declarative_base()


class UserRepository(Base):
    __tablename__ = f'{list_repos.user}_repos'

    id = Column(Integer, primary_key=True)
    repo = Column(String(255))
    URL = Column(String(255))


Base.metadata.create_all(engine)
