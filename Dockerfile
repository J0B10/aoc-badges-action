FROM python:3.8-alpine

RUN apk add build-base

RUN pip install mkdocs requests

ADD entrypoint.sh /entrypoint.sh
ADD aoc-badges.py /aoc-badges.py

RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]