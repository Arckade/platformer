import pygame
import pygame.midi
import time
import sys

# Initialize Pygame
pygame.init()

# Initialize the MIDI module
pygame.midi.init()

# Get the number of MIDI input devices
input_device_count = pygame.midi.get_count()

# Find the first MIDI input device (you may want to choose a specific device)
input_device_id = int(sys.argv[1])
print('midi', input_device_id)

# Open the MIDI input device
midi_input = pygame.midi.Input(input_device_id)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for MIDI input events
    if midi_input.poll():
        midi_events = midi_input.read(10)  # Read up to 10 MIDI events
        for midi_event in midi_events:
            [status, data1, data2, data3], tempo = midi_event
            print(format(status, 'b'), tempo)

            # Interpret MIDI events
            if status & 0xF0 == 0x90:  # Note On event
                print(f"Note On: Note={data1}, Velocity={data2}")
            elif status & 0xF0 == 0x80:  # Note Off event
                print(f"Note Off: Note={data1}, Velocity={data2}")
            elif status & 0xF0 == 0xB0:  # Control Change event
                print(f"Control Change: Control={data1}, Value={data2}")
            elif status & 0xF0 == 0xE0:  # Pitch Bend event
                pitch_bend = (data2 << 7) + data1
                print(f"Pitch Bend: Value={pitch_bend}")

    # Your game logic goes here

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Clean up
midi_input.close()
pygame.midi.quit()
pygame.quit()
