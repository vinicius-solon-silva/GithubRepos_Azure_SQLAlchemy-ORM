import list_repos
import connectionBase
from connectionBase import UserRepository


print(f"\nCreating {list_repos.user}_repos table...")

try:
    for repos in list_repos.repos:
        userRepo = UserRepository(id=repos["id"], repo=repos["name"], URL=repos["html_url"])
        connectionBase.session.add(userRepo)

    connectionBase.session.commit()
    connectionBase.session.close()

    print(f"\nData from the github repositories of {connectionBase.github_user} has been successfully inserted into the table {list_repos.user}_repos!\n")

except Exception:
    print(f"\n---Error inserting data! Probably because table already exists!")
    print(f"\n---Delete the existing table and run the code again.\n")
