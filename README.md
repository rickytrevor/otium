# Rick-Discord-bot

## License
this software is released under the gnu gplv3 license and it's ment only for educational use, i won't provide any free hosting, if you have any suggestions/fixes or simply you find some optimizations to my code feel free to start a pull request

## Howto: edit the source code
The source code is ment to be edited in a docker container using visual studio code with the remote-containers plugin, with that you can just open the project, tap "open in container" and vscode should install everything that it's needed to test and debug the bot
## Howto: deploy it 
You can deply it just by running python3 bot.py or via docker, first you have to build the image by going inside the source directory and running 

docker build -t bot . 


Then, you can run it with 


docker run -t -d -v /your/songs/cache/directory:/songs bot 

## credits
Library: https://github.com/Rapptz/discord.py
early contributors: https://github.com/ThatsMassy

## What is the bot capable of doing?
this example is capable of: playing songs (also it should be able to play in more than one server at once), pausing, resuming and skipping 
