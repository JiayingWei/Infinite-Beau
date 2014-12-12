"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""

import pyaudio
import wave

def record(duration, filename, rate = 44100, channels = 2, aud_format = pyaudio.paInt16, _bytes = 1024):
    """ for channels, 1 is mono and 2 is stereo
    """
    p = pyaudio.PyAudio()
    frames = []

    stream = p.open(format = aud_format, channels=channels, rate=rate, input=True, frames_per_buffer=_bytes)

    for i in range(0, int(rate / _bytes * duration)):
        data = stream.read(_bytes)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(aud_format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()
    # return False


# record(5, "Audio/recordtest.wav")