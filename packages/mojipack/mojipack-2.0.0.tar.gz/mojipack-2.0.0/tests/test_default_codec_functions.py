import mojipack


def test_default_codec_functions_e2e(some_test_message: bytes):
    for _ in range(10_000):
        encoded = mojipack.encode(some_test_message)

        try:
            decoded = mojipack.decode(encoded)

            assert decoded == some_test_message

        except Exception as e:
            print(encoded)
            raise e
