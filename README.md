
# DLMDSEDE02 - Phase 2 Submission

## 📌 Project Title
**Quarterly Batch Processing Pipeline for Time-Series Stock Data**

## 📁 Project Structure

```
.
├── data/              # Raw data files (CSV)
├── delivery/          # FastAPI service to serve processed data
├── documentation/     # Diagrams, NiFi template XML
├── ingestion/         # Ingestion Docker/NiFi configurations
├── processed/         # Output of NiFi processing
├── storage/           # (Optional) Long-term file storage
├── docker-compose.yml # Compose file for services
├── README.md          # Project overview and usage
```

## 🔧 How to Use

1. **Put your CSV data** in the `data/` folder (e.g. `prices_v2.csv`)
2. **Start services**:
```bash
docker-compose up --build
```
3. **Access Apache NiFi**:
   - URL: [http://localhost:8080/nifi](http://localhost:8080/nifi)
4. **Import your template** from `documentation/Phase2_Ingestion.xml`
   - Start the processors
5. **Processed data** will appear in the `processed/` folder
6. **Delivery service** (FastAPI) will be running at:
   - [http://localhost:8000](http://localhost:8000)

## ✅ Features

- NiFi-based batch ingestion pipeline
- Containerized delivery microservice (FastAPI)
- Configured with Docker Compose
- Handles 1M+ time-series entries
- Secure, maintainable, and scalable

## 🧾 Notes

- Tested locally with Docker Desktop (WSL2)
- Data must include a `date` column
- Developed for IU’s DLMDSEDE02 course, Phase 2

---

📝 For full pipeline logic, see: `documentation/Phase2_Ingestion.xml`
## Phase 3 Summary

This repository now contains the final version of the batch-processing data architecture project, including:

- Fully functional Dockerized microservices
- Complete project documentation and reflection
- Data pipeline reproducible on any Docker-enabled system
- GitHub link document and architecture diagram

This project was submitted as part of the IU course DLMDSEDE02 (Data Engineering).

