# Use an official Maven runtime as a parent image
FROM maven:3.6.3-jdk-8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the pom.xml file to the working directory
COPY pom.xml .

# Run Maven to download dependencies
RUN mvn dependency:resolve

# Copy the rest of the project to the working directory
COPY . .

# Compile the project
RUN mvn compile

# Build the project
RUN mvn package

# Start the application when the container launches
CMD ["mvn", "test"]


