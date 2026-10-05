#!/usr/bin/env bash
cd "$(dirname "$0")"

# workspace 상위의 .venv 가상환경이 있으면 활성화
if [ -d "../.venv" ]; then
    source ../.venv/bin/activate
elif [ -d ".venv" ]; then
    source .venv/bin/activate
fi

streamlit run app.py
