OS := $(shell uname -s 2>/dev/null || echo Windows)

.PHONY: install setup run clean

install:
ifeq ($(OS), Darwin)
	@echo "==> macOS: installing portaudio via Homebrew"
	brew install portaudio
else ifeq ($(OS), Linux)
	@echo "==> Linux: installing portaudio via apt"
	sudo apt-get update -qq && sudo apt-get install -y portaudio19-dev python3-dev
else
	@echo "==> Windows: installing portaudio via pipwin"
	pip install pipwin && pipwin install pyaudio
endif
ifeq ($(OS), Windows)
	pip install -r requirements.txt
else
	pip3 install -r requirements.txt
endif
	@echo "==> Done. Copy .env.example to .env and fill in your credentials."

setup: install
	@[ -f .env ] || cp .env.example .env
	@echo "==> Edit .env with your ELEVENLABS_API_KEY and ELEVENLABS_AGENT_ID"

tools:
	python3 setup_tools.py

run:
	python3 main.py

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null; true
