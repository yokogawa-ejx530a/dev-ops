from fastapi import FastAPI
import psutil
import time

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the System Monitor API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/cpu")
def get_cpu():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "cores": psutil.cpu_count(logical=True)
    }

@app.get("/memory")
def get_memory():
    mem = psutil.virtual_memory()
    return {
        "total_bytes": mem.total,
        "available_bytes": mem.available,
        "percent_used": mem.percent
    }

@app.get("/disk")
def get_disk():
    disk = psutil.disk_usage('/')
    return {
        "total_bytes": disk.total,
        "free_bytes": disk.free,
        "percent_used": disk.percent
    }

@app.get("/uptime")
def get_uptime():
    boot_time = psutil.boot_time()
    current_time = time.time()
    uptime_seconds = current_time - boot_time
    return {"uptime_seconds": int(uptime_seconds)}