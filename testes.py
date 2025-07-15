# Exemplo de Teste por meio de requisições pela biblioteca Requets

import requests

headers = {
    "Authorization": "Bearer Seu token refresh"
}
requisicao = requests.get("http://127.0.0.1:8000/auth/refresh", headers=headers)
print(requisicao)
print(requisicao.json())
