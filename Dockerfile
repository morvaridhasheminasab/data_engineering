
# Base image (optional: python or data tools, here we'll use Ubuntu for example)
FROM ubuntu:20.04

# Set working directory
WORKDIR /app

# (Optional) Install needed tools or dependencies if scripted ingestion is added
RUN apt-get update && apt-get install -y curl unzip && apt-get clean

# Copy ingestion scripts if any (currently placeholder)
COPY . .

CMD ["bash"]
