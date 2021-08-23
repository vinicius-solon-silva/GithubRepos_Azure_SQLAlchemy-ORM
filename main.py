import list_repos
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

github_user = list_repos.user
list_repos.user = list_repos.user.replace('-', '')

print("\n--Enter your Azure username and password--")
username = input('Username: ')
password = input('Password: ')

print("\n--Enter your Azure server and database name--")
server_name = input('Server name: ')
db_name = input('Database name: ')

engine = create_engine(f'mssql+pymssql://{username}:{password}@{server_name}.database.windows.net:1433/{db_name}', echo=False)

Sessions = sessionmaker(bind=engine)
session = Sessions()

Base = declarative_base()


class UserRepository(Base):
    __tablename__ = f'{list_repos.user}_repos'

    id = Column(Integer, primary_key=True)
    repo = Column(String(255))
    URL = Column(String(255))


Base.metadata.create_all(engine)
print(f"\nCreating {list_repos.user}_repos table...")


try:
    for repos in list_repos.repos:
        userRepo = UserRepository(id=repos["id"], repo=repos["name"], URL=repos["html_url"])
        session.add(userRepo)

    session.commit()
    session.close()

    print(f"\nData from the github repositories of {github_user} has been successfully inserted into the table {list_repos.user}_repos!\n")

except Exception:
    print(f"\n---Error inserting data! Probably because table already exists!")
    print(f"\n---Delete the existing table and run the code again.\n")
