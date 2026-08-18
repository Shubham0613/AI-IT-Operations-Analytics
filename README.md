\# AI-IT Operations Analytics \& Incident Intelligence Platform
🌐 Live Demo: https://ai-it-operations-analytics.streamlit.app


An end-to-end IT operations analytics solution combining \*\*MySQL, SQL, Excel, Python/Pandas, AI-assisted incident prioritization, Power BI, and Streamlit\*\* to analyze IT incidents, monitor SLA performance, and support operational decision-making.



> \*\*Important:\*\* The project uses AI-assisted scoring/prioritization terminology. No claim of a trained and evaluated machine-learning model is made.



\---



\## 📌 Project Overview



IT support teams handle large volumes of incidents across departments, locations, issue types, priorities, and service channels.



This project transforms a 1,500-ticket IT incident dataset into an interactive analytics and incident intelligence platform.



The solution provides:



\* IT incident analytics

\* SLA performance monitoring

\* Service quality analysis

\* AI-assisted priority scoring

\* AI confidence analysis

\* Incident exploration

\* Interactive filtering

\* Executive KPI reporting

\* Power BI dashboard

\* Streamlit web application



\### Core Recruiter Message



\*\*This is an end-to-end IT operations analytics solution, not merely a Power BI dashboard.\*\*



\---



\## 🎯 Business Problem



IT operations teams need visibility into:



\* Which incidents require urgent attention?

\* Which issue types generate the highest ticket volume?

\* Which locations experience the most incidents?

\* Where are SLA breaches occurring?

\* How are incidents distributed across priorities?

\* How confident is the AI-assisted prioritization?

\* Which incidents may require escalation?



This project addresses these questions through centralized data analysis and interactive dashboards.



\---



\## 🎯 Objectives



1\. Analyze IT incident data using SQL and Excel.

2\. Clean and structure incident data for analytics.

3\. Calculate operational KPIs.

4\. Analyze SLA performance and breaches.

5\. Implement AI-assisted incident scoring and prioritization.

6\. Visualize operational insights using Power BI.

7\. Build a genuinely interactive Streamlit application.

8\. Provide an Incident Explorer for operational investigation.

9\. Prepare the solution for GitHub and cloud deployment.



\---



\## 📊 Dataset



The project uses an IT incident dataset containing:



\*\*1,500 records\*\*



The primary analytical dataset is:



`Cleaned\_Data`



The Python application uses:



`data/cleaned\_data.csv`



\### Key Data Fields



\* Ticket\_ID

\* Ticket\_Date

\* Department

\* Issue\_Type

\* Channel

\* Location

\* Priority

\* Status

\* Agent

\* Resolution\_Hours

\* SLA\_Hours

\* SLA\_Breach

\* Root\_Cause

\* Business\_Impact

\* Users\_Affected

\* CSAT

\* AI\_Priority\_Score

\* AI\_Predicted\_Priority

\* AI\_Confidence



\---



\## 🏗️ Project Architecture



```text

IT Incident Dataset

&#x20;       |

&#x20;     MySQL

&#x20;       |

&#x20;      SQL

&#x20;       |

&#x20;  Excel / Python

&#x20;       |

&#x20;  Pandas Analytics

&#x20;       |

AI-assisted Scoring

&#x20;       |

&#x20;  +----+----+

&#x20;  |         |

Power BI  Streamlit

&#x20;  |         |

&#x20;  +----+----+

&#x20;       |

&#x20;     GitHub

&#x20;       |

&#x20;Streamlit Cloud

&#x20;       |

&#x20;  LIVE DEMO

```



\---



\## 🗄️ MySQL / SQL Analysis



\### Database



`ai\_it\_operations`



\### Table



`tickets`



\### Records



`1,500`



SQL analysis is stored in:



`sql/AI\_IT\_Operations\_Analysis.sql`



The SQL layer supports operational analysis and KPI generation before visualization.



\---



\## 📗 Excel Analysis



The Excel workbook is:



`excel/AI\_IT\_Operations\_Analytics.xlsx`



\### Workbook Sheets



\* Cleaned\_Data

\* Raw\_Data\_Schema

\* KPI\_Summary

\* Issue\_Analysis

\* Location\_Analysis

\* README

\* Dashboard



Excel was used for structured data preparation, analysis, KPI summaries, and supporting operational insights.



\---



\## 🐍 Python / Pandas



Python is used to load and analyze the cleaned incident dataset.



The Streamlit application reads:



`data/cleaned\_data.csv`



The application uses:



\* Pandas

\* NumPy

\* Plotly

\* Streamlit



Python provides the interactive application layer on top of the existing analytics project.



\---



\## 🤖 AI-Assisted Prioritization



The dataset contains:



\* `AI\_Priority\_Score`

\* `AI\_Predicted\_Priority`

\* `AI\_Confidence`



\### AI Predicted Priority Distribution



| Priority | Tickets |

| -------- | ------: |

| Critical |     347 |

| High     |     447 |

| Medium   |     505 |

| Low      |     201 |



The project uses the terminology \*\*AI-assisted prioritization/scoring\*\* because a separately trained and evaluated machine-learning model is not claimed.



\---



\## 📊 Power BI Dashboard



\### Dashboard Title



\*\*AI-IT OPERATIONS ANALYTICS\*\*



\### Subtitle



\*\*AI-assisted IT incident prioritization | SLA performance | Service quality | Operational insights\*\*



\### Key KPIs



| KPI                     |  Value |

| ----------------------- | -----: |

| Total Tickets           |  1,500 |

| Resolved Tickets        |    977 |

| SLA Compliance          | 91.80% |

| Avg CSAT                |   4.11 |

| SLA Breaches            |    123 |

| Avg Resolution Hours    |   7.13 |

| AI Critical Predictions |    347 |

| High Critical Tickets   |    575 |



\### Power BI Visuals



\* AI Predicted Priority Distribution

\* Ticket Status Distribution

\* Tickets by Location

\* Tickets by Issue Type

\* AI Prediction Alignment

\* SLA Breaches by Priority

\* AI Confidence Distribution



\---



\## 🌐 Public Power BI Dashboard



The Power BI report has been published publicly and verified without login.



\*\*Public Dashboard:\*\*



https://app.powerbi.com/view?r=eyJrIjoiYjFhNjliNmUtZTI0Ni00Y2UxLWJjOTctNjdjMzQyYjQwN2UwIiwidCI6Ijg3MGY4ZTE2LTllMWQtNDNjNi1hZGUwLWMxMDY1ODAxYTc2MiJ9



\---



\## 🚀 Streamlit Application



The Streamlit application is an interactive web-based extension of the Power BI analytics solution.



\### Current Application Features



\* Executive Overview

\* KPI cards

\* Department filters

\* Issue Type filters

\* Location filters

\* Priority filters

\* Status filters

\* Ticket Status Distribution

\* AI Predicted Priority Distribution

\* Tickets by Issue Type

\* Tickets by Location

\* SLA Breach Analysis

\* AI Confidence Distribution

\* AI / Operations Insights

\* Incident Explorer

\* Ticket search



The application uses the same 1,500-ticket dataset as the analytics pipeline.



\---



\## 🔎 Incident Explorer



The Incident Explorer allows users to search incidents by:



\* Ticket ID

\* Issue Type

\* Agent

\* Root Cause



The explorer exposes operational fields including:



\* Priority

\* Status

\* Resolution Hours

\* SLA Hours

\* SLA Breach

\* CSAT

\* Business Impact

\* Users Affected

\* AI Priority Score

\* AI Predicted Priority

\* AI Confidence



\---



\## 📈 Key Insights



\### Ticket Status



\* Resolved: 738

\* Escalated: 278

\* In Progress: 245

\* Closed: 239



\### Location Distribution



\* Mumbai: 234

\* Bengaluru: 228

\* Indore: 220

\* Pune: 219

\* Gurugram: 207

\* Delhi: 205

\* Bhopal: 187



\### Issue Type Distribution



\* VPN Access: 171

\* Application Error: 165

\* Hardware Failure: 165

\* Security Alert: 159

\* Cloud Access: 146

\* Endpoint Performance: 145

\* Network Connectivity: 141

\* Password Reset: 141

\* Email Issue: 138

\* Wi-Fi Issue: 129



\### AI Confidence



\* 0–60%: 8

\* 60–70%: 226

\* 70–80%: 465

\* 80–90%: 343

\* 90–100%: 458



\### Additional Metrics



\* AI Prediction Alignment: 63.93%

\* High-priority SLA breaches: 83

\* Critical SLA breaches: 29

\* Medium SLA breaches: 11

\* Low SLA breaches: 0



\---



\## 🛠️ Technologies



\* MySQL

\* SQL

\* Microsoft Excel

\* Power Query

\* DAX

\* Power BI

\* Python

\* Pandas

\* NumPy

\* Plotly

\* Streamlit

\* Git

\* GitHub

\* Streamlit Cloud



\---



\## 📁 Project Structure



```text

AI\_IT\_Operations\_Project/

│

├── app/

│   └── app.py

│

├── data/

│   └── cleaned\_data.csv

│

├── sql/

│   └── AI\_IT\_Operations\_Analysis.sql

│

├── excel/

│   └── AI\_IT\_Operations\_Analytics.xlsx

│

├── powerbi/

│   └── AI\_IT\_Operations\_Analytics.pbix

│

├── screenshots/

│

├── requirements.txt

├── .gitignore

└── README.md

```



\---



\## ⚙️ Installation \& Run Instructions



\### 1. Clone the repository



```bash

git clone <repository-url>

cd AI\_IT\_Operations\_Project

```



\### 2. Create a virtual environment



```bash

python -m venv .venv

```



\### 3. Activate the environment



Windows:



```bash

.venv\\Scripts\\activate

```



\### 4. Install dependencies



```bash

pip install -r requirements.txt

```



\### 5. Run Streamlit



```bash

streamlit run app/app.py

```



The application will open locally at:



```text

http://localhost:8501

```



\---



\## 📸 Screenshots



Screenshots of the Power BI dashboard and Streamlit application will be stored in:



```text

screenshots/

```



\---



\## 🚀 Live Demo



The final deployment target is:



\*\*Streamlit Cloud\*\*



The live application URL will be added here after deployment.



\---



\## 🔮 Future Improvements



Potential future improvements include:



\* Training and evaluating a real machine-learning classification model

\* Automated incident risk prediction

\* Advanced SLA risk forecasting

\* Automated anomaly detection

\* Real-time incident ingestion

\* MySQL-to-Streamlit live connectivity

\* Role-based access

\* Automated operational alerts

\* Advanced incident recommendation engine

\* Cloud-hosted production architecture



\---



\## 👨‍💻 Project Positioning



This project demonstrates practical experience across:



\* SQL

\* MySQL

\* Excel

\* Power Query

\* DAX

\* Power BI

\* Python

\* Pandas

\* Interactive visualization

\* AI-assisted prioritization

\* SLA analytics

\* IT operations analytics

\* Dashboard development

\* Web application development

\* Git/GitHub

\* Cloud deployment



\### Final Portfolio Statement



> \*\*An end-to-end AI-assisted IT operations analytics and incident intelligence platform built to transform raw IT incident data into actionable operational insights.\*\*





