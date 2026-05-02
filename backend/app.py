from flask import Flask, jsonify
import redis
import time

app = Flask(__name__)

# підключення до Redis (сервіс з docker-compose)
r = redis.Redis(host="redis", port=6379, decode_responses=True)

# час старту сервера (для uptime)
start_time = time.time()


# 🏠 ГОЛОВНА СТОРІНКА
@app.get("/")
def home():
    visits = r.incr("visits")  # кожен запит +1 в Redis
    return jsonify({
        "message": "🔥 DevOps Lab Backend is alive",
        "visits": visits
    })


# ❤️ СТАТУС СЕРВЕРА
@app.get("/status")
def status():
    return jsonify({
        "status": "alive",
        "redis": "connected"
    })


# 📊 СТАТИСТИКА
@app.get("/stats")
def stats():
    return jsonify({
        "visits": r.get("visits")
    })


# ⏱ UPTIME (скільки працює сервер)
@app.get("/uptime")
def uptime():
    return jsonify({
        "uptime_seconds": int(time.time() - start_time)
    })


# 🚀 запуск сервера
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
