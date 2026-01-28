# Gunakan Python Image yang kecil (Slim)
FROM python:3.12-slim

# Set direktori kerja
WORKDIR /app

# Copy file dependensi
COPY pyproject.toml uv.lock ./

# Install dependensi
RUN pip install uv && uv sync --frozen

# Copy seluruh kode
COPY . .

# Jalankan aplikasi
CMD ["uv", "run", "uvicorn", "01_foundation.day01_api:app", "--host", "0.0.0.0", "--port", "8000"]
