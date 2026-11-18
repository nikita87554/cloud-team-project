# Cloud Team Project

**Cloud Team Project** — учебное контейнерное веб-приложение по дисциплине «Основы облачных технологий». Приложение отдаёт по HTTP каталог облачных сервисов с разделением на модели **IaaS / PaaS / SaaS** и упаковано в Docker-контейнер, поэтому одинаково запускается на локальном компьютере, виртуальной машине или в облаке.

## О проекте

Цель проекта — показать полный цикл работы с облачным приложением:

- хранение исходного кода в репозитории GitHub;
- описание зависимостей и конфигурации;
- сборка Docker-образа;
- запуск контейнера и проверка работы через HTTP.

## Архитектура

| Компонент | Назначение | Взаимодействие |
|-----------|------------|----------------|
| Пользователь | Отправляет HTTP-запросы через браузер или `curl` | Обращается к приложению на порту 5000 |
| Веб-приложение (Flask) | Обрабатывает запросы, реализует логику API | Читает данные из хранилища, формирует JSON-ответ |
| Хранилище данных | Файл `services.json` с каталогом сервисов | Используется приложением при запросе `/services` |
| Конфигурация | Безопасные параметры запуска (порт, путь к данным) | Читается приложением из переменных окружения при старте |
| Docker-контейнер | Изолированная среда выполнения | Содержит Python, зависимости и код приложения |

Подробная схема — в файле [docs/architecture.md](docs/architecture.md).

### Эндпоинты API

| Метод | Путь | Ответ |
|-------|------|-------|
| GET | `/` | Название проекта и статус |
| GET | `/health` | Проверка работоспособности |
| GET | `/services` | Список облачных сервисов |

## Структура репозитория

```
cloud-team-project/
├── app/
│   ├── main.py            # исходный код Flask-приложения
│   └── data/
│       └── services.json  # данные каталога сервисов
├── config/
│   └── .env.example       # пример конфигурации (без секретов)
├── docs/
│   └── architecture.md    # схема архитектуры
├── Dockerfile             # инструкция сборки образа
├── requirements.txt       # зависимости Python
├── .gitignore             # исключения для Git
└── README.md              # документация проекта
```

## Технологии

- [Git](https://git-scm.com/) и [GitHub](https://github.com/) — контроль версий и хостинг репозитория
- [Python 3.12](https://www.python.org/) — язык разработки
- [Flask](https://flask.palletsprojects.com/) — веб-фреймворк
- [Docker](https://www.docker.com/) — контейнеризация

## Запуск

### Предварительные требования

- установлен Git;
- установлен Docker (для запуска в контейнере) **или** Python 3.10+ (для локального запуска).

### Вариант 1. Запуск в Docker-контейнере

1. Клонировать репозиторий:
   ```bash
   git clone <URL_репозитория>
   cd cloud-team-project
   ```
2. Собрать образ:
   ```bash
   docker build -t cloud-team-project .
   ```
3. Запустить контейнер:
   ```bash
   docker run -d -p 5000:5000 --name cloud-app cloud-team-project
   ```
4. Проверить работу — открыть в браузере `http://localhost:5000/services` или выполнить:
   ```bash
   curl http://localhost:5000/health
   ```
5. Остановить и удалить контейнер:
   ```bash
   docker stop cloud-app && docker rm cloud-app
   ```

### Вариант 2. Локальный запуск без Docker

```bash
git clone <URL_репозитория>
cd cloud-team-project
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python app/main.py
```

## Конфигурация

Параметры задаются переменными окружения. Пример — в файле `config/.env.example`:

| Переменная | По умолчанию | Описание |
|------------|--------------|----------|
| `APP_PORT` | `5000` | Порт приложения |
| `DATA_FILE` | `app/data/services.json` | Путь к файлу данных |

> **Важно:** реальные пароли, токены и ключи доступа в репозиторий не добавляются. Файл `.env` внесён в `.gitignore`.

## Автор

| Участник | Группа | Роль |
|----------|--------|------|
| Ивашин Никита Александрович | ИСР-262 | Разработка приложения, Dockerfile, документация |

## Полезные ссылки

- [GitHub Docs: базовый синтаксис Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [GitHub Docs: About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
