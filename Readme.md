

## Setup Instructions

### 1. Clone Repository

```bash
git clone <repo-url>
cd django
```

---

### 2. Create Virtual Environment

#### Windows

```powershell
python -m venv .denv
.denv\Scripts\activate
```

#### macOS / Linux

```bash
python -m venv .denv
source .denv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Environment Variables

Create `.env` from the example:

```bash
cp .env.example .env
```

Edit values as needed.

Example:

```env
DEBUG=True
SECRET_KEY=replace-this-secret-key
ALLOWED_HOSTS=127.0.0.1,localhost,192.168.1.45
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://192.168.1.50:3000
```

---

### 5. Run Migrations

```bash
python manage.py migrate
```

---

### 6. Start Development Server (LAN Enabled)

```bash
python manage.py runserver 0.0.0.0:8888
```

Access locally:

```
http://127.0.0.1:8888
```

Access from same Wi-Fi:

```
http://<your-local-ip>:8888
```

---
