# 22. Mobile QA Automation Project

## 📱 Mobile tests for Wikipedia on BrowserStack

Автоматизация тестирования мобильного приложения Wikipedia с использованием современного стека:
* **BrowserStack** — облачная платформа для запуска тестов на реальных устройствах.
* **Appium** — фреймворк для автоматизации мобильных приложений.
* **Selene** — удобная обёртка над Selenium/Appium для Python.
* **Pytest** — тестовый фреймворк.
* **Allure** — генерация подробных отчетов о тестировании.
* **Jenkins** — инструмент непрерывной интеграции (CI/CD).

---

## ✅ Что реализовано


| Тест | Описание |
| :--- | :--- |
| `test_wikipedia_search` | Поиск текста "BrowserStack" в Wikipedia |
| `test_wikipedia_article_click` | Поиск статьи и клик по результату |

---

## 🚀 Запуск тестов локально

### 1. Клонировать репозиторий
```bash
git clone https://github.com/1DimonNT/22.Mobile-QA-Automation-Project.git
cd 22.Mobile-QA-Automation-Project
```

### 2. Создать виртуальное окружение
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

### 3. Установить зависимости
```bash
pip install -r requirements.txt
```

### 4. Настроить переменные окружения
Создайте файл `.env` в корне проекта на основе `.env.example` и добавьте ваши учетные данные BrowserStack:

```ini
BROWSERSTACK_USERNAME=your_username
BROWSERSTACK_ACCESS_KEY=your_access_key
APP_URL=bs://your_app_id
```

### 5. Запустить тесты
```bash
pytest tests/ --platform=android --alluredir=allure-results
```

### 6. Посмотреть Allure отчет
```bash
allure serve allure-results
```

---

## 🔧 Jenkins сборка

### Параметры окружения
* **Job name**: `22.Mobile-QA-Automation-Project`
* **Agent**: `python3-jenkins-agent-1`
* **Artifacts**: `allure-results`, `allure-report`

### Настройка Freestyle Job

1. **New Item** → имя: `22.Mobile-QA-Automation-Project` → **Freestyle project**

2. **Source Code Management** → Git
   * **Repository URL**: `https://github.com/1DimonNT/22.Mobile-QA-Automation-Project.git`
   * **Branch Specifier**: `*/main`

3. **Restrict where this project can be run**
   * **Label Expression**: `python3-jenkins-agent-1`

4. **Build Steps** → **Execute shell**:
```bash
#!/bin/bash
echo "===== Установка зависимостей ====="
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "===== Запуск мобильных тестов на BrowserStack ====="
# Рекомендуется использовать Jenkins Credentials плагин вместо хранения токенов в открытом виде
export BROWSERSTACK_USERNAME="mtpbahob_YhZvyK"
export BROWSERSTACK_ACCESS_KEY="4NMazF8xfcWYngjTSAaQ"
export REMOTE_URL="http://hub.browserstack.com/wd/hub"
export PLATFORM_NAME="android"
export DEVICE_NAME="Samsung Galaxy S23 Ultra"
export PLATFORM_VERSION="13.0"
export APP_URL="bs://51b4dd3c328b4cf8b59601552262b84a21fb39f8"
export TIMEOUT="45"

pytest tests/ -v --platform=android --alluredir=allure-results
```

5. **Post-build Actions** → **Allure Report**
   * **Path**: `allure-results`

### 🧪 Результаты тестов в Jenkins


| Тест | Статус |
| :--- | :--- |
| `test_wikipedia_search` | ✅ PASSED |
| `test_wikipedia_article_click` | ✅ PASSED |
| `test_ios_wikipedia` | ⏭️ SKIPPED (требует отдельной настройки iOS) |

---

## 📁 Структура проекта

```text
├── data/                      # Тестовые данные
├── pages/                     # Page Object модели для страниц/экранов
├── tests/                     # Тест-кейсы
├── utils/                     # Хелперы и утилиты (скриншоты, видео, логи Allure)
├── .env.example               # Пример файла конфигурации среды
├── .gitignore                 # Исключения для Git
├── config.py                  # Конфигурация проекта (Pydantic Settings)
├── conftest.py                # Общие фикстуры для тестов
├── pytest.ini                 # Конфигурационный файл Pytest
├── requirements.txt           # Список зависимостей проекта
├── README.md                  # Документация проекта
└── WikipediaApp/              # Тестируемое мобильное приложение
```

---

## 📦 Используемые технологии

* **Python 3.12+**
* **Appium-Python-Client 4.0.0**
* **Selene 2.0.0rc9**
* **Pytest 8.2.1**
* **Allure Pytest 2.13.5**
* **Pydantic 2.5.0**
* **BrowserStack**

---

## 📎 Ссылки

* [BrowserStack App Automate](https://browserstack.com)
* [Selene Documentation](https://github.io)
* [Appium Python Client](https://github.com)

---

## 👤 Автор

**Dmitrii Ivantsov**  
*QA Automation Engineer*
