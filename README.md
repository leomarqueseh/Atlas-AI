Markdown
# 🌌 ATLAS AI — Engine System

**Plataforma de Engenharia de Software com IA (Prompt-to-Production & Dynamic Canvas Builder)**

---

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/Frontend-React%20%7C%20TypeScript-61DAFB?logo=react)](https://react.dev/)
[![Docker](https://img.shields.io/badge/Deployment-Docker-2496ED?logo=docker)](https://www.docker.com/)

O **ATLAS AI** é uma plataforma de classe enterprise para engenharia de software automatizada. Diferente de assistentes de código convencionais (*co-pilots*) que apenas geram snippets isolados, o ATLAS AI atua como um engenheiro de software autônomo de nível *Staff*: analisa requisitos em linguagem natural, projeta a arquitetura, implementa bases de dados, constrói APIs REST e disponibiliza interfaces visuais interativas (**Canvas Drag & Drop**) para personalização de dashboards de Business Intelligence e páginas web.

Embora o ecossistema do **ATLAS AI** seja integralmente desenvolvido em **Python** (Backend) e **TypeScript/React** (Frontend), o engine de geração possui capacidade poliglota nativa, permitindo que o usuário escolha a linguagem e a stack de destino para os projetos exportados (Python, Go, Node.js, Java, C#, etc.).

---

## 🏛️ Visão Geral da Arquitetura

O coração do ecossistema é o **ATLAS Blueprint Engine™**, que utiliza o conceito de *Single Source of Truth* (SSOT). Toda a especificação da aplicação gerada — desde modelos de dados e segurança até a posição de cada widget no ecrã — é armazenada e atualizada através de um esquema rigorosamente tipado em JSON.

┌───────────────────────────┐
│   Prompt em Linguagem     │
│         Natural           │
└─────────────┬─────────────┘
│
▼
┌───────────────────────────┐
│ Requirement Analysis Engine│
└─────────────┬─────────────┘
│
▼
┌───────────────────────────┐
│  ATLAS Blueprint Engine™  │ ◄─────── Modificações do Usuário
│      (blueprint.json)     │          no Canvas Visual
└─────────────┬─────────────┘
│
├──────────────────────────────────────┐
▼                                      ▼
┌───────────────────────────┐          ┌───────────────────────────┐
│    Code Generation Engine │          │   Dynamic Visual Canvas   │
│ (Python, Go, Node, etc.)  │          │    (React-Grid-Layout)    │
└─────────────┬─────────────┘          └─────────────┬─────────────┘
│                                      │
└──────────────────┬───────────────────┘
│
▼
┌──────────────────────────┐
│ Artefatos de Produção &  │
│   Deploy (Docker/CI-CD)  │
└──────────────────────────┘


---

## ✨ Principais Capacidades

### 1. Geração Poliglota de Software
O usuário define a tecnologia de destino para o projeto gerado, e a IA compõe a solução aderindo às melhores práticas do ecossistema escolhido:
* **Backend:** Python (FastAPI, Django), Go (Gin, Fiber), Node.js (NestJS, Express), Java (Spring Boot), C# (.NET Core).
* **Frontend:** React, Next.js, Vue.js, Angular.
* **Bases de Dados:** PostgreSQL, MySQL, SQLite, MongoDB.

### 2. Interactive Canvas Builder (BI & Web)
* **Editor Visual Drag & Drop:** Interface em grid dinâmico que permite redimensionar, mover e reconfigurar widgets em tempo real.
* **Persistência Bidirecional:** Cada alteração efetuada no Canvas altera instantaneamente a estrutura no `blueprint.json`, garantindo sincronia total entre UI e código backend.
* **Widget Engine:** Componentes de BI nativos (KPI Cards, gráficos interativos via ECharts/Recharts e tabelas dinâmicas com filtros de dados).

### 3. Pipeline Integrada de Engenharia
* **Análise de Requisitos Automatizada:** Mapeamento de requisitos funcionais, não-funcionais e regras de negócio.
* **Modelagem de Dados & DB Migration:** Criação de schemas SQL/NoSQL e scripts de migração.
* **OpenAPI & Documentação Nativa:** Documentação interativa em padrão Swagger/OpenAPI gerada automaticamente.
* **Infrastructure as Code (IaC):** Arquivos `Dockerfile`, `docker-compose.yml` e workflows do GitHub Actions prontos para produção.

---

## 📂 Estrutura do Repositório Nacional (Core)

A plataforma **ATLAS AI** é construída em **Python 3.11+** e **React/TypeScript**:

```text
Atlas-AI/
├── backend/                  # Core Service (Python / FastAPI)
│   ├── app/
│   │   ├── api/              # Endpoints REST (Auth, Blueprints, Canvas, Generates)
│   │   ├── core/             # Configurações globais, segurança e JWT
│   │   ├── engines/          # Motores de IA (Requirements Engine & Code Generators)
│   │   ├── blueprints/       # Validadores e parsers do blueprint.json
│   │   ├── generators/       # Geradores de código multi-linguagem (Python, Go, Node)
│   │   ├── models/           # Modelos ORM (PostgreSQL via SQLAlchemy)
│   │   ├── schemas/          # Validações Pydantic (Dashboard Layout & Canvas Schemas)
│   │   └── main.py           # Ponto de entrada do serviço Backend
├── frontend/                 # Interface Web & Visual Builder (React / TypeScript)
│   ├── src/
│   │   ├── components/       # UI Primitives e Componentes Atômicos
│   │   ├── canvas/           # Construtor Visual Drag & Drop (React-Grid-Layout)
│   │   ├── store/            # Gerenciamento de Estado Global do Blueprint (Zustand)
│   │   └── pages/            # Módulos de Studio, Editor e Dashboard
├── docs/                     # Documentação de Arquitetura e Engenharia
├── docker-compose.yml        # Orquestração do ambiente completo de desenvolvimento
└── README.md
🚀 Quickstart (Ambiente de Desenvolvimento)
Pré-requisitos
Python 3.11+

Node.js 18+

Docker & Docker Compose

1. Clona o Repositório
Bash
git clone [https://github.com/open-source/atlas-ai.git](https://github.com/open-source/atlas-ai.git)
cd atlas-ai
2. Configuração do Backend (Python)
Bash
cd backend
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
3. Configuração do Frontend (Canvas Studio)
Bash
cd ../frontend
npm install
npm run dev
🛣️ Roadmap Estratégico
[x] Fase 1: Core Engine & Blueprints (Modelagem do Engine, Parsers em Python e Especificação JSON).

[ ] Fase 2: Visual Canvas & BI Studio (Implementação do Grid Drag & Drop, Integração do ECharts e Sincronização em Tempo Real).

[ ] Fase 3: Multi-Language Code Generators (Aprimoramento dos geradores para Go, Node.js e Java).

[ ] Fase 4: Multi-Agent Architecture & One-Click Cloud Deploy (Orquestração de agentes especializados e deploy automatizado em provedores Cloud).

📄 Licença
Este projeto é disponibilizado sob a Licença MIT. Para mais detalhes, consulte o arquivo LICENSE.