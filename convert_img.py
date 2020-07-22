import os
import sys

import jwt
import requests
from http import HTTPStatus

from sheetgo.api.utils import file_loader


def convert_image(email, output_format, input_filename, output_filename):
    token = jwt.encode(payload={'email': email},
                       key='z6Ct_d2Wy0ZcZZVUYD3beI5ZCSsFrR6-f3ZDyn_MW00').decode('utf-8')

    headers = {'Authorization': f'Bearer {token}'}

    filename = os.path.join(os.path.dirname(__file__), input_filename)
    file_data = file_loader(filename, True)

    files = {'file': (filename, file_data)}
    data = {'format': output_format}

    response = requests.post('http://localhost:5000/image/convert', files=files, data=data, headers=headers)
    if response.status_code == HTTPStatus.OK:
        with open(output_filename, 'wb') as f:
            f.write(response.content)

    else:
        print(response.json())


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print('You need to pass 4 arguments. The first is the email and the second the output format, '
              'the third is input file and the fourth is the output file.')
        exit(-1)

    convert_image(str(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4])
