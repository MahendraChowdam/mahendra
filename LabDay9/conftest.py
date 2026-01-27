import pytest

# Function scope fixture
@pytest.fixture(scope="function")
def numbers():
    return (10, 5)

# Module scope fixture
@pytest.fixture(scope="module")
def resource():
    print("\nresource setup (module scope)")
    yield
    print("\nresource teardown (module scope)")
