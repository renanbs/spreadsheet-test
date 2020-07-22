# SpreadSheet and Image API's


This project consists in 2 API's. One of them returns the list of tabs of a excel xlsx file and the other converts a image from 2 formats jpeg -> png and png -> jpg.

 - It was only tested on Linux.


## Requirements

 - Make
 - Python 3.8+


## Development Environment
 
 
### Automation tool

This project uses `Makefile` as automation tool.

### Set-up Virtual Environment

The following commands will install and set-up `pyenv` tool (https://github.com/pyenv/pyenv) used to create/manage virtual environments:

> Just replace `zshrc` with the configuration file of your interpreter, like `bashrc`

```bash
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.zshrc
$ exec "$SHELL"
$ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
$ exec "$SHELL"
```

After that, access the project directory and execute `make create-venv` to create and recreate the virtual environment:

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

This will start the server in your localhost using port 5000.

The server is accessible at the link below, despite there is no root endpoint:
> http://127.0.0.1:5000/

The only available endpoints are:
- http://127.0.0.1:5000/image/convert
- http://127.0.0.1:5000/excel/info

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
