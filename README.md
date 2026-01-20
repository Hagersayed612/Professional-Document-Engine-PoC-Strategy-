# Professional Document Engine (PoC)

A **Proof of Concept (PoC)** for a professional document generation platform that transforms structured user input into high-quality business documents (HTML preview & PDF).

This project was built as part of a technical assessment to demonstrate **engineering judgment, clean architecture, and product thinking**, not as a production-ready system.

---

## 🎯 Objective

The goal of this PoC is to demonstrate a **vertical slice** of functionality:

* A clean user interface for structured data entry
* A document engine that maps user input into a professional layout
* A high-fidelity output (HTML & PDF)
* A clear architectural path for scaling into a full product

---

## ✨ Features

* 📄 Professional business document layout (A4, margins, typography)
* 🧾 Dynamic content sections (add / remove sections)
* 👁️ Live HTML preview before export
* 📥 PDF generation from the same template
* 🧠 Single data model powering both preview & PDF
* 🧱 Clean separation between UI, logic, and templates

---

## 🧩 Tech Stack

### Backend

* **Python 3.10+**
* **FastAPI** – lightweight, high-performance API framework
* **Jinja2** – server-side HTML templating
* **xhtml2pdf** – HTML to PDF rendering

### Frontend

* **HTML5 / CSS3**
* **Vanilla JavaScript** (no framework, intentional for simplicity)

---

## 🏗️ Architecture Overview

```
User Input (HTML Form)
        ↓
FastAPI Routes
        ↓
Document Engine (Python Helpers)
        ↓
Jinja2 Templates (HTML)
        ↓
Preview (HTML)  |  PDF Export
```

* The **document engine** is independent of the output format
* HTML is the source for both preview and PDF generation
* No state is stored on the server (stateless design)

---

## 📁 Project Structure

```
project-root/
│
├── main.py                 # FastAPI application
├── templates/
│   ├── index.html          # User input interface
│   └── report.html         # Professional document template
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/professional-document-engine.git
cd professional-document-engine
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
uvicorn main:app --reload
```

### 5. Open in browser

```
http://127.0.0.1:8000
```

---

## 🧠 Key Design Decisions

### Why FastAPI?

* High performance
* Clean and readable code
* Async-ready for future scalability

### Why HTML → PDF?

* Full control over layout and typography
* Same template used for preview and export
* Easier iteration during product development

### Why Vanilla JS?

* Keeps the PoC simple and focused
* No unnecessary framework complexity

---

## 📈 Scalability (Future Roadmap)

This PoC is designed with scalability in mind:

* Background job processing for PDF generation (Celery / Redis)
* Stateless backend for horizontal scaling
* Queue-based workload management
* Template versioning system
* Docker & Kubernetes for auto-scaling

---

## 🧪 Limitations (PoC Scope)

* No authentication or user management
* No persistent storage
* No collaborative editing (planned)
* PDF generation is synchronous (acceptable for PoC)

These limitations are intentional and documented as part of the assessment.

---

## 🛣️ Next Steps (Sprint 2)

* Template management system
* Collaborative editing (WebSockets + CRDTs)
* Dynamic charts & data visualization
* Saved drafts & document history
* Production-ready PDF workers

---

## 📌 Disclaimer

This project is a **technical proof of concept**, built to demonstrate architecture, code quality, and strategic thinking. It is not intended to be a full commercial product in its current form.

---

## 👩‍💻 Author

**Hager Sayed**
Software Engineer

---

## 📄 License

This project is provided for evaluation and demonstration purposes only.
