# 📦 Inventory Management System
 **Multi-Access with Remote Control**

**A complete system for inventory management featuring a high-performance API (FastAPI), desktop client (PyQt6), and PostgreSQL + Redis database.**

---

## 📂 Project Structure
```
inventory-system/  
├── 📁 backend/                 # Servidor da API
│   ├── 📁 app/
│   │   ├── 📁 core/            # Configurações centrais
│   │   ├── 📁 models/          # Modelos do banco de dados (SQLAlchemy)
│   │   ├── 📁 schemas/         # Schemas do Pydantic
│   │   ├── 📁 routes/          # Endpoints da API
│   │   │   ├── auth.py         # Autenticação
│   │   │   ├── products.py     # CRUD de produtos
│   │   │   ├── inventory.py    # Movimentações de estoque
│   │   │   └── reports.py      # Relatórios
│   │   ├── 📁 services/        # Lógica de negócio
│   │   ├── 📁 utils/           # Utilitários (cache, logs, etc.)
│   │   └── main.py             # Ponto de entrada da API
│   ├── requirements.txt        # Dependências do Python
│   └── Dockerfile              # Configuração do container
│
├── 📁 client/                  # Aplicação Desktop (GUI)
│   ├── 📁 views/               # Interfaces gráficas
│   ├── 📁 controllers/         # Lógica de interação com a API
│   ├── 📁 models/              # Modelos de dados locais
│   ├── main.py                 # Ponto de entrada da aplicação
│   └── requirements.txt        # Dependências
│
├── 📁 database/                # Configuração do banco de dados
│   ├── init.sql                # Script de criação do schema
│   ├── migrations/             # Scripts de migração
│   └── docker-compose.yml      # Configuração do container do banco
│
├── 📁 scripts/                 # Scripts utilitários
│   ├── backup_db.sh            # Script para backup do banco
│   └── deploy.sh               # Script de deploy do sistema
│
├── docker-compose.yml          # Orquestração do sistema completo
└── README.md                   # Documentação do projeto
```

---

## 🛠️ Technologies Used

| Component          | Technology Stack       |
|--------------------|------------------------|
| API Server         | FastAPI + Uvicorn      |
| Database           | PostgreSQL + Redis     |
| Desktop Client     | Python + PyQt6         |
| Authentication     | JWT + OAuth2           |
| Deployment         | Docker + Docker Compose|

---

## 🚀 Quick Start Guide

1. **Clone the repository**:
```bash
git clone https://github.com/your-username/inventory-system.git
cd inventory-system 
```

2. **Launch the system**:
```bash
docker-compose up -d
```

3. **Access the services**:

- API Docs: http://localhost:8000/docs

- Client App: Run client/main.py

---

## 📝 Key File Descriptions
1. **Backend API**:

* app/routes/products.py: Product management endpoints

* app/models/inventory.py: Stock movement models

* app/schemas/products.py: Data validation schemas

2. **Desktop Client**:

* views/main_window.py: Primary application window

* controllers/api_client.py: API communication handler

3. **Database**:

* database/init.sql: Initial schema setup

* database/migrations/: Versioned migration files
---
## 🌐 API Endpoint Examples
``` bash
# Sample FastAPI endpoint
@app.get("/products/{product_id}")
async def get_product(product_id: int):
    """Retrieve product details"""
    return {"id": product_id, "name": "Sample Product"}
```
---
## 🔒 Environment Variables
Create .env file in backend/:
``` bash
DB_URL=postgresql://user:password@db:5432/inventory
REDIS_URL=redis://redis:6379
JWT_SECRET=your-secret-key
```
---
## 📜 License
**MIT License - See LICENSE for details.**

---

This standardized English structure follows common naming conventions for:
* Clear, descriptive names

* Consistent casing (snake_case for Python files)

* Logical grouping of related components

* Separation of concerns


**The project is now ready for international collaboration and follows best practices for open-source Python projects.**