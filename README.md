# 📊 Revenue Forecasting with Databricks

A complete end-to-end data engineering and machine learning project demonstrating revenue forecasting using Databricks, Delta Lake, and Facebook Prophet.

## 🎯 Project Overview

This project implements a production-ready revenue forecasting pipeline that:
- Ingests raw transaction data into a **Delta Lake Lakehouse**
- Processes data through **Bronze → Silver → Gold** layers
- Builds a **Prophet time-series ML model** for 30-day revenue forecasts
- Provides **SQL analytics** for business insights
- Tracks experiments with **MLflow**

## 🏗️ Architecture

```
Data Pipeline Architecture:
┌─────────────────────────────────────────────────────────────┐
│                   BRONZE LAYER (Raw)                        │
│  • Raw transaction CSV ingestion                            │
│  • Add metadata (timestamps, source)                        │
│  • Delta Lake storage with ACID transactions                │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                   SILVER LAYER (Cleaned)                    │
│  • Data quality checks & validation                         │
│  • Remove duplicates & nulls                                │
│  • Type conversions & standardization                       │
│  • Add business logic columns                               │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                   GOLD LAYER (Aggregated)                   │
│  • Daily revenue aggregations                               │
│  • Monthly revenue with MoM growth                          │
│  • Category & regional analytics                            │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                   ML FORECASTING                            │
│  • Prophet model with seasonality                           │
│  • 30-day revenue forecast                                  │
│  • MLflow experiment tracking                               │
│  • Confidence intervals (95%)                               │
└─────────────────────────────────────────────────────────────┘
```

## 📂 Project Structure

```
databricks-revenue-forecasting/
│
├── data/
│   └── generate_revenue_data.py    # Synthetic data generator (730 days)
│
├── notebooks/
│   ├── 01_bronze_ingestion.py      # Raw data ingestion
│   ├── 02_silver_transformation.py # Data cleaning & quality
│   ├── 03_gold_aggregation.py      # Analytics aggregations
│   ├── 04_ml_revenue_forecasting.py # ML model training & prediction
│   └── 05_sql_analytics.sql        # Business analytics queries
│
├── screenshots/                     # (Add your dashboard screenshots here)
│
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Git ignore rules
└── README.md                        # This file
```

## 🚀 Quick Start

### 1. Generate Sample Data

```bash
cd data
python generate_revenue_data.py
```

This creates `sample_transactions.csv` with 2 years of synthetic transaction data (~40,000 transactions).

### 2. Upload Data to Databricks

Upload `sample_transactions.csv` to Databricks:
- **Option A**: Use Databricks UI → Data → Upload File → `/FileStore/`
- **Option B**: Use Databricks CLI
  ```bash
  databricks fs cp sample_transactions.csv dbfs:/FileStore/
  ```

### 3. Run Notebooks in Order

Import all notebooks from the `notebooks/` folder into your Databricks workspace and run them sequentially:

1. **01_bronze_ingestion.py** - Loads CSV into Delta Lake Bronze layer
2. **02_silver_transformation.py** - Cleans and validates data
3. **03_gold_aggregation.py** - Creates daily/monthly aggregations
4. **04_ml_revenue_forecasting.py** - Trains Prophet model and generates forecast
5. **05_sql_analytics.sql** - Business analytics and insights

### 4. View Results

After running all notebooks, you'll have:
- **Delta Tables**: `main.bronze.transactions`, `main.silver.transactions_cleaned`, `main.gold.daily_revenue`, etc.
- **Forecast**: `main.gold.revenue_forecast_30d` with 30-day predictions
- **Metrics**: Model performance metrics (MAE, MAPE, RMSE)
- **MLflow Experiments**: Tracked at `/Users/mlflow/revenue_forecasting`

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Databricks** | Unified analytics platform |
| **Delta Lake** | ACID-compliant data storage |
| **PySpark** | Distributed data processing |
| **Prophet** | Time-series forecasting |
| **MLflow** | Experiment tracking & model registry |
| **Plotly** | Interactive visualizations |
| **SQL** | Business analytics queries |

## 📊 Key Features

### 1. **Medallion Architecture**
- **Bronze**: Raw data with full lineage
- **Silver**: Cleaned, validated, deduplicated data
- **Gold**: Business-level aggregations ready for analytics

### 2. **Time-Series Forecasting**
- Prophet model with automatic seasonality detection
- Weekly and yearly patterns captured
- 95% confidence intervals
- MAPE accuracy tracking

### 3. **Data Quality**
- Null handling and validation
- Duplicate removal
- Type conversions and standardization
- Business rule enforcement

### 4. **Analytics**
- Daily/monthly revenue trends
- Day-of-week patterns
- Product category performance
- Regional analysis
- Customer segmentation
- Year-over-year comparisons

## 📈 Sample Output

### Forecast Metrics
- **MAE** (Mean Absolute Error): ~$500
- **MAPE** (Mean Absolute % Error): ~3-5%
- **RMSE** (Root Mean Squared Error): ~$750

### Sample Forecast
| Date | Predicted Revenue | Lower Bound | Upper Bound |
|------|-------------------|-------------|-------------|
| 2025-01-01 | $15,234.50 | $14,200.00 | $16,300.00 |
| 2025-01-02 | $15,890.25 | $14,850.00 | $16,950.00 |
| ... | ... | ... | ... |

## 🔧 Configuration

### Update File Paths
If your data is in a different location, update the path in `01_bronze_ingestion.py`:
```python
input_file_path = "/your/custom/path/sample_transactions.csv"
```

### Adjust Forecast Period
To change the forecast horizon, modify in `04_ml_revenue_forecasting.py`:
```python
future_dates = pd.date_range(start=last_date + timedelta(days=1), periods=60, freq='D')  # 60 days
```

## 📚 Learning Resources

- [Databricks Documentation](https://docs.databricks.com/)
- [Delta Lake Guide](https://delta.io/)
- [Prophet Documentation](https://facebook.github.io/prophet/)
- [MLflow Documentation](https://mlflow.org/)

## 🎓 Use Cases

This project demonstrates skills in:
- ✅ **Data Engineering**: ETL pipelines, data quality, medallion architecture
- ✅ **Machine Learning**: Time-series forecasting, model evaluation
- ✅ **MLOps**: Experiment tracking, model versioning
- ✅ **SQL Analytics**: Business intelligence, KPI tracking
- ✅ **Databricks**: Workspace, notebooks, Delta Lake, SQL

## 🤝 Contributing

Feel free to fork this repo and customize for your own use cases:
- Add more sophisticated ML models (ARIMA, LSTM, etc.)
- Implement automated retraining pipelines
- Create Databricks dashboards
- Add alerting for forecast anomalies
- Integrate with external BI tools

## 📝 License

This project is open source and available for educational use.

## 👤 Author

**Sonam Jaiswal**

This project was created as a proof-of-concept to demonstrate Databricks capabilities for revenue forecasting in a production environment.

---

**⭐ If you find this useful, please star the repo!**
