# Game of Live - MESA implementation

Dominik Kołodziej, Szymon Borowy


## Installation

### First way - Python

1. Open project directory
2. Install requirements (optional):
`pip install -r requirements.txt`
3. Run app:
`python game/main.py`
4. Open the browser on address: http://localhost:8521/


### Second way - Docker

1. Build an image:
`docker build --tag game-of-life-mesa .`
2. Run the image:
`docker run game-of-life-mesa -p 8521:8521`
3. Open the browser on address: http://localhost:8521/