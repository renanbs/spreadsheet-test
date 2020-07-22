import os
import sys

import jwt
import requests

from sheetgo.api.utils import file_loader


def get_tabs(email, filename):
    token = jwt.encode(payload={'email': email},
                       key='z6Ct_d2Wy0ZcZZVUYD3beI5ZCSsFrR6-f3ZDyn_MW00').decode('utf-8')

    headers = {'Authorization': f'Bearer {token}'}

    filename = os.path.join(os.path.dirname(__file__), filename)
    file_data = file_loader(filename, True)

    data = {'file': (filename, file_data)}

    response = requests.post('http://localhost:5000/excel/info', files=data, headers=headers)
    print(response.json())


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('You pass 2 arguments. The first is the email and the second is the file.')
        exit(-1)

    get_tabs(str(sys.argv[1]), sys.argv[2])
