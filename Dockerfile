# Use the official lightweight Python image (this image has already python in it)
FROM python:3.12-slim 
#install all python libraries
RUN pip install matplotlib
RUN pip install webexteamssdk
RUN pip install webex_bot
#set the working directory
WORKDIR /app
#copy our application
COPY run.sh /app/run.sh
COPY app/*.py /app/.
RUN chmod 744 /app/run.sh
#start the bot application
CMD ["/app/run.sh"]
