# Soccer Data Ingestion Pipeline (Airflow & Snowflake)
> **Pipeline de Ingesta de Datos de Fútbol utilizando Airflow y Snowflake**

---

## Overview / Resumen

**EN:** This project implements an automated ETL pipeline that extracts top soccer league data using Python, orchestrates the flow with Apache Airflow (running on Docker via Astro CLI), and performs a bulk load into a Snowflake Cloud Data Warehouse.

**ES:** Este proyecto implementa un pipeline ETL automatizado que extrae datos de las principales ligas de fútbol usando Python, orquestando el flujo con Apache Airflow (ejecutándose en Docker vía Astro CLI) y realizando una carga masiva (Bulk Load) en el Data Warehouse de Snowflake.

---

## Architecture / Arquitectura

[Image of Data Engineering Architecture showing Airflow Docker Snowflake and Python integration]

1. **Extraction (Python/Pandas):** Local data generation/extraction.
2. **Orchestration (Airflow):** Automated workflow management.
3. **Staging (Snowflake Stage):** Intermediate landing area in the cloud.
4. **Storage (Snowflake Table):** Final data structured in a Data Warehouse.

---

## 🛠️ Tech Stack / Tecnologías

| Tool / Herramienta | Purpose / Propósito |
| :--- | :--- |
| **Python 3.12** | Extraction and data manipulation (Pandas). |
| **Apache Airflow** | Workflow orchestration (TaskFlow API). |
| **Snowflake** | Cloud Data Warehousing & SQL Analytics. |
| **Docker** | Containerization for environment consistency. |
| **Astro CLI** | Local development and deployment tool. |

---

## 🚀 Key Features / Características Clave

* **Bilingual Documentation:** Detailed instructions in English and Spanish.
* **Modern Airflow Syntax:** Uses the latest TaskFlow API (`@dag`, `@task`).
* **Optimized Loading:** Implements `PUT` and `COPY INTO` for high-performance bulk loading.
* **Security Focused:** Environment variables and `.gitignore` integration to protect credentials.

---

## 📖 Setup & Usage / Configuración y Uso

### Prerequisites / Requisitos
* Docker Desktop
* Astro CLI
* Snowflake Account

### Steps / Pasos
1. **Clone the repo:** `git clone https://github.com/your-user/soccer-airflow-snowflake.git`
2. **Start the environment:** `astro dev start`
3. **Configure Connection