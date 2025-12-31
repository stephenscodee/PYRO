# 🔥 PYRO - AI Automation Platform

> **Tu operador digital personal en una app móvil. Habla con IA, crea automatizaciones complejas sin código ni flujos visuales.**

## 🎯 Visión

PYRO es una **IA dentro de una app móvil** que permite a cualquier usuario crear **automatizaciones complejas** usando lenguaje natural. Tú escribes *"cuando pase X, haz Y"* y PYRO construye, ejecuta y mantiene el workflow.

## 🚀 MVP v1.0

### Features Core
- ✅ **Chat con IA**: Crear automatizaciones en lenguaje natural
- ✅ **Ejecución de flujos**: Máximo 5 pasos por automatización  
- ✅ **Triggers básicos**: Webhook, cron (diario/semanal), email
- ✅ **Historial**: Logs simples y estado de ejecuciones
- ✅ **Conexiones**: Google Sheets, Notion, Email (SMTP), Webhooks genéricos
- ✅ **Autenticación**: OAuth 2.0 (Google) + email/password

### Límites MVP
- **Usuarios**: 100 usuarios beta
- **Automatizaciones**: 3 por usuario
- **Ejecuciones**: 100 por día por usuario
- **Almacenamiento**: 1GB por usuario

## 🏗️ Arquitectura

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React Native  │    │   Next.js       │    │   API Gateway   │
│   Mobile App    │    │   Dashboard     │    │   (Auth + RL)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
         ┌─────────────────────────────────────────────────┐
         │              Backend Services                   │
         │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐│
         │  │   Auth      │ │  Flow Engine│ │ Connectors  ││
         │  │  Service    │ │  (NestJS)   │ │ Service     ││
         │  └─────────────┘ └─────────────┘ └─────────────┘│
         └─────────────────────────────────────────────────┘
                                 │
         ┌─────────────────────────────────────────────────┐
         │                AI Service                       │
         │          FastAPI + Python                      │
         └─────────────────────────────────────────────────┘
                                 │
         ┌─────────────────────────────────────────────────┐
         │               Data Layer                        │
         │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐│
         │  │ PostgreSQL  │ │    Redis    │ │  S3 Storage ││
         │  │             │ │   (Jobs)    │ │  (Logs)     ││
         │  └─────────────┘ └─────────────┘ └─────────────┘│
         └─────────────────────────────────────────────────┘
```

## 📁 Estructura del Proyecto

```
pyro/
├── backend/                 # NestJS + TypeScript
│   ├── src/
│   │   ├── auth/           # OAuth 2.0 + JWT
│   │   ├── flows/          # Motor de automatizaciones
│   │   ├── connectors/     # Integraciones externas
│   │   └── webhooks/       # Triggers externos
│   └── package.json
├── ai/                     # FastAPI + Python
│   ├── src/
│   │   ├── nlp/            # Procesamiento lenguaje natural
│   │   ├── flow_gen/       # Generador de flujos
│   │   └── api/            # Endpoints REST
│   └── requirements.txt
├── mobile/                 # React Native + Expo
│   ├── src/
│   │   ├── screens/        # Pantallas principales
│   │   ├── components/     # Componentes UI
│   │   ├── services/       # API calls
│   │   └── store/          # Estado global
│   └── package.json
├── web/                    # Next.js Dashboard (opcional)
│   ├── src/
│   │   ├── app/            # App Router
│   │   ├── components/     # UI components
│   │   └── lib/            # Utilidades
│   └── package.json
├── infra/                  # Infraestructura
│   ├── docker/             # Dockerfiles
│   ├── docker-compose.yml  # Desarrollo local
│   └── k8s/                # Kubernetes (producción)
├── docs/                   # Documentación
│   ├── api/                # API docs
│   ├── deployment/         # Guías de deploy
│   └── examples/           # Ejemplos de flows
└── README.md
```

## 🛠️ Stack Tecnológico

### Backend
- **Framework**: NestJS (TypeScript)
- **Base de datos**: PostgreSQL 15+
- **Cache/Colas**: Redis 7+
- **Jobs**: BullMQ
- **Auth**: OAuth 2.0 + JWT

### AI Service  
- **Framework**: FastAPI (Python)
- **NLP**: OpenAI API / LlamaIndex
- **Procesamiento**: spaCy / transformers

### Frontend
- **Mobile**: React Native (Expo) + TypeScript
- **Web**: Next.js + TypeScript + TailwindCSS
- **Estado**: Zustand + React Query
- **Real-time**: Socket.IO

### Infraestructura
- **Container**: Docker + Docker Compose
- **Storage**: S3 compatible (MinIO dev)
- **Reverse Proxy**: Nginx

## 🚀 Quick Start

### Prerrequisitos
- Node.js 18+
- Python 3.11+
- Docker & Docker Compose
- PostgreSQL client (opcional)

### 1. Clonar y Setup
```bash
git clone https://github.com/tu-org/pyro.git
cd pyro
npm install
```

### 2. Iniciar Infraestructura
```bash
cd infra
docker-compose up -d postgres redis minio
```

### 3. Setup Backend
```bash
cd backend
npm install
npm run migration:run
npm run start:dev
```

### 4. Setup AI Service
```bash
cd ai
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn src.main:app --reload
```

### 5. Setup Mobile
```bash
cd mobile
npm install
npx expo start
```

## 📖 Documentación

- [Arquitectura Completa](./ARCHITECTURE.md)
- [API Documentation](./docs/api/README.md)
- [Deployment Guide](./docs/deployment/README.md)
- [Ejemplos de Flows](./docs/examples/README.md)

## 🤝 Contribuir

1. Fork el proyecto
2. Crear feature branch (`git checkout -b feature/amazing-feature`)
3. Commit cambios (`git commit -m 'Add amazing feature'`)
4. Push al branch (`git push origin feature/amazing-feature`)
5. Abrir Pull Request

## 📄 Licencia

MIT License - ver [LICENSE](LICENSE) para detalles.

## 🔮 Roadmap

### v1.1 (Post-MVP)
- [ ] Más conectores (Slack, Discord, Stripe)
- [ ] Flujos condicionales
- [ ] Variables y transformaciones
- [ ] Marketplace de flujos

### v2.0
- [ ] Flujos visuales opcionales
- [ ] Integraciones enterprise
- [ ] Advanced analytics
- [ ] Multi-tenant teams

---

**Built with ❤️ by the PYRO team**
