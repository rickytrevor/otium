FROM debian:latest
RUN apt -y update
RUN apt -y install python3-pip python3 ffmpeg wget 
RUN apt -y install curl

RUN curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
RUN chmod a+rx /usr/local/bin/yt-dlp

#RUN dnf install -y python3-pip python3 ffmpeg wget youtube-dl aria2 yt-dlp
#RUN wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
#RUN chmod a+rx /usr/local/bin/youtube-dl
ENV token=${token}
RUN pip install -U discord.py pynacl python-dotenv youtube-search-python ydl
RUN ln -s /usr/bin/python3 /usr/bin/python
COPY . /data
CMD python3 /data/bot.py ${token}
