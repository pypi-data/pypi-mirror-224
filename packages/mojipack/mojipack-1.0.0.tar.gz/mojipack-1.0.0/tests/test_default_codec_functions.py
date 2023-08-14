import mojipack


def test_default_codec_functions_e2e(some_test_message: bytes):
    encoded = mojipack.encode(some_test_message)
    decoded = mojipack.decode(encoded)

    print(encoded)

    assert decoded == some_test_message
