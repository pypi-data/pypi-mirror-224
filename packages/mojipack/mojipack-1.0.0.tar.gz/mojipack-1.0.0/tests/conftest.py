import msgpack
import pytest


@pytest.fixture()
def some_test_message() -> bytes:
    return msgpack.packb(
        {
            "name": "Jane Doe",
            "age": 21,
            "city": "New York",
            "is_student": False
        },
        use_bin_type=True
    )
