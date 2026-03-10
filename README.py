class LuizFernandoRibeiro:
    def __init__(self):
        self.name = "Luiz Fernando Ribeiro"
        self.role = "Back-End Developer"
        self.language = "pt-BR"
        self.location = "Brasil"

        self.about_me = {
            "experience": "Back-End com experiência em Python, Django, automações e integrações",
            "focus": [
                "Desenvolvimento Back-End",
                "Automação de tarefas",
                "Integração com APIs",
                "Manipulação de arquivos e documentos",
                "Inteligência Artificial",
                "Cybersegurança"
            ],
            "currently_learning": [
                "Java",
                "Cyber Security",
                "Arquitetura de sistemas",
                "Agentes de IA"
            ],
            "interests": [
                "Tecnologia",
                "Computação",
                "Hacking",
                "Rock",
                "Natureza",
                "Games"
            ]
        }

        self.skills = {
            "languages": ["Python", "JavaScript", "HTML", "CSS", "Java"],
            "frameworks": ["Django", "Flask"],
            "tools": ["Git", "GitHub", "APIs", "Automação", "OpenAI", "Google Cloud"],
            "knowledge": [
                "CRUDs e sistemas web",
                "Automação de e-mails",
                "Upload de arquivos para cloud",
                "Leitura e processamento de documentos",
                "Bots e assistentes virtuais",
                "Transcrição e diarização com IA"
            ]
        }

        self.projects = [
            "Automação para leitura de e-mails, download de anexos e upload no Google Storage",
            "Assistentes virtuais com GPT",
            "Transcrição de áudio para texto com IA",
            "Landing pages e sistemas com foco em automação e produtividade"
        ]

        self.goals = [
            "Evoluir como especialista em Back-End",
            "Aprofundar conhecimentos em Cybersegurança",
            "Criar soluções inteligentes com IA",
            "Desenvolver projetos escaláveis e úteis"
        ]

    def introduce(self):
        print("Olá, eu sou Luiz Fernando Ribeiro")
        print("Back-End Developer apaixonado por tecnologia, automação e construção de soluções inteligentes.\n")

        print("Sobre mim:")
        for key, value in self.about_me.items():
            print(f"- {key}: {value}")

        print("\nSkills:")
        for category, items in self.skills.items():
            print(f"- {category}: {', '.join(items)}")

        print("\nProjetos:")
        for project in self.projects:
            print(f"- {project}")

        print("\nObjetivos:")
        for goal in self.goals:
            print(f"- {goal}")

        print("\nVamos construir algo incrível.")

if __name__ == "__main__":
    profile = LuizFernandoRibeiro()
    profile.introduce()
