#  YouTube Data Engineering Project using AWS (My First AWS end to end Project)

##  Introduction

This is my first hands-on data engineering project using AWS tools and services. I followed along with a tutorial and successfully replicated the entire pipeline to manage and analyze YouTube trending videos data. The project helped me understand how to design and implement a scalable data pipeline on the cloud using services like AWS Glue, S3, Athena, and QuickSight.

Through this experience, I learned a lot about the AWS ecosystem, setting up ETL workflows, using crawlers, and building visualizations—all while handling real-world semi-structured data.

---

## Project Architecture
![architecture](https://github.com/user-attachments/assets/93c20ad8-18fd-4fa2-a6b4-58c4ad236e18)


## ☁️ AWS Services Used
- **Amazon S3**
- **AWS IAM**
- **AWS Lambda**
- **AWS Glue**
- **AWS Athena**
- **Amazon QuickSight**


## 🗃️ Dataset Used

I used the **YouTube Trending Videos Dataset** available on Kaggle:

[YouTube Trending Dataset – Kaggle](https://www.kaggle.com/datasets/datasnaek/youtube-new)

---

##  Key Implementation Steps

1. **Data Preparation**  
   - Downloaded YouTube trending CSVs from Kaggle and uploaded them to S3 (`youtube/raw_statistics/`).

2. **Glue Crawler**  
   - Configured a Glue Crawler to catalog the raw data from S3 for querying with Athena.

3. **AWS Lambda**  
   - Used Lambda to clean data and ETL Job triggers.

4. **Glue ETL Job**  
   - Created a PySpark Glue Job to read raw data, filter by region (`us`, `gb`, `ca`), clean it, and write Parquet files partitioned by `region` to S3.

5. **Athena Querying**  
   - Queried transformed data using SQL in Athena to validate and explore insights.

6. **QuickSight Dashboard**  
   - Built visualizations showing top videos, category performance, and engagement trends.


## 🖼️ Screenshots

- Glue Script Run

![aws_glue_script_successful](https://github.com/user-attachments/assets/0c330dda-720a-4585-8e92-2fdeb2882fca)

- Lambda Function 

![lambda_functions](https://github.com/user-attachments/assets/8c127c63-2117-419f-a368-c1f04def37cb)
  
- Lambda Trigger Run

![lambda_trigger](https://github.com/user-attachments/assets/6bdbecc1-c793-4ece-85d9-cae5759e2607)

- Amazon S3 Partitioned Data

![partitioned_data](https://github.com/user-attachments/assets/c43d21b2-076f-4ff2-919f-a14e17d61906)

- Athena Queries
![athena_queries](https://github.com/user-attachments/assets/2e0356ce-50b9-4b31-be71-014c3d62625c)

---
