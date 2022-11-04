# Scrapper App

## Steps

### 1. Install Poetry
[Here](https://python-poetry.org/docs/#installing-with-the-official-installer) you can check how to do it

Using WSL, MacOS or Linux it should just be:

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

### 2. Install PyEnv
You'll need python version > 3.8, due to a pandas requirement.
```
pyenv install 3.9.1
```
```
pyenv global 3.9.1
```
Copy the path to your python 3.9.1. Then inside "/scrapper"
```
poetry env use {path to your python 3.9.1}
```


### 3. Run `poetry install`

```
poetry install
```

If VScode is throwing you import errors after doing this, go to the right bottom corner and change your interpreter, add the path returned by this:
```
poetry env info --path
```

### 4. Make sure you have a chrome driver installed

If you work in macos and you have chrome, you probably have it.

Ubuntu: `sudo apt install chromium-chromedriver`

Debian: `sudo apt install chromium-driver`

### 5. Go to your notebook and run all
