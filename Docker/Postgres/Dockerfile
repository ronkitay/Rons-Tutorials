FROM postgres:9.5

WORKDIR /docker-entrypoint-initdb.d

ADD all.sql /docker-entrypoint-initdb.d
# ADD 01_x_yy_z.sql /docker-entrypoint-initdb.d

# Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt

EXPOSE 5432

ENV NAME World