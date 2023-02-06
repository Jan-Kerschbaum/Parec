FROM elasticsearch:8.6.1

WORKDIR /data

COPY ./data /data
#copy init script

# run init script
# which creates data.yml
RUN init_data.py

# copy data to es data path
COPY ./data.yml usr/share/elasticsearch/config