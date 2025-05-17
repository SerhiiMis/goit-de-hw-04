# 🧠 GoIT DE Homework 4 — Spark Jobs & SparkUI

## 📘 Task

This project is part of GoIT Data Engineering homework focused on exploring Spark job execution and SparkUI.

We run three PySpark scripts to observe how transformations and actions generate Spark jobs, with and without caching.

---

## 📂 Files

- `part1.py` — base version with filter and collect (5 jobs expected)
- `part2.py` — with intermediate `.collect()` (8 jobs expected)
- `part3.py` — using `.cache()` before repeated actions (7 jobs expected)
- `nuek-vuh3.csv` — input dataset

---

## 📸 Screenshots

Saved in the `screenshots/` folder as:

- `part1_jobs.png`
- `part2_jobs.png`
- `part3_jobs.png`

Each image shows the full job list from [http://localhost:4040/jobs](http://localhost:4040/jobs)

---

## ✅ Steps to Run

1. Activate virtual environment:

   ```bash
   source ~/pyspark-env/bin/activate

   ```

2. Run the desired part:

   ```bash
   python part1.py

   ```

3. View Spark UI:

   ```bash
   http://localhost:4040/jobs

   ```
