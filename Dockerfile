# use the AWS base image for Python 3.12
FROM public.ecr.aws/lambda/python:3.12

#install build-essential compiler and tools
RUN microdnf update -y && microdnf install -y gcc-c++ make

# copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# install packages
RUN pip install -r requirements.txt

# copy function code
COPY travelAgent.py ${LAMBDA_TASK_ROOT}

# set permissions to make file executable
RUN chmod +x travelAgent.py

# set CMD to yout handler
CMD ["travelAgent.lambda_handler"]