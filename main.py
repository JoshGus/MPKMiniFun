from MIDIcontroller.listener import MidiListener
from MIDIcontroller.parser import parse_event
from MIDIcontroller.actions import handle_action

def main():

    listener = MidiListener()

    print("Starting MIDI event loop...\n")

    for event in listener.listen():

        # DEBUG: show raw event
        # print("RAW:", event)

        parsed = parse_event(event)

        # DEBUG: show parsed result
        if parsed:
            print("PARSED:", parsed)

            handle_action(parsed)
            
        else:
            print("RAW:", event)


if __name__ == "__main__":
    main()