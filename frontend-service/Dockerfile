FROM python:3.9-slim
RUN pip install flask requests
COPY app.py .
EXPOSE 8080
CMD ["python", "app.py"]