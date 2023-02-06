FROM elasticsearch:8.6.1

#WORKDIR /data

#COPY ./data /data
#copy init script

# run init script
# which creates data.yml
#RUN init_data.py

# copy data to es data path
COPY ./data/arxiv_reduced.json usr/share/elasticsearch/data/arxiv_reduced.json