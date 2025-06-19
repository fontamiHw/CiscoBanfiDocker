# Use the official lightweight Python image
FROM python:3.12-slim
#install all python libraries
RUN pip install matplotlib
#set the working directory
WORKDIR /app
#copy our application
COPY run.sh /app/run.sh
RUN chmod 744 /app/run.sh
#start the bot application
CMD ["/app/run.sh"]
