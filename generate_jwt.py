import jwt

token = jwt.encode(payload={'email': 'lucas@sheetgo.com'},
                   key='z6Ct_d2Wy0ZcZZVUYD3beI5ZCSsFrR6-f3ZDyn_MW00').decode('utf-8')
print(f'Bearer {token}')
