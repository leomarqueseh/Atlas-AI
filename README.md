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