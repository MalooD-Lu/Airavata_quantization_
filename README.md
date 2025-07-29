# Airavata Quantization

This project demonstrates how to **load**, **quantize**, and **serve** the [Ai4Bharat/Airavata](https://huggingface.co/ai4bharat/Airavata) Hindi LLM using FastAPI. It also includes a benchmark to evaluate the model’s latency and throughput using the deployed API.

---

## 📌 Features

- ✅ Load **base** and **4-bit quantized** versions of Airavata LLM
- ✅ Deploy using **FastAPI + Uvicorn + ngrok**
- ✅ Measure **latency** and **throughput** using `requests`
- ✅ Full support for **Google Colab + GPU**

---

## 📓 Google Colab Notebook

All the following were implemented in a **single Google Colab notebook**:

- ✅ Quantization using `bitsandbytes`
- ✅ FastAPI setup with working `/generate` endpoint
- ✅ ngrok tunneling for external access
- ✅ Latency and throughput benchmarking

> ⚠️ **Note**: Make sure to enable GPU via  
> `Runtime > Change runtime type > Hardware accelerator > GPU`.

---
## 📊 Benchmark Results

| Metric        | Base Model | Quantized Model (4-bit) |
|---------------|------------------------|---------------------------|
| **Latency**   | 2046.86 ms        | 2010 ms           |
| **Throughput**| 0.49 req/sec          | 0.50 req/sec             |
