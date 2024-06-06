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
    assert r["total_count"] == 57
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] != 0


# Індивідуальна частина проєкту


@pytest.mark.api  # Перевіряємо,чи є можливість використати емозді в гітхабі
def test_find_emodji(github_api):
    emodjis = github_api.get_emojis()
    assert len(emodjis) > 0


@pytest.mark.api
def test_repo_exsits(github_api):
    owner = "Vict09ria"
    repo = "VikQA-auto"
    sha = "0e7f057bfd7622a0a81249419306c0f2c55b5f0b"
    commit = github_api.get_commit(owner, repo, sha)
    assert "sha" in commit
    assert commit["sha"] == sha
    assert "commit" in commit
    assert "message" in commit["commit"]
