import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("butenkosergii")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    # выводим в терминал количество сущенствующих репозиториев с именем "become-qa-auto"
    # Команда в терминале GitBush: pytest -m api -s
    # total_count = r['total_count']
    # print(f"total_count is {total_count}")

    # Перевірка кількості репозиторіїв
    assert r["total_count"] == 59
    # перший знайдений репозиторій буде містити в собі ім'я "become-qa-auto"
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] != 0


# Individual part of the project:


@pytest.mark.api  # We are checking whether it is possible to use emojis in github
def test_find_emodji(github_api):
    emodjis = github_api.get_emojis()
    assert len(emodjis) > 0


@pytest.mark.api  # We check the presence of a commit in the repository
def test_repo_exsits(github_api):
    owner = "Vict09ria"
    repo = "VikQA-auto"
    sha = "0e7f057bfd7622a0a81249419306c0f2c55b5f0b"
    commit = github_api.get_commit(owner, repo, sha)
    assert "sha" in commit
    assert commit["sha"] == sha
    assert "commit" in commit
    assert "message" in commit["commit"]

@pytest.mark.api  # Checking for non-existent commit
def test__non_exist_commit(github_api):
    owner = "Vict09ria"
    repo = "VikQA-auto"
    sha = "6dcb09b5b57875f334f61aebed695e2e4193db5e"
    commit = github_api.get_non_exist_commit(owner, repo, sha)
    assert "No commit found" in commit["message"]
