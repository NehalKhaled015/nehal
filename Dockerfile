# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and requirements file into the container
COPY python.py /app/
COPY paragraphs.txt /app/

# Install NLTK and download the stopwords corpus
RUN pip install --no-cache-dir nltk && \
    python -m nltk.downloader stopwords punkt

# Run the Python script when the container launches
CMD ["python", "python.py"]
