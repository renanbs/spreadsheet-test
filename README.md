# SpreadSheet and Image API's


This project consists in 2 API's. One of them returns the list of tabs of a excel xlsx file and the other converts a image from 2 formats jpeg -> png and png -> jpg.

 - It was only tested on Linux.

#### API Endpoints
- POST /image/convert
- POST /excel/info


## Requirements

 - Make
 - Python 3.6+
 - pyenv


## Development Environment
 
 
### Automation tool

This project uses `Makefile` as automation tool.

### Set-up Virtual Environment

1. If you don't have `pyenv` already installed, follow the lines above:

The following commands will install and set-up `pyenv` tool (https://github.com/pyenv/pyenv) used to create/manage virtual environments:

> If you use `zsh`, just replace `bashrc` with the configuration file of your interpreter `zshrc`

```bash
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc
$ exec "$SHELL"
$ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
$ exec "$SHELL"
```

2. If you already have it installed, it might be necessary to update it. If you installed like cloning the project:

I'm assuming you have it installed in your home directory, like this: `$HOME/.pyenv`

```bash
$ cd $HOME/.pyenv
$ git pull
$ exec "$SHELL"
```

After choosing one of the steps, access the project directory and execute `make create-venv` to create and recreate the virtual environment:

```bash
➜ make create-venv
```

> The environment will be create in your home directory:

> `$PROJECT_NAME` and `$PYTHON_VERSION` are variables defined in the Makefile

```bash
$HOME/.pyenv/versions/$PROJECT_NAME-$PYTHON_VERSION/bin/python

/home/renan/.pyenv/versions/spreadsheet_test-3.8.3/bin/python
```


### Run unit tests, style and convention

- Tests will run with coverage minimum at 90%.

Running code style
```bash
➜ make code-convention
```
Running unit tests
```bash
➜ make test
```
Running code style and all tests
```bash
➜ make
```

## How to run this project

There are 2 ways to run this project.

```bash
➜ flask run
```
or

```bash
➜ python wsgi.py
```
or 

```bash
➜ make run
```

This will start the server in your localhost using port 5000.

The server is accessible at the link below, despite there is no root endpoint:
> http://127.0.0.1:5000/

The only available endpoints are:
- POST http://127.0.0.1:5000/image/convert
- POST http://127.0.0.1:5000/excel/info

---
## Usage examples

### cURL

Just change the email inside generate.py to generate another token

Get tabs ordered alphabetical
```bash
➜ curl http://127.0.0.1:5000/excel/info -H "X-Authentication-Token: `python generate_jwt.py`" -F file=@Sample.xlsx
```

Convert jpg image to png
```bash
➜ curl http://127.0.0.1:5000/image/convert -H "X-Authentication-Token: `python generate_jwt.py`" -F file=@sample.jpg -F format=png --output ./jpg-to-png-sample.png                                      
```

Convert png image to jpg 
```bash
➜ curl http://127.0.0.1:5000/image/convert -H "X-Authentication-Token: `python generate_jwt.py`" -F file=@png-sample.png -F format=jpg --output ./png-to-jpg-sample.jpg
```

### Python Scripts

- Get tabs ordered alphabetical

The first parameter is the email to be authenticated and the second is the xlsx files to extract the tabs.
```bash
➜ python excel_info.py lucas@sheetgo.com sample.xlsx
```

- Convert image

  The first parameter is the email to be authenticated, the second is the input file and the third is the output file

    - jpg to png

    ```bash
    ➜ python convert_img.py lucas@sheetgo.com png jpg-sample.jpg jpg-to-png-sample.png                                  
    ```

    - png to jpg 
    ```bash
    ➜ python convert_img.py lucas@sheetgo.com jpg png-sample.png png-to-jpg-sample.jpg  
    ```
