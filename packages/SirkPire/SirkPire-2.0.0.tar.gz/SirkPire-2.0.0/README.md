<h1>SirkPire 1.0.0</h1>

> SirkPire is a powerful and easy library for building self Bots in Rubika


<p align='center'>
    <a href='https://github.com/MrTelepathic/SirkPire'>GitHub</a>
    •
    <a href='https://rubika.ir/SirkPire'>Documents</a>
</p>

<hr>

**Example:**
``` python
from SirkPire import Bot, Message

bot = Bot("sessionName")

for update in bot.on_message():
    if update.text() == 'hello':
        bot.send_text(update.chat_id(), f"**Hello** ``{update.author_title()}``. __This message is from the SirkPire library.__", update.
message_id())
```

<hr>

### Features:
    
- **Fast** : *The requests are very fast.*

- **Easy** : *All methods and features are designed as easy and optimal as possible*

- **Powerful** : *While the library is simple, it has high speed and features that make your work easier and faster*


<hr>

## Rubika : @SirkPire

### Install or Update:

``` bash
pip install -U SirkPire
```
