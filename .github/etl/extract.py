from git import Repo
import os

def extract_repo(repo_url, local_path):
    if not os.path.exists(local_path):
        Repo.clone_from(repo_url, local_path)
    else:
        repo = Repo(local_path)
        repo.git.pull()
    print(f"Repository extracted to {local_path}")

