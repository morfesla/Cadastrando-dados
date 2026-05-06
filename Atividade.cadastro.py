import os
from dataclasses import dataclass

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


@dataclass
class Aluno:
    nome: str
    idade: int
    curso: str
    nota: float

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Curso: {self.curso}')
        print(f'Nota: {self.nota}\n')


def cadastrar_aluno():
    print('\n= Cadastro de aluno =')

    try:
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        curso = input('Curso: ')
        nota = float(input('Nota: '))

        aluno = Aluno(nome, idade, curso, nota)

        with open('alunos.csv', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{aluno.nome},{aluno.idade},{aluno.curso},{aluno.nota}\n')

        print('\nAluno cadastrado com sucesso!')

    except ValueError:
        print('\nErro: idade ou nota inválida!')

    input('\nPressione ENTER para continuar...')


def listar_alunos():
    print('\n= Lista de alunos =')

    try:
        with open('alunos.csv', 'r', encoding='utf-8') as arquivo:
            vazio = True

            for linha in arquivo:
                vazio = False
                nome, idade, curso, nota = linha.strip().split(',')
                aluno = Aluno(nome, int(idade), curso, float(nota))
                aluno.mostrar_dados()

            if vazio:
                print('Nenhum aluno cadastrado.')

    except FileNotFoundError:
        print('Arquivo não encontrado! Cadastre alunos primeiro.')

    except ValueError:
        print('Erro nos dados do arquivo.')

    input('\nPressione ENTER para continuar...')


while True:
    limpar_tela()
    print('--- SISTEMA ESCOLAR ---')
    print('1 - Cadastrar aluno')
    print('2 - Listar alunos')
    print('3 - Sair')

    opcao = input('\nEscolha: ')

    if opcao == '1':
        limpar_tela()
        cadastrar_aluno()

    elif opcao == '2':
        limpar_tela()
        listar_alunos()

    elif opcao == '3':
        print('\nSaindo...')
        break

    else:
        print('\nOpção inválida!')
        input('Pressione ENTER...')