import music21
import numpy as np
import io
from scipy.io.wavfile import write as wav_write
from synthesizer import Synthesizer, Waveform

def note_to_frequencies(note_list):
    """Convert a list of music21 note objects to their corresponding frequencies."""
    frequencies = []
    for note_str in note_list:
        try:
            note = music21.note.Note(note_str)
            frequencies.append(note.pitch.frequency)
        except Exception as e:
            print(f"Error processing {note_str}: {e}")
            continue
    return frequencies



def generate_wav_bytes_from_notes_freq(notes_freq):
    synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    sample_rate = 44100

    audio = np.concatenate([
        synth.generate_constant_wave(frequency=freq, duration=0.5)
        for freq in notes_freq
    ])
    buffer = io.BytesIO()
    wav_write(buffer, sample_rate, audio.astype(np.float32))
    return buffer.getvalue()
