# Base Image
FROM grpc/python

# Create dir for the server and copy all files
RUN mkdir /home/server
ADD . /home/server

# Working directory
WORKDIR /home/server

# Install pip
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py

# Install deps
RUN python3 -m pip install grpcio
RUN python3 -m pip install protobuf
RUN python3 -m pip install grpcio_tools

# Build proto
RUN python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. service.proto

# Expose port for the connection
EXPOSE "4300"

# Execute server
ENTRYPOINT ["python3","main.py"]