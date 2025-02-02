import os
import mido
import time

def play_midi_file(midi_file, output_port):
    print(f"Playing {midi_file} on {output_port.name}")
    mid = mido.MidiFile(midi_file)
    start_time = time.time()
    for msg in mid.play():
        if not msg.is_meta:  # Send only non-meta messages
            output_port.send(msg)
    print(f"Finished {midi_file}")

def main():
    # List available MIDI output ports
    print("Available MIDI output ports:")
    for name in mido.get_output_names():
        print(name)

    # Replace with the name of your virtual port connected to Massive Standalone
    port_name = "IAC Driver Bus 1"

    try:
        with mido.open_output(port_name) as outport:
            midi_folder = "/Users/macbookair/Documents/mid/aestheticspls"
            if not os.path.isdir(midi_folder):
                print(f"Folder '{midi_folder}' does not exist.")
                return

            midi_files = [f for f in os.listdir(midi_folder)
                          if f.lower().endswith(('.mid', '.midi'))]
            if not midi_files:
                print("No MIDI files found in the folder.")
                return

            midi_files.sort()

            for midi_filename in midi_files:
                midi_path = os.path.join(midi_folder, midi_filename)
                play_midi_file(midi_path, outport)
                time.sleep(1)  # small pause between files

    except IOError as e:
        print(f"Could not open MIDI output port: {port_name}")
        print(f"Error details: {e}")

if __name__ == "__main__":
    main()