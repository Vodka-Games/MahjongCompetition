# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:latest

COPY . /api
RUN make /api
WORKDIR /api

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["uvicorn", "main:app", "--host", "0.0.0.0","--port","8000"]
