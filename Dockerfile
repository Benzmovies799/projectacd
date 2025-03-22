FROM python:3.10

WORKDIR /Tgmofcl

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . . 

CMD ["python3", "bot.py"]
