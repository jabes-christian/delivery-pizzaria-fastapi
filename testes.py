# Exemplo de Teste por meio de requisições pela biblioteca Requets

import requests

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI3IiwiZXhwIjoxNzUyODc5MjA0fQ.fOpwQY9AubVmWP8z4lnChs3K0KUbaty49bjsvHlAHfw"
}
requisicao = requests.get("http://127.0.0.1:8000/auth/refresh", headers=headers)
print(requisicao)
print(requisicao.json())
