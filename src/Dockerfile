FROM python:3.10

LABEL name="megabox-open-push"

WORKDIR /

COPY * .

# discord bot token
ENV DISCORD_BOT_TOKEN=""

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["megabox_open_push_main.py"]

EXPOSE 5000