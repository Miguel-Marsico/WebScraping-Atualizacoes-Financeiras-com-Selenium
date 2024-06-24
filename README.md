<h1>
    WebScraping - Atualizações financeiras com Selenium 📈
</h1>

![image](https://github.com/Miguel-Marsico/Financial-updates-with-selenium/assets/158609724/e294bd58-bb1c-4f3a-9d16-dde9d1dde450)
![image](https://github.com/Miguel-Marsico/Financial-updates-with-selenium/assets/158609724/dd436653-338a-45a1-aeb2-c33411ea8f69)

 ## 📋 Tópicos
<div>
 • <a href="#-sobre">Sobre</a> </br>
 • <a href="#-ferramentas">Ferramentas</a> </br>
 • <a href="#-como-executar-esse-projeto">Como Executar esse projeto</a> </br>    
 • <a href="#-licença">Licença</a></br>
</div>

## 📗 Sobre
Este projeto é uma automação em **Selenium** que realiza **WebScraping** de dados financeiros na internet e os envia por **e-mail**, rodando em **background**.

## 🔧 Ferramentas

### 👩‍💻 **Linguagem** ([Pyhton](https://www.python.org))

- [Selenium](https://www.selenium.dev/documentation/)
- [Smtplib](https://docs.python.org/3/library/smtplib.html)
- [Email](https://docs.python.org/3/library/email.html#module-email)

### 🛠️ **Utilitários** 

- Compiladores: **[Pycharm Community](https://www.jetbrains.com/pt-br/pycharm/)** 

## ▶ Como executar o projeto

### Criando ambiente virtual:

1 - Navegue até o diretório onde deseja criar o ambiente virtual:
```bash
 cd /path/to/your/project
```
2 - Crie um ambiente virtual:
```bash
 python3 -m venv name
```
3 - Ative o ambiente virtual:
```bash
 name\Scripts\activate
```

### Instalação de biblioteca:

```bash
 pip install selenium
```

### 💡 SmtpLib e Email são bibliotecas Python nativas

### Importação de bibliotecas:
```bash
 from selenium import webdriver
 from selenium.webdriver.chrome.options import Options
 from selenium.webdriver.common.by import By
 imdport smtplib
 from email.mime.text import MIMEText
 from email.mime.multipart import MIMEMultipart
```

### Configuração do Gmail 📨

Se você inserir sua senha comum ao inserir seus dados de e-mail, o **código não funcionará**. Nesse caso, você deve usar outra senha que será gerada pelo **Google**.

1 - Vá para "Gerenciar sua conta do Google"

<br>

![image](https://github.com/Miguel-Marsico/Financial-updates-with-selenium/assets/158609724/85998236-064b-492e-ae5d-eb21def9912d)
<br>

2- Vá até a aba “Segurança” e “Verificação em duas etapas”. É obrigatório que este recurso esteja habilitado em sua conta.

<br>

![image](https://github.com/Miguel-Marsico/Financial-updates-with-selenium/assets/158609724/220cae17-7668-4931-bde0-9bcd766d9cde)

<br>

3- Vá em "Senhas de aplicativos" e crie um novo aplicativo e copie a senha gerada
<br>

![image](https://github.com/Miguel-Marsico/Financial-updates-with-selenium/assets/158609724/090e110a-08f5-4c8f-a35a-1e0f887f2056)

![image](https://github.com/Miguel-Marsico/Financial-updates-with-selenium/assets/158609724/7db99b28-fcf0-488b-b606-4ff141330521)

![image](https://github.com/Miguel-Marsico/Financial-updates-with-selenium/assets/158609724/62cf8111-4391-4a78-a704-16711a571e92)

### 💡 Será **impossível** visualizar a senha de um APP novamente, ela só aparece uma vez ao criá-lo

<br>

## 📜 Licença
### Este projeto está sob licença do MIT.
<br>
Desenvolvido por Miguel Marsico 👋🏻
