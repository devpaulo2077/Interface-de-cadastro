import customtkinter as cust
import mysql.connector


class TelaLogin:


    def __init__(self):
        #DEFININDO TEMAS PARA A TELA
        cust.set_appearance_mode("dark")
        cust.set_default_color_theme("dark-blue")

        #ADICIONANDO O CUSTOMTKINTER EM UMA VARIAVEL PARA SER ATIVADO
        self.janela = cust.CTk()
        #DEFININDO O TAMANHO DA JANELA SENDO "500" (EXEMPLO) A LARGURA E "300" (EXEMPLO) A ALTURA
        self.janela.geometry("500x300")
        #APENAS INSERINDO UM TEXTO
        self.texto = cust.CTkLabel(self.janela, text="Fazer Cadastro")
        self.texto.pack(padx=10, pady=10)
        #APENAS INSERINDO UM CAMPO PARA INSERIR COISAS
        self.nome = cust.CTkEntry(self.janela, placeholder_text='Nome')
        self.nome.pack(padx=10, pady=10)

        self.username = cust.CTkEntry(self.janela, placeholder_text='Username')
        self.username.pack(padx=10, pady=10)

        self.senha = cust.CTkEntry(self.janela, placeholder_text='Senha', show="*")
        self.senha.pack(padx=10, pady=10)
        #APENAS INSERINDO UM BOTÃO
        self.botao = cust.CTkButton(self.janela, text="Cadastrar", command=self.click)
        self.botao.pack(padx=10, pady=10)
        #APENAS INSERINDO UM BOTÃO DE CHECK PODENDO SER MARCADO OU DESMARCADO
        self.lembrete = cust.CTkCheckBox(self.janela, text="Lembrar Login")
        self.lembrete.pack(padx=10, pady=10)
        #self.janela.bind("<KeyRelease>", self.onclick)
        #ENCERRANDO A JANELA
        self.janela.mainloop()


    def click(self):
        conexao = mysql.connector.connect(
        host='nome-do-host-aqui',
        user='user-aqui',
        password='password',
        database='nome-db',
        )

        cursor = conexao.cursor()
        query = f'INSERT INTO usuário (NOME, USERNAME, SENHA) VALUES ("{self.nome.get()}", "{self.username.get()}", {self.senha.get()});'
        cursor.execute(query) #Executa
        conexao.commit()
        cursor.close()
        conexao.close()

        print(self.nome.get())
    def onclick(self,event):
        print(self.nome.get())

TelaLogin()