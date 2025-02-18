# 📊 UMD Softball Performance Analytics ETL Pipeline  

## 🚀 Project Overview  
This project builds an **ETL pipeline** to extract, transform, and load **25 years of UMD Softball performance data** into **Snowflake** for analytics and reporting. The objective is to ensure **data accuracy, automation, and efficient querying**.  

## 🏗️ Key Features  
✔ **Data Extraction & Transformation:** Processed structured and unstructured data from historical records.  
✔ **Data Pipeline Development:** Automated ingestion via **AWS S3** and **Apache Airflow**.  
✔ **Data Cleaning & Processing:** Standardized formats, removed inconsistencies, and enriched datasets.  
✔ **Snowflake Integration:** Efficient loading into **Snowflake for scalable analysis**.  

---

## 📂 Repository Structure  
```
📁 umd-softball-etl
│── 📂 data/ # Raw and processed datasets
│── 📂 scripts/ # Python scripts for data processing & pipeline automation
│── 📂 dags/ # Apache Airflow DAGs for orchestration
│── 📂 notebooks/ # Jupyter notebooks for ETL development and testing
│── 📄 README.md # Project documentation
│── 📄 requirements.txt # List of required dependencies
```  

> **📢 Note:** Due to GitHub’s file size limitations, **large datasets are stored externally in AWS S3**. Contact the repo owner for access.  

---

## 🛠️ Tech Stack  
- **Languages:** Python  
- **Libraries:** `pandas`, `boto3`, `snowflake-connector-python`, `airflow`, `pyarrow`  
- **Data Storage:** AWS S3  
- **Workflow Orchestration:** Apache Airflow  
- **Database:** Snowflake  

---

## 📊 Results  
✅ **Automated ETL pipeline** with **end-to-end data flow**  
✅ **Integrated AWS S3 & Snowflake** for seamless storage and querying  
✅ **Scalable & efficient Airflow DAGs** for job orchestration  

---

## 📌 How to Run the Project  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/umd-softball-etl.git
   ```  

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

3. Set up AWS credentials for S3 access.  

4. Execute the pipeline:  
   - Run `scripts/convert_to_csv.py` to preprocess data.  
   - Run `scripts/upload_to_s3.py` to upload files to AWS S3.  
   - Run `scripts/etl_pipeline.py` to clean and transform data.  
   - Trigger **Apache Airflow DAGs** from `dags/softball_etl_dag.py`.  

---
## 📢 Future Improvements  
🔹 Implement **real-time data streaming** for continuous updates  
🔹 Optimize performance using **parallel processing & caching**  
🔹 Develop a **dashboard** for performance analytics in Snowflake  
🔹 Expand Airflow DAGs for incremental data loads  

---
## 📬 Contact  
For any questions, feel free to reach out via [LinkedIn](https://www.linkedin.com/in/tanmaysakharkar) or open an issue!  
