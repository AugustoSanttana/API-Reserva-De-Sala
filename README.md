📘 API de Reservas de Sala

Descrição
API responsável por gerenciar reservas de salas vinculadas a turmas e professores. Valida entidades consultando outro microsserviço externo (API da escola).

Como executar

Pré-requisitos
- Docker
- Docker Compose

Passos
1. Clone o repositório:
bash
git clone <seu-repo>.git
cd <seu-repo>
Execute com Docker:

bash

docker-compose up --build
Acesse a API em: http://localhost:8001

Endpoints principais
GET /turmas_disponiveis
Retorna todas as turmas ativas disponíveis para reserva.

GET /reservas
Retorna todas as reservas registradas no sistema.

POST /reservar_sala
Cria uma nova reserva de sala.

Tecnologias utilizadas
Python 3.12

Flask

PostgreSQL

SQLAlchemy

Docker

Integração com Microsserviços
Esta API depende da API da escola para validar turmas e professores, fazendo chamadas HTTP para os seguintes endpoints externos:

GET /turmas/<id>

GET /professores/<id>

Esses endpoints devem estar ativos e acessíveis via http://localhost:8000.

Status
✅ API funcional e integrada com verificação externa. Pronta para testes e deploy.







