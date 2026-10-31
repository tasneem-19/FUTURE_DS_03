# 📊 Marketing Campaign Conversion Performance Dashboard

### Future Interns – Data Science & Analytics

### **Track Code:** DS

### **Task Number:** 03

### **Repository:** FUTURE_DS_03

---

## 👨‍💻 Author

**Khaisar Tasneem Shaik**  
Future Interns – Data Science & Analytics

---

## 📁 Project Overview

This project presents a **Marketing Campaign Conversion Performance Dashboard** built using **Power BI**.

It analyzes marketing campaign data to understand how effectively campaign contacts convert into customers who subscribe to a bank's term deposit. The analysis explores conversion rates and performance across different dimensions, including **job**, **age group**, **contact method**, **campaign outcome**, and **number of campaign contacts**.

The dashboard provides insights into customer response patterns, campaign performance, and potential opportunities to improve marketing effectiveness.

*Note: The selected dataset focuses on campaign contacts and subscription outcomes rather than website visitor-to-lead tracking.*

## 🖼 Dashboard Preview

[Marketing Campaign Conversion Dashboard](Dashboard_screenshot.jpg)

---

## 📂 Repository Structure

```text
FUTURE_DS_03/
│
├── Task 3 - PowerBI Dashboard.pbix    # Power BI dashboard file
│
├── Dashboard_screenshot.jpg           # Dashboard visual
│
├── analysis.py                        # Python data cleaning and analysis
│
├── cleaned_bank_marketing.csv         # Cleaned dataset used
│
└── README.md                          # Documentation
```

---

## 📊 Dashboard Highlights

### **Key Metrics**

- **Total Campaign Contacts:** 41,176
- **Successful Subscriptions:** 4,639
- **Unconverted Contacts:** 36,537
- **Overall Conversion Rate:** 11.27%

---

### **Conversion Performance Analysis**

- **By Contact Method:**
  - Cellular – 14.74%
  - Telephone – 5.23%

- **By Job:**
  - Student – 31.43%
  - Retired – 25.26%
  - Unemployed – 14.20%
  - Admin – 12.97%
  - Blue-collar – 6.90%

- **By Age Group:**
  - 17–25 – 20.96%
  - 26–35 – 11.72%
  - 36–45 – 8.51%
  - 46–55 – 8.69%
  - 56+ – 20.69%

---

### **Campaign Performance**

- **By Previous Campaign Outcome:**
  - Success – 65.11%
  - Failure – 14.23%
  - Nonexistent – 8.83%

- **By Number of Contacts:**
  - 1 Contact – 13.04%
  - 2 Contacts – 11.46%
  - 3 Contacts – 10.75%
  - 4 Contacts – 9.40%
  - 5 Contacts – 7.50%
  - 6+ Contacts – 5.49%

---

### **Monthly Conversion Analysis**

- March – 50.55%
- December – 48.90%
- September – 44.91%
- October – 43.93%
- May – 6.44%

Higher conversion rates were observed in March, December, September, and October. However, these months had different contact volumes, which should be considered when interpreting the results.

---

## 💡 Key Insights & Recommendations

### **Insights**

- The overall campaign conversion rate is 11.27%.
- Cellular contacts achieved a higher conversion rate than telephone contacts.
- Students and retired customers showed comparatively higher conversion rates.
- Customers with a successful previous campaign outcome had a conversion rate of 65.11%.
- Conversion rates generally decreased as the number of campaign contacts increased.
- March, December, September, and October recorded the highest monthly conversion rates.

### **Recommendations**

- Prioritize effective contact methods based on observed conversion performance.
- Study successful previous campaigns to identify strategies that can be reused.
- Focus on customer segments with stronger response rates.
- Review repeated contact strategies to improve campaign efficiency.
- Evaluate monthly performance alongside contact volumes before planning future campaigns.

---

## 🛠 Tools & Technologies Used

- **Python** – Data cleaning and exploratory data analysis
- **Pandas & NumPy** – Data manipulation and preprocessing
- **Matplotlib & Seaborn** – Data analysis and visualization
- **Power BI** – Interactive dashboard creation
- **DAX** – Calculated measures and KPIs
- **CSV** – Dataset storage and data handling

---

## 🔗 Dashboard Access

The dashboard has not been published to Power BI Service.

You can explore the full interactive dashboard using the Power BI file included in this repository:

**Task 3 - PowerBI Dashboard.pbix**

---

## 📝 Submission Notes

- Repository name follows the required format: **FUTURE_DS_03**
- Includes: PBIX file, cleaned dataset, Python analysis script, screenshot, and README
- Public repository for review and verification
