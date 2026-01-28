import pytest

# Uses --env from command line
def test_env_from_cli(env):
    assert env in ["dev", "qa", "prod"]


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (5, 5, 10),
        (-1, 1, 0),
    ]
)
def test_addition(a, b, expected):
    assert a + b == expected


@pytest.mark.skip(reason="Feature not ready")
def test_skip_example():
    assert False


@pytest.mark.xfail(reason="Known bug")
def test_expected_failure():
    assert 1 == 2
