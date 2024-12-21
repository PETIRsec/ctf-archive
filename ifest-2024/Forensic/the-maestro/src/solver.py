import mido
import random

def bits_to_text(bits):
    chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
    return ''.join(chars)

def decode_message_from_midi_with_seed(midi_file, message_length, seed):
    mid = mido.MidiFile(midi_file)
    binary_message = ''
    
    random.seed(seed)

    note_on_messages = []
    for track in mid.tracks:
        for msg in track:
            if msg.type == 'note_on':
                note_on_messages.append(msg)

    random.shuffle(note_on_messages)

    for msg in note_on_messages:
        if len(binary_message) < message_length * 8:
            bit = msg.velocity & 1
            binary_message += str(bit)

    decoded_message = bits_to_text(binary_message)
    return decoded_message

def brute_force_decode(midi_file, message_length, max_seed=1337):
    for seed in range(max_seed):
        print(seed)
        decoded_message = decode_message_from_midi_with_seed(midi_file, message_length, seed)
        if "IFEST" in decoded_message:
            print(f"Valid message found with seed {seed}: {decoded_message}")
            return seed, decoded_message
    print("No valid message found within seed range.")
    return None, None

seed, message = brute_force_decode('maestro.mid', len('IFEST{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}'))