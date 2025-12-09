#Atividade 1: Validador de Senha e Acesso

login_salvo = "admin_ti"
senha_salva = "Sistema@123"

login_digitado = input("Digite o login: ")
senha_digitada = input("Digite a senha: ")

if login_digitado == login_salvo and senha_digitada == senha_salva:
    print("Acesso Concedido. Bem-vindo ao Painel de Controle.")
elif login_digitado == "guest" and senha_digitada == "123456":
    print("Acesso Negado: Credenciais de baixo risco ou padrão de segurança.")
else:
    print("Erro de Acesso: Login ou Senha inválidos.")

#Atividade 2: Classificador de Prioridade de Chamados

# chamado = {
# "equipamento": "Servidor Principal",
# "tempo_parado_horas": 5,
# "setor": "Financeiro",
# "status": "aberto"
# }
#
# if chamado['equipamento'] == "Servidor Principal" or chamado['tempo_parado_horas'] > 4:
#     pri = "P1"
# elif chamado['setor'] == "Financeiro" and chamado['tempo_parado_horas'] > 1:
#     pri = "P2"
# else:
#     pri = "P3"
#
# print(chamado['equipamento'] + ", Prioridade: " + pri)