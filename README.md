# Weather Notification App (Twilio & AWS EC2)
> **App de Notificaciones Climáticas utilizando Twilio y AWS EC2**

---

## Overview / Resumen

**EN:** This Data Engineering and DevOps project automates the daily retrieval of weather forecasts using WeatherAPI and sends instant SMS notifications via Twilio. The script is deployed on an AWS EC2 instance and scheduled for unattended execution using Linux `cron`.

**ES:** Este proyecto de Ingeniería de Datos y DevOps automatiza la descarga diaria de pronósticos del clima usando WeatherAPI y envía notificaciones instantáneas vía SMS a través de Twilio. El script está desplegado en una instancia AWS EC2 y programado para ejecutarse de forma desatendida mediante Linux `cron`.

---

## Architecture / Arquitectura



1. **Extraction (Python/Requests):** Fetches real-time weather data from WeatherAPI.
2. **Processing (Pandas):** Structures and filters relevant weather alerts.
3. **Notification (Twilio API):** Sends automated SMS messages to the user.
4. **Cloud Deployment (AWS EC2):** Hosts the application in a scalable Linux environment.
5. **Scheduling (Cron):** Automates the daily execution of the data pipeline.

---

## Tech Stack / Tecnologías

| Tool / Herramienta | Purpose / Propósito |
| :--- | :--- |
| **Python 3.x** | Core logic and data processing (Pandas, Requests). |
| **AWS EC2 (Ubuntu)** | Cloud production server for deployment. |
| **Twilio API** | Communication platform for SMS delivery. |
| **WeatherAPI** | External data source for weather forecasting. |
| **Linux Cron** | Task scheduling for workflow automation. |
| **Git / GitHub** | Version control and secure code management. |

---

## Key Features / Características Clave

* **Bilingual Documentation:** Full project details in both English and Spanish.
* **Security Focused:** Implementation of Environment Variables (`os.environ.get`) to protect API keys.
* **History Cleanup:** Specialized Git cleaning to remove sensitive data from the repository history.
* **Production Ready:** Includes a Shell wrapper script for robust automation in Linux environments.

---

## Setup & Usage / Configuración y Uso

### Prerequisites / Requisitos
* Python 3.x
* Twilio Account & WeatherAPI Key
* AWS Account (EC2 Instance)

### Steps / Pasos

#### EN:
1. **Clone the repo:** `git clone https://github.com/AbrahamRodriguez97/ClimaNotifierEC2.git`
2. **Environment Setup:** Create a `venv` and install dependencies:  
   `python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
3. **Configuration:** Create a `.env` file with your `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `WEATHER_API_KEY`.
4. **Automation:** Configure `crontab -e` to execute the `run_notifier.sh` script daily.

#### ES:
1. **Clonar el repo:** `git clone https://github.com/AbrahamRodriguez97/ClimaNotifierEC2.git`
2. **Configuración del Entorno:** Crear un `venv` e instalar dependencias:  
   `python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
3. **Configuración de Claves:** Crear un archivo `.env` con tus credenciales de Twilio y WeatherAPI.
4. **Automatización:** Configurar `crontab -e` para ejecutar el script `run_notifier.sh` diariamente.

---
