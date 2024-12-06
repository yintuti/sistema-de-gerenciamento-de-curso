class Curso:

  def __init__(self, nome_curso, codigo):
    self.nome_curso = nome_curso
    self.codigo = codigo
    self.Professor = None
    self.Aluno = []
    self.Aula = []

  def setNome_curso(self, nome_curso):
    self.nome_curso = nome_curso

  def setCodigo(self, codigo):
    self.codigo = codigo

  def setProfessor(self, Professor):
    self.Professor = Professor

  def setAluno(self, Aluno):
    self.Aluno = Aluno

  def setAula(self, Aula):
    self.Aula = Aula

  def getNome_curso(self):
    return self.nome_curso

  def getCodigo(self):
    return self.codigo

  def getProfessor(self):
    return self.Professor

  def getAluno(self):
    return self.Aluno

  def getAula(self):
    return self.Aula

  def __str__(self):
    return f"Curso: {self.nome_curso}, Código: {self.codigo}, Professor: {self.Professor}, Aluno: {self.Aluno}, Aula: {self.Aula}"


class Pessoa:

  def __init__(self, nome):
    self.nome = nome

  def setNome(self, nome):
    self.nome = nome

  def getNome(self):
    return self.nome

  def exibir_informacoes(self):
    return f"Pessoa: {self.nome}"


class Aluno(Pessoa):

  def __init__(self, nome, matricula, Curso):
    super().__init__(nome)
    self.matricula = matricula
    self.Curso = Curso

  def setMatricula(self, matricula):
    self.matricula = matricula

  def setCurso(self, Curso):
    self.Curso = Curso

  def getMatricula(self):
    return self.matricula

  def getCurso(self):
    return self.Curso

  def exibir_informacoes(self):
    return f"Aluno: {self.nome}, Matrícula: {self.matricula}, Curso: {self.Curso.getNome_curso()}"


class Professor(Pessoa):

  def __init__(self, nome, id_professor, Curso):
    super().__init__(nome)
    self.id_professor = id_professor
    self.Curso = Curso

  def setId_professor(self, id_professor):
    self.id_professor = id_professor

  def setCurso(self, Curso):
    self.Curso = Curso

  def getId_professor(self):
    return self.id_professor

  def getCurso(self):
    return self.Curso

  def exibir_informacoes(self):
    return f"Professor: {self.nome}, ID: {self.id_professor}, Curso: {self.Curso.getNome_curso()}"


class Aula:

  def __init__(self, nome_aula, Curso):
    self.nome_aula = nome_aula
    self.Curso = Curso

  def setNome_aula(self, nome_aula):
    self.nome_aula = nome_aula

  def setCurso(self, Curso):
    self.Curso = Curso

  def getNome_aula(self):
    return self.nome_aula

  def getCurso(self):
    return self.Curso


cursos = []
alunos = []
professores = []
aulas = []
pessoas = []

while True:
  print("<><><><><><><><><><><><><><><><><><><><><><><><><>")
  print("\nMenu:\n")
  print("1 - Cadastrar curso, aluno ou professor")
  print("2 - Listar cursos, alunos ou professores")
  print("3 - Adicionar uma aula a um curso")
  print("4 - Gerenciar")
  print("5 - Remover curso, aluno ou professor")
  print("6 - Sair")

  opcao = input("\nEscolha uma opção: ")

  if opcao not in ["1", "2", "3", "4", "5", "6"]:
    print("\nOpção inválida!\n")
    continue

  elif opcao == "1":
    while True:
      print("\n1 - Cadastrar curso")
      print("2 - Cadastrar aluno")
      print("3 - Cadastrar professor")
      print("4 - Voltar")

      opcao2 = input("\nEscolha uma opção: ")

      if opcao2 not in ["1", "2", "3", "4"]:
        print("\nOpção inválida!")
        continue

      elif opcao2 == "1":
        nome_curso = input("Nome do curso: ")
        codigo = input("Código do curso: ")
        novo_curso = Curso(nome_curso, codigo)
        cursos.append(novo_curso)
        print("\nCurso cadastrado com sucesso!\n")
        break

      elif opcao2 == "2":
        nome = input("Nome do aluno: ")
        matricula = input("Matrícula do aluno: ")
        if not cursos:
          print("\nNenhum curso cadastrado ainda.\n")
          break
        print("\nEscolha um curso:")
        for i, curso in enumerate(cursos):
          print(f"{i + 1} - {curso.getNome_curso()}")
        curso_opcao = int(input("\nEscolha o número do curso: ")) - 1
        if curso_opcao < 0 or curso_opcao >= len(cursos):
          print("\nOpção inválida!")
          continue
        curso_aluno = cursos[curso_opcao]
        novo_aluno = Aluno(nome, matricula, curso_aluno)
        alunos.append(novo_aluno)
        pessoas.append(novo_aluno)
        print("\nAluno cadastrado com sucesso!\n")
        break

      elif opcao2 == "3":
        nome = input("Nome do professor: ")
        id_professor = input("ID do professor: ")
        if not cursos:
          print("\nNenhum curso cadastrado ainda.\n")
          break
        print("\nEscolha um curso:")
        print("0 - Não atribuir a um curso")
        for i, curso in enumerate(cursos):
          print(f"{i + 1} - {curso.getNome_curso()}")
        curso_opcao = int(input("\nEscolha o número do curso: "))
        if curso_opcao == 0:
          novo_professor = Professor(nome, id_professor, None)
        elif 1 <= curso_opcao <= len(cursos):
          curso_professor = cursos[curso_opcao - 1]
          novo_professor = Professor(nome, id_professor, curso_professor)
          curso_professor.setProfessor(novo_professor)
        else:
          print("\nOpção inválida!")
          continue
        professores.append(novo_professor)
        pessoas.append(novo_professor)
        print("\nProfessor cadastrado com sucesso!\n")
        break

      elif opcao2 == "4":
        print()
        break

  elif opcao == "2":
    while True:
      print("\n1 - Listar cursos")
      print("2 - Listar alunos")
      print("3 - Listar professores")
      print("4 - Listar todas pessoas cadastradas")
      print("5 - Voltar")

      opcao2 = input("\nEscolha uma opção: ")

      if opcao2 not in ["1", "2", "3", "4", "5"]:
        print("\nOpção inválida!")
        continue

      elif opcao2 == "1":
        if not cursos:
          print("\nNenhum curso cadastrado.\n")
        else:
          print("\nCursos cadastrados: \n")
          for curso in cursos:
            print(f"Curso: {curso.getNome_curso()}, Código: {curso.getCodigo()}")
          print()
        break

      elif opcao2 == "2":
        if not alunos:
          print("\nNenhum aluno cadastrado.\n")
        else:
          print("\nAlunos matrículados: ")
          for aluno in alunos:
            print(f"Aluno: {aluno.getNome()} - Matrícula: {aluno.getMatricula()} - Curso: {aluno.getCurso().getNome_curso()}")
          print()
        break

      elif opcao2 == "3":
        if not professores:
          print("\nNenhum professor cadastrado.\n")
        else:
          print("\nProfessores cadastrados: ")
          for professor in professores:
            print(f"Professor: {professor.getNome()} - ID: {professor.getId_professor()}")
          print()
        break

      elif opcao2 == "4":
        if not pessoas:
          print("\nNenhuma pessoa cadastrada.\n")
        else:
          print("\nPessoas cadastradas: ")
          for pessoa in pessoas:
            print(f"Pessoa: {pessoa.getNome()}")
          print()
        break

      elif opcao2 == "5":
        print()
        break

  elif opcao == "3":
    while True:
      if not cursos:
        print("\nNenhum curso cadastrado ainda.\n")
        break
      nome_aula = input("\nNome da aula: ")
      print("\nCursos:")
      for i, curso in enumerate(cursos):
        print(f"{i + 1} - {curso.getNome_curso()}")
      curso_opcao = int(input("\nEscolha o número do curso: ")) - 1
      if 0 <= curso_opcao < len(cursos):
        curso_aula = cursos[curso_opcao]
        nova_aula = Aula(nome_aula, cursos[curso_opcao])
        aulas.append(nova_aula)
        print("\nAula cadastrada com sucesso!\n")
        break
      else:
        print("\nOpção inválida!\n")

  elif opcao == "4":
    while True:
      print("\n1 - Gerenciar cursos")
      print("2 - Gerenciar alunos")
      print("3 - Gerenciar professores")
      print("4 - Voltar")

      opcao2 = input("\nEscolha uma opção: ")

      if opcao2 not in ["1", "2", "3", "4"]:
        print("\nOpção inválida!")
        continue

      elif opcao2 == "1":
        if not cursos:
          print("\nNenhum curso cadastrado.\n")
          break

        print("\nCursos disponíveis para gerenciar:")
        for idx, curso in enumerate(cursos):
          print(f"{idx + 1} - {curso.getNome_curso()} (Código: {curso.getCodigo()})")

        try:
          opcao3 = int(input("\nEscolha o número do curso que deseja gerenciar: ")) - 1
          if 0 <= opcao3 < len(cursos):
            curso_selecionado = cursos[opcao3]
            print(f"\nCurso Selecionado: {curso_selecionado.getNome_curso()}")
            while True:
              print("\nGerenciar curso:")
              print("1 - Exibir alunos e professor do curso")
              print("2 - Editar nome do curso")
              print("3 - Editar código do curso")
              print("4 - Editar professor do curso")
              print("5 - Editar aulas do curso")
              print("6 - Voltar")

              opcao4 = input("\nEscolha uma opção: ")

              if opcao4 not in ["1", "2", "3", "4", "5", "6"]:
                print("\nOpção inválida!")
                continue

              elif opcao4 == "1":
                print("\nAlunos e professor do curso:")
                professor = curso_selecionado.getProfessor()
                if professor:
                  print(f"Professor: {professor.getNome()}")
                else:
                  print("Professor não atribuído ainda.")
                for aluno in alunos:
                  if aluno.getCurso() == curso_selecionado:
                    print(f"Aluno: {aluno.getNome()}")

              elif opcao4 == "2":
                print(f"\nAtual nome do curso: {curso_selecionado.getNome_curso()}")
                novo_nome = input("\nNovo nome do curso: ")
                curso_selecionado.setNome_curso(novo_nome)
                print("\nNome atualizado com sucesso!")

              elif opcao4 == "3":
                print(f"Atual código do curso: {curso_selecionado.getCodigo()}")
                novo_codigo = input("\nNovo código do curso: ")
                curso_selecionado.setCodigo(novo_codigo)
                print("\nCódigo atualizado com sucesso!")

              elif opcao4 == "4":
                if curso_selecionado.getProfessor() is not None:
                  print(f"Atual professor do curso: {curso_selecionado.getProfessor().getNome()}")
                else:
                  print(
                      "Atual professor do curso: Nenhum professor atribuído.")
                if not professores:
                  print("\nNenhum professor cadastrado.\n")
                else:
                  print("\nProfessores disponíveis:")
                  for i, professor in enumerate(professores):
                    print(f"{i + 1} - {professor.getNome()}")
                  try:
                    novo_professor = int(
                        input(f"\nEscolha o novo professor do curso: ")) - 1
                    if 0 <= novo_professor < len(professores):
                      curso_selecionado.setProfessor(
                          professores[novo_professor])
                      print("\nProfessor atualizado com sucesso!")
                      break
                    else:
                      print(f"Seleção inválida! Por favor, escolha um número entre 1 e {len(professores)}.")
                  except ValueError:
                    print("Entrada inválida! Por favor, digite um número válido.")

              elif opcao4 == "5":
                if not aulas:
                  print("Nenhuma aula cadastrada.")
                  break
                print("Aulas disponíveis para editar:")
                contador = 1
                for aula in aulas:
                  if aula.getCurso() == curso_selecionado:
                    print(f"{contador} - {aula.getNome_aula()}")
                    contador += 1

                try:
                  opcao_aula = int(input("\nEscolha o número da aula que deseja editar: ")) - 1
                  if 0 <= opcao_aula < len(aulas):
                    aula_selecionada = aulas[opcao_aula]
                    print(f"\nAula selecionada: {aula_selecionada.getNome_aula()}")
                    while True:
                      print("\nGerenciar aula:")
                      print("1 - Editar nome da aula")
                      print("2 - Voltar")

                      opcao5 = input("\nEscolha uma opção: ")

                      if opcao5 not in ["1", "2"]:
                        print("\nOpção inválida!")
                        continue

                      elif opcao5 == "1":
                        print(f"\nNome atual da aula: {aula_selecionada.getNome_aula()}")
                        novo_nome = input("Novo nome da aula: ")
                        aula_selecionada.setNome_aula(novo_nome)
                        print("\nNome atualizado com sucesso!")
                        break

                      elif opcao5 == "2":
                        break

                  else:
                    print("\nOpção inválida!")

                except ValueError:
                  print("Entrada inválida! Por favor, digite um número válido.")

              elif opcao4 == "6":
                break

          else:
            print("\nOpção inválida!")

        except ValueError:
          print("\nEntrada inválida! Digite um número.")

      elif opcao2 == "2":
        if not alunos:
          print("\nNenhum aluno cadastrado.\n")
          break

        print("\nAlunos cadastrados:")
        for idx, aluno in enumerate(alunos):
          print(f"{idx + 1} - {aluno.getNome()} - Matrícula: {aluno.getMatricula()} - Curso: {aluno.getCurso().getNome_curso()}")

        try:
          opcao3 = int(
              input("\nEscolha o número do aluno que deseja gerenciar: ")) - 1
          if 0 <= opcao3 < len(alunos):
            aluno_selecionado = alunos[opcao3]
            print(f"\nAluno Selecionado: {aluno_selecionado.getNome()}")
            while True:
              print("\nGerenciar aluno:")
              print("1 - Exibir curso do aluno")
              print("2 - Editar nome do aluno")
              print("3 - Editar matrícula do aluno")
              print("4 - Editar curso do aluno")
              print("5 - Voltar")

              opcao4 = input("\nEscolha uma opção: ")

              if opcao4 not in ["1", "2", "3", "4", "5"]:
                print("\nOpção inválida!")
                continue

              elif opcao4 == "1":
                print(f"\nCurso do aluno: {aluno_selecionado.getCurso().getNome_curso()}")

              elif opcao4 == "2":
                print(f"\nNome do aluno: {aluno_selecionado.getNome()}")
                novo_nome = input("Novo nome do aluno: ")
                aluno_selecionado.setNome(novo_nome)
                print("\nNome atualizado com sucesso!")

              elif opcao4 == "3":
                print(f"\nMatrícula do aluno: {aluno_selecionado.getMatricula()}")
                nova_matricula = input("Nova matrícula do aluno: ")
                aluno_selecionado.setMatricula(nova_matricula)
                print("\nMatrícula atualizada com sucesso!")

              elif opcao4 == "4":
                print(f"\nCurso atual do aluno: {aluno_selecionado.getCurso().getNome_curso()}")
                print("\nCursos disponíveis:")
                for i, curso in enumerate(cursos):
                  print(f"{i + 1} - {curso.getNome_curso()}")
    
                try:
                  opcao_curso = int(input("\nEscolha o número do novo curso: ")) - 1
                  if 0 <= opcao_curso < len(cursos):
                    novo_curso = cursos[opcao_curso]
                    aluno_selecionado.setCurso(novo_curso)
                    print("\nCurso atualizado com sucesso!")
                  else:
                    print("\nOpção inválida!")
                except ValueError:
                  print("\nEntrada inválida! Por favor, digite um número.")

              elif opcao4 == "5":
                break

          else:
            print("\nOpção inválida!")

        except ValueError:
          print("\nEntrada inválida! Digite um número.")

      elif opcao2 == "3":
        if not professores:
          print("\nNenhum professor cadastrado.\n")
          break

        print("\nProfessores cadastrados:")
        for idx, aluno in enumerate(professores):
          print(f"{idx + 1} - {aluno.getNome()} - ID: {aluno.getId_professor()}")

        try:
          opcao3 = int(input("\nEscolha o número do professor que deseja gerenciar: ")) - 1
          if 0 <= opcao3 < len(professores):
            professor_selecionado = professores[opcao3]
            print(f"\nAluno Selecionado: {professor_selecionado.getNome()}")
            while True:
              print("\nGerenciar professor:")
              print("1 - Editar nome do professor")
              print("2 - Editar ID do professor")
              print("3 - Voltar")

              opcao4 = input("\nEscolha uma opção: ")

              if opcao4 not in ["1", "2", "3"]:
                print("\nOpção inválida!")
                continue

              elif opcao4 == "1":
                print(f"\nNome do professor: {professor_selecionado.getNome()}")
                novo_nome = input("Novo nome do professor: ")
                professor_selecionado.setNome(novo_nome)
                print("\nNome atualizado com sucesso!")

              elif opcao4 == "2":
                print(f"\nID do professor: {professor_selecionado.getId_professor()}")
                novo_ID = input("Novo ID do professor: ")
                professor_selecionado.setId_professor(novo_ID)
                print("\nID atualizado com sucesso!")

              elif opcao4 == "3":
                break

          else:
            print("\nOpção inválida!")

        except ValueError:
          print("\nEntrada inválida! Digite um número.")

      elif opcao2 == "4":
        break

  elif opcao == "5":
    while True:
      print("\n1 - Remover curso")
      print("2 - Remover aluno")
      print("3 - Remover professor")
      print("4 - Voltar")

      opcao2 = input("\nEscolha uma opção: ")

      if opcao2 not in ["1", "2", "3", "4"]:
        print("\nOpção inválida!")
        continue

      elif opcao2 == "1":
        if not cursos:
          print("\nNenhum curso cadastrado.\n")
          break

        print("\nCursos cadastrados:")
        for idx, curso in enumerate(cursos):
          print(f"{idx + 1} - {curso.getNome_curso()} (Código: {curso.getCodigo()})")

        try:
          opcao3 = int(input("\nEscolha o número do curso que deseja remover: ")) - 1
          if 0 <= opcao3 < len(cursos):
            curso_selecionado = cursos[opcao3]
            cursos.remove(curso_selecionado)
            print(f"\nCurso '{curso_selecionado.getNome_curso()}' removido com sucesso!\n")
            break

          else:
            print("\nOpção inválida!")

        except ValueError:
          print("Entrada inválida! Digite um número.")

      elif opcao2 == "2":
        if not alunos:
          print("\nNenhum aluno cadastrado.\n")
          break

        print("\nAlunos cadastrados:")
        for idx, aluno in enumerate(alunos):
          print(f"{idx + 1} - {aluno.getNome()} - Matrícula: {aluno.getMatricula()} - Curso: {aluno.getCurso().getNome_curso()}")

        try:
          opcao3 = int(input("\nEscolha o número do aluno que deseja remover: ")) - 1
          if 0 <= opcao3 < len(alunos):
            aluno_selecionado = alunos[opcao3]
            alunos.remove(aluno_selecionado)
            print(f"\nAluno '{aluno_selecionado.getNome()}' removido com sucesso!\n")
            break

          else:
            print("\nOpção inválida!")

        except ValueError:
          print("Entrada inválida! Digite um número.")

      elif opcao2 == "3":
        if not professores:
          print("\nNenhum professor cadastrado.\n")
          break

        print("\nProfessores cadastrados:")
        for idx, professor in enumerate(professores):
          print(f"{idx + 1} - {professor.getNome()} - ID: {professor.getId_professor()}")

        try:
          opcao3 = int(
              input("\nEscolha o número do professor que deseja remover: ")) - 1
          if 0 <= opcao3 < len(professores):
            professor_selecionado = professores[opcao3]
            professores.remove(professor_selecionado)
            print(f"\nProfessor '{professor_selecionado.getNome()}' removido com sucesso!\n")
            break

          else:
            print("\nOpção inválida!")

        except ValueError:
          print("Entrada inválida! Digite um número.")

      elif opcao2 == "4":
        print()
        break

  elif opcao == "6":
    print("\nSaindo do programa...")
    break