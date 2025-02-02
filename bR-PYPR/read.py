import mido

# Open the output port for the virtual MIDI bus
try:
    outport = mido.open_output("IAC Driver Bus 1")
except IOError:
    print("Could not open the MIDI output port. Check that the IAC Driver is enabled and the name is correct.")
    exit(1)

# Correct path to the MIDI loop file (using a raw string)
midi_loop_path = r"/Users/macbookair/Documents/drums/bbRzr EXPORT'D KIT/bR-K04-C5.mid"

try:
    # Load and parse the MIDI file
    midi_file = mido.MidiFile(midi_loop_path)
    print("Playing MIDI loop...")

    # Send each message to the output port
    for msg in midi_file.play():
        outport.send(msg)

    print("MIDI loop finished.")
except Exception as e:
    print(f"Error playing MIDI loop: {e}")