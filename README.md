# LinkedIn Connect Bot

Bot em Python que faz login no LinkedIn e envia solicitações de conexão usando Selenium.

## Requisitos
- Google Chrome e ChromeDriver compatível  
  Baixar o ChromeDriver: [https://googlechromelabs.github.io/chrome-for-testing/#stable](https://googlechromelabs.github.io/chrome-for-testing/#stable)  
  Certifique-se de baixar a versão que corresponde ao seu Google Chrome.
- Instalar dependências:
  ```
  pip install selenium python-dotenv
  ```

## Configuração
Criar arquivo `config/.env`:
```
EMAIL=seu_email
PASSWORD=sua_senha
```
Colocar `chromedriver.exe` na pasta `driver/`.

## Uso
```
python -m core.connect
```

## Parar o bot
Pressionar **CTRL + C** no terminal.

## Aviso
Somente para estudo. Pode violar as regras do LinkedIn.
