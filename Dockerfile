# Use a lightweight Python Linux image
FROM python:3.9-slim

# Install the art library
RUN pip install Pillow

# Set up the workspace
WORKDIR /app

# Copy all your code into the container
COPY . .

# 1. Run the art generator
# 2. Create the folder structure
# 3. Zip it up
# We use a mini-script inside the command line here for simplicity
CMD python generate_assets.py && \
    mkdir -p eCHOMP_CosmicCrisp/assets && \
    cp -r assets/* eCHOMP_CosmicCrisp/assets/ && \
    cp content.json manifest.json config.json eCHOMP_CosmicCrisp/ && \
    python -m zipfile -c Release.zip eCHOMP_CosmicCrisp && \
    # Move the zip to the output mount
    cp Release.zip /output/eCHOMP_CosmicCrisp_Release.zip