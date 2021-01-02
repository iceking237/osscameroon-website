from app.utils.database import storage
from app.utils.database.users import fetch_all_users
from app.utils.database.projects import fetch_all_projects
import json
import sys
import os
import meilisearch

HOST = "http://127.0.0.1:7700"


def create_github_users_index():
    ret = fetch_all_users()

    client = meilisearch.Client(HOST, os.getenv("MEILISEARCH_MASTER_KEY"))
    try:
        index = client.create_index(storage.KIND_USERS, {"primaryKey": "id"})
    except Exception as e:
        index = client.get_index(storage.KIND_USERS)
        print("error: ", e)
    finally:
        index.update_documents(ret)
        print("started updating github_users documents")


def create_github_projects_index():
    ret = fetch_all_projects()

    client = meilisearch.Client(HOST, os.getenv("MEILISEARCH_MASTER_KEY"))
    try:
        index = client.create_index(storage.KIND_PROJECTS, {"primaryKey": "id"})
    except Exception as e:
        index = client.get_index(storage.KIND_PROJECTS)
        print("error: ", e)
    finally:
        index.update_documents(ret)
        print("started updating github_projects documents")


if __name__ == "__main__":
    # Usage :
    # python3 -m cli.main
    create_github_users_index()
    create_github_projects_index()
