# Mojipack

Encode any collection of bytes into a fun square of emojis. It's like base64, but more colourful!

```
📦‌💖‌🌺‌🦋‌🌈‌🥰‌😂‌🐦‌🍩‌💵‌😢‌🦄
🍎‌🍎‌🍎‌🍎‌🍎‌🐌‌⏰‌💪‌👌‌🎊‌💓‌💖
🎂‌💸‌🧡‌🌈‌🙃‌🎵‌👉‌🌷‌💓‌👉‌📢‌📺
🙃‌🐶‌💖‌🌻‌💸‌😢‌🚀‌💭‌🌈‌💰‌🙃‌🙃
🤗‌🐯‌🍀‌💫‌🤗‌😤‌💫‌💎‌🤧‌🎵‌📣‌📺
📺‌🤧‌🐯‌😤‌💘‌🙂‌🐻‌🌷‌😱‌😞‌🌞‌😹
👉‌🤭‌💪‌💪‌🚀‌💪‌💓‌🦋‌💰‌💰‌😱‌😱
😏‌🍎‌😢‌🤧‌🌺‌🌺‌🍓‌👌‌🤧‌💪‌🍀‌🦄
🦄‌⏰‌😚‌📢‌🌻‌😱‌🌈‌💭‌📌‌🤧‌📌‌😻
🎀‌💫‌🌷‌😤‌😱‌🤯‌🥴‌🤯‌📺‌🦄‌🥴‌🍓
🙃‌💋‌🐶‌🤗‌🍀‌🐯‌😢‌👉‌😹‌😐‌💫‌💘
🐌‌🍎‌😃‌🌷‌😃‌🤧‌🎵‌📌‌🤯‌👌‌🚀‌😄
😤‌🤭‌🌈‌😏‌😚‌💰‌💘
```

# Installation

Mojipack is on PyPI! So all you need to get started is to install it with pip:
```shell
pip install mojipack
```

# Usage

Here is how you create a mojipack encoded payload. The example uses msgpack for inner encoding. You could also use UTF-8
encoded json if you don't want to install more packages.
```python
import mojipack
import msgpack

data = msgpack.packb(
    {
        "name": "Jane Doe",
        "age": 21,
        "city": "New York",
        "is_student": False
    },
    use_bin_type=True
)

output = mojipack.encode(data)

print(output)
```

Decoding is just as simple:
```python
import mojipack
import msgpack

MOJIPACK_MESSAGE = "📦‌💖‌🌺‌🦋‌🌈‌🥰‌😂‌🐦‌🍩‌ ..."

data = mojipack.decode(MOJIPACK_MESSAGE)

print(
    repr(
        msgpack.unpackb(data)
    )
)
```