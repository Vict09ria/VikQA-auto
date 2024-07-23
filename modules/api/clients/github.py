import requests


class GitHub:

    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", params={"q": name}
        )
        body = r.json()

        return body

    # Individual part of the project
    def get_emojis(self):
        r = requests.get("https://api.github.com/emojis")
        body = r.json()

        return body

    def get_commit(self, owner, repo, sha):
        url = f"https://api.github.com/repos/{owner}/{repo}/commits/{sha}"
        r = requests.get(url)
        body = r.json()
        return body

    def get_non_exist_commit(self, owner, repo, sha):
        url = f"https://api.github.com/repos/{owner}/{repo}/commits/{sha}"
        r = requests.get(url)
        return r.json()
