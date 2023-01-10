FROM python:3.8
WORKDIR /book_store
COPY . .
RUN python3 -m pip install -r requirements.txt
EXPOSE 5000
CMD [ "python3", "main.py"]