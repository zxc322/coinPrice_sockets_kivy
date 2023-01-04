# Runing manual

### Install dependencies from venv

    pip install -r req.txt

### For storing prices we are using redis. Run it local or use from `redis-docker` dir

    docker-compose -f docker-compose-redis.yml up --build

### To start websocket connection (using binance sockets) run

    python socket_runner.py

### To start kivy-interface app run (chose 1 option). They are completely the same

    1) python run_kivy_interface.py
    2) python kivy_with_kv\interface.py