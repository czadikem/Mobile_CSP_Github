FROM debian:bullseye
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8
RUN apt-get update && apt install wget python3 python3-pip python3-venv -y
RUN echo "deb [arch=amd64,arm64,armhf] http://deb.volian.org/volian/ scar main" | tee /etc/apt/sources.list.d/volian-archive-scar-unstable.list && wget -qO - https://deb.volian.org/volian/scar.key | tee /etc/apt/trusted.gpg.d/volian-archive-scar-unstable.gpg > /dev/null && apt update && apt install nala-legacy -y
RUN nala update && nala upgrade -y
RUN nala install git curl -y
RUN useradd -m autiboy && echo "autiboy:@utb10yM@ut1!" | chpasswd && adduser autiboy sudo
WORKDIR /home/autiboy
COPY program-y.tar.gz ./
RUN tar -xf program-y.tar.gz && chown -R autiboy:autiboy /home/autiboy/program-y
COPY start-mauti.sh ./
RUN chmod +x /home/autiboy/start-mauti.sh && chown -R autiboy:autiboy /home/autiboy/start-mauti.sh
USER autiboy
RUN pip3 install python-dateutil wget beautifulsoup4 lxml PyYAML xmljson zeep fuzzywuzzy python-Levenshtein requests Flask Flask-SocketIO tweepy sleekxmpp python-telegram-bot pymessenger twilio slackclient viberbot line-bot-sdk kik discord.py botbuilder-core botbuilder-schema wikipedia MetOffer APScheduler emoji textblob redis pymango SQLAlchemy PyMySQL pymongo
RUN export PYTHONPATH=/home/autiboy/program-y/src && python3 -m programy.admin.tool install textblob
EXPOSE 8989
CMD ./start-mauti.sh
