# aternos-server-parser

This is a Python script that can parse some minecraft servers hosted on Aternos. It takes servername variants from wordlist file, adds _".aternos.me"_ and checks if server this server exist. **This version works only for Java**.

## Preparing

- Clone this repo to your machine:
    ```sh
    git clone https://github.com/arpatutin/aternos-server-parser.git
    ```
- Install requirements from _requirements.txt_:
  ```sh
  pip install -r requirements.txt
  ```
- Replace _wordlist.txt_ file to wordlist you're going to use (there should be just words, without _.aternos.me_). Please don't leave any space or new line symbols in the end of your file.

Now you're ready to use script. 

## Usage

```sh
python parser.py [--no-prepare] [--no-shuffle]
```

- ```--no-prepare```
  Preparing means deleting queries that contain some special symbols that can't be used in domain. Using ```-no-prepare``` you can run script without this cleaning.
- ```--no--shuffle```
  By default script shuffles wordlist befire starting parsing. If you don't want your words to be shuffled, you can desable it with this option.

> After launching you'll receive data using stdout and two files.
> First file is _online.txt_, there you can see servers that are started at the moment that script made request to ping it.
> Second file is _offline.txt_, it should contain servers that ain't working at the moment, but exist on aternos.

> If parser will test all the names from your wordlist, it'll stop automatically.
>You can also stop it using Ctrl+C ot other interrupt signal.

## Collaboration

I'm always open to receive any fixes or collaborations in this repo.
