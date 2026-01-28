import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests against: dev / qa / prod"
    )

@pytest.fixture
def env(request):
    return request.config.getoption("--env")
