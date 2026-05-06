# 🚀 TCC DevOps — Automação de Testes

> **Trabalho de Conclusão de Curso** — Engenharia de Software · UniSATC · 2026  
> Análise do impacto das práticas DevOps na eficiência da automação de testes em projetos de software.

[![CI - Testes Automatizados com DevOps](https://github.com/LuizFilipeLinhares/tcc-devops-testes/actions/workflows/ci.yml/badge.svg)](https://github.com/LuizFilipeLinhares/tcc-devops-testes/actions/workflows/ci.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=LuizFilipeLinhares_tcc-devops-testes&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=LuizFilipeLinhares_tcc-devops-testes)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=LuizFilipeLinhares_tcc-devops-testes&metric=coverage)](https://sonarcloud.io/summary/new_code?id=LuizFilipeLinhares_tcc-devops-testes)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=LuizFilipeLinhares_tcc-devops-testes&metric=bugs)](https://sonarcloud.io/summary/new_code?id=LuizFilipeLinhares_tcc-devops-testes)

---

## 📌 Sobre o Projeto

Este repositório contém o experimento prático do TCC que investiga como a adoção de práticas **DevOps** impacta na eficiência da **automação de testes** em projetos de software.

O estudo compara dois cenários:

| Cenário | Abordagem | Execução |
|---|---|---|
| ❌ Sem DevOps | Testes manuais | Interação direta no navegador |
| ✅ Com DevOps | Testes automatizados | Pipeline CI/CD com GitHub Actions |

---

## 🏗️ Estrutura do Repositório

```
tcc-devops-testes/
├── .github/
│   └── workflows/
│       └── ci.yml          # Pipeline de CI/CD
├── app/                    # Aplicação web (HTML, CSS, JS)
├── tests/                  # Scripts de teste com Selenium
├── Dockerfile              # Configuração do ambiente conteinerizado
├── requirements.txt        # Dependências Python
└── sonar-project.properties # Configuração do SonarCloud
```

---

## 🛠️ Tecnologias Utilizadas

| Categoria | Ferramenta |
|---|---|
| Controle de versão | Git + GitHub |
| CI/CD | GitHub Actions |
| Automação de testes | Selenium WebDriver |
| Conteinerização | Docker |
| Qualidade de código | SonarCloud |
| Aplicação | HTML · CSS · JavaScript |

---

## ⚙️ Como Executar Localmente

### Pré-requisitos

- [Docker](https://www.docker.com/) instalado

### Rodando os testes

```bash
# Clone o repositório
git clone https://github.com/LuizFilipeLinhares/tcc-devops-testes.git
cd tcc-devops-testes

# Build da imagem
docker build -t tcc-devops-testes .

# Executa os testes
docker run --name tcc-tests tcc-devops-testes

# Copia o relatório gerado
docker cp tcc-tests:/app/report.html ./report.html
```

---

## 🔄 Pipeline CI/CD

A cada `push` ou `pull request` na branch `main`, a pipeline executa automaticamente:

```
Push/PR → Checkout → Build Docker → Testes Selenium → Relatório → SonarCloud → Deploy
```

1. **Checkout** do código-fonte
2. **Build** da imagem Docker
3. **Execução** dos testes automatizados com Selenium
4. **Upload** do relatório HTML como artefato
5. **Análise** de qualidade com SonarCloud
6. **Deploy** da aplicação no GitHub Pages *(apenas na `main`)*

---

## 📊 Métricas Avaliadas

As seguintes métricas são coletadas e comparadas entre os dois cenários:

- ⏱️ **Tempo de execução** dos testes
- 🐛 **Número de falhas** identificadas
- 🔁 **Frequência de execução**
- 👤 **Grau de intervenção humana**
- 📈 **Cobertura de testes** (via SonarCloud)

---

## 👨‍💻 Autores

| Nome | Contato |
|---|---|
| Luiz Filipe Romualdo Linhares | linharesluizfilipe@gmail.com |
| Mateus Zanin Fernandes | — |

**Orientador:** Prof. Deiezon Lemes — dieizon.lemes@satc.edu.br

---

## 🎓 Instituição

**Centro Universitário UniSATC** · Curso de Engenharia de Software · 2026-01

---

<p align="center">Feito com 💙 para o TCC de Engenharia de Software</p>
