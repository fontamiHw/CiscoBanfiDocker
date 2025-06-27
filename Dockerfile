# Use the official lightweight Python image (this image has already python in it)
FROM python:3.12-slim 
#install all python libraries
RUN pip install matplotlib 
RUN pip install webexteamssdk webex_bot webexpythonsdk

#set the working directory
WORKDIR /app
# Define environment variable
ENV APP_ROOT_PATH="/app"
ENV APP_ROOT_HOST="${APP_ROOT_PATH}/host"
ENV APP_SOR_FILES="${APP_ROOT_HOST}/SOR"
ENV APP_JPG_FILES="${APP_ROOT_HOST}/JPG"

# Create a new directory under /app
RUN mkdir -p ${APP_ROOT_HOST}


#copy our application
COPY run.sh /app/run.sh
COPY app/*.py /app/.
RUN chmod 744 /app/run.sh
#start the bot application
CMD ["/app/run.sh"]
