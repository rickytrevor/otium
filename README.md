# Otium

## License
this software is released under the gnu gplv3 license and it's ment only for educational use, i won't provide any free hosting, if you have any suggestions/fixes or simply you find some optimizations to my code feel free to start a pull request

## Howto: deploy it 
## there are two ways to deploy this bot, via docker or via the bot.py file
### Docker
To deploy the bot with docker you have to first build the docker image with 

#### docker build -t bot . 
Then, you can run it with 
#### docker run -t -d -v /your/songs/cache/directory:/songs bot 

### non-docker method 
To deploy it without docker you first need to install all the dependencies with pip install -U discord.py pynacl python-dotenv youtube-dl  youtube-search-python && sudo apt install ffmpeg youtube-dl 
and then to actually run the program just run python3 bot.py 


## credits
Library: https://github.com/Rapptz/discord.py
early contributors: https://github.com/ThatsMassy

## What is the bot capable of doing?
this example is capable of: playing songs (also it should be able to play in more than one server at once), pausing, resuming and skipping 

## Commands
#### .play song
#### .stop
#### .resume
#### .skip

## Howto: Contribute
The source code is ment to be edited in a docker container using visual studio code with the remote-containers plugin, with that you can just open the project, tap "open in container" and vscode should install everything that it's needed to test and debug the bot


