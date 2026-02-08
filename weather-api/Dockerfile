#Stage 1:Builder
FROM python:3.9-slim as builder
WorkDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

#stage 2:Runtime
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY app.py .
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "app.py"]