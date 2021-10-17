FROM fedora:latest
RUN dnf -y update
#RUN apt -y install python3-pip python3 ffmpeg wget youtube-dl
RUN dnf install -y python3-pip python3 ffmpeg wget youtube-dl aria2
#RUN wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
#RUN chmod a+rx /usr/local/bin/youtube-dl
RUN pip install -U discord.py pynacl python-dotenv youtube-search-python ydl
RUN ln -s /usr/bin/python3 /usr/bin/python
COPY . /data
CMD python3 /data/bot.py
