from listener import MidiListener
from parser import parse_event
from actions import handle_action


def main():
    listener = MidiListener()

    for event in listener.listen():
        parsed = parse_event(event)

        if parsed:
            handle_action(parsed)


if __name__ == "__main__":
    main()