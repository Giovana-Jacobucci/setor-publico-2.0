import urllib.request
import json

login_req = urllib.request.Request(
    'http://127.0.0.1:8000/api/v1/login/',
    data=json.dumps({'matricula': 'admin', 'senha': 'admin123'}).encode('utf-8'),
    headers={'Content-Type': 'application/json'}
)
with urllib.request.urlopen(login_req) as resp:
    token = json.loads(resp.read().decode('utf-8'))['access']

print("Token obtido com sucesso.")

perguntar_req = urllib.request.Request(
    'http://127.0.0.1:8000/api/v1/analise-ia/perguntar/',
    data=json.dumps({
        'pergunta': 'Quais as tendencias no SEBRAE para Novembro? Alguns padroes irao se repetir?',
        'inicio': '2026-09-01',
        'fim': '2026-10-26'
    }).encode('utf-8'),
    headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
)

try:
    with urllib.request.urlopen(perguntar_req, timeout=120) as resp:
        print("Resposta:")
        print(json.loads(resp.read().decode('utf-8')))
except Exception as e:
    print("Erro:", e)
    if hasattr(e, 'read'):
        print("Corpo:", e.read().decode('utf-8'))
