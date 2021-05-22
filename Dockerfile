FROM python:3.8.8

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' api-user

WORKDIR /opt/api

ARG PIP_EXTRA_INDEX_URL
ENV FLASK_APP app.py

# Install requirements, including from Gemfury
ADD ./packages/api /opt/api/
RUN pip install --upgrade pip
RUN pip install -r /opt/api/requirements.txt

RUN chmod +x /opt/api/run.sh
RUN chown -R api-user:api-user ./

USER api-user

EXPOSE 5000

CMD ["bash", "./run.sh"]