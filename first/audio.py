import pyaudio
import socket

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
SERVER_IP = "127.0.0.1"
PORT = 5004


def send_audio():
    p = pyaudio.PyAudio()
    stream = p.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
    )

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, PORT))
        while True:
            data = stream.read(CHUNK)
            s.sendall(data)


# if __name__ == '__main__':
#     send_audio()

send_audio()
