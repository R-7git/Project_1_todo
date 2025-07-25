FROM python:3.11-slim
RUN pip install django==5.2.4
COPY . .
RUN python manage.py migrate
EXPOSE 8009
CMD ["python", "manage.py", "runserver", "0.0.0.0:8009" ]