# 📊 Marketing Funnel & Conversion Performance Analysis
### Data Science & Analytics Internship Task 3 — Future Interns 2026

---

## 👤 Author
**Khethani Mugeri**  


---

## 📌 Project Overview

This project presents a full end-to-end marketing funnel and conversion
analysis for X Education, an online education platform. 

The goal is to answer real business questions such as:
- Where are users dropping off in the funnel?
- Which channels bring the highest quality leads?
- Which specializations convert best?
- How can conversion rates be improved?

---

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python 3.13 | Core analysis and visualisation |
| Pandas | Data loading, cleaning, and analysis |
| Matplotlib | Dashboard layout and chart creation |
| Anaconda / Spyder | Development environment |
| LaTeX (Overleaf) | Professional report writing |

---

## 📊 Dataset

**Leads Dataset — X Education**  
Source: [Kaggle — Leads Dataset](https://www.kaggle.com/datasets/ashydv/leads-dataset)

| Feature | Detail |
|---------|--------|
| Total Records | 9,240 leads |
| Total Visitors | 31,362 |
| Converted Customers | 3,561 |
| Conversion Rate | 38.54% |
| Drop-off Rate | 61.46% |
| Key Columns | Lead Source, Lead Origin, TotalVisits, Time Spent on Website, Specialization, Converted |

---

## 🔍 Analysis Performed

### ✅ Stage 1 — Data Loading & Preparation
- Loaded CSV using Pandas
- Fixed numeric columns (TotalVisits, Page Views)
- Cleaned Lead Source casing inconsistencies
- Engineered funnel stage flags

### ✅ Stage 2 — KPI Calculation
- Total visitors, leads, customers
- Traffic-to-lead rate
- Lead-to-customer conversion rate
- Overall funnel drop-off rate

### ✅ Stage 3 — Funnel Analysis
- Funnel overview (Visitors → Leads → Customers)
- Drop-off analysis by funnel stage
- Conversion rate by channel (lead source)
- Channel volume vs conversion quality
- Conversion rate by specialization
- Conversion trend by lead cohort

### ✅ Stage 4 — Dashboard & Visualisation
- 6 KPI cards across the top
- 6-panel professional dashboard
- Consistent blue theme
- Saved as high-resolution PDF

---

## 📈 Key Findings

| Area | Finding | Value |
|------|---------|-------|
| Traffic to Lead Rate | Most visitors never become leads | 29.46% |
| Lead Conversion Rate | Strong but improvable | 38.54% |
| Overall Funnel Rate | Only 1 in 9 visitors converts | 11.40% |
| Biggest Drop-off | Browse to convert stage | 43.10% |
| Best Channel | Welingak Website | 98.59% |
| Best Referral Channel | Reference (word of mouth) | 91.76% |
| Worst Channel | Olark Chat | 25.53% |
| Best Specialization | Healthcare Management | 49.69% |
| Cohort Warning | Recent cohort 12 decline | 31.00% |
| Lost Warm Leads | Unconverted leads in funnel | 5,679 |

---

## 💡 Business Recommendations

1. Scale Reference & Welingak Channels — Both convert above 90% but generate low volume
2. Fix Browse-to-Convert Drop-off — 43% of engaged browsers still don't convert
3. Target High-Converting Specializations — Healthcare & Banking convert above 49%
4. Improve Olark Chat Conversion — High volume (1,755 leads) but only 25.53% convert
5. Investigate Cohort 12 Decline — Conversion dropped to 31%, lowest of all cohorts
6. Re-engage 5,679 Unconverted Leads — Warm leads already in the funnel, no acquisition cost needed

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/khethanimugeri/FUTURE_DS_03.git
```

2. Install dependencies:
```bash
conda install pandas matplotlib numpy
```

3. Place `Leads.csv` in the project folder and update the path:
```python
df = pd.read_csv(r'C:\Anaconda3\Marketing Funnel\Leads.csv')
```

4. Run the analysis:
```bash
python Marketing Funnel Code.py
```

5. The dashboard will be saved as `Funnel_Dashboard.pdf` in the same folder

---

## 📜 License
This project was completed as part of the Future Interns Data Science
Internship Programme 2026.

---


