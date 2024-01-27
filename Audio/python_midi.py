import rtmidi

midiin = rtmidi.MidiIn()

def print_message(midi):
    if midi.isNoteOn():
        print('ON: ', midi.getMidiNoteName(midi.getNoteNumber()), midi.getVelocity())
    elif midi.isNoteOff():
        print('OFF:', midi.getMidiNoteName(midi.getNoteNumber()))
    elif midi.isController():
        print('CONTROLLER', midi.getControllerNumber(), midi.getControllerValue())

ports = range(midiin.get_port_count())
if ports:
    for i in ports:
        print(midiin.get_port_name(i))
    print("Opening port 2!") 
    midiin.open_port(2) #set port here, currently hardcoded
    while True:
        m = midiin.get_message() # some timeout in ms
        if m:
            # print_message(m[0])
            print(m[0][1])
else:
    print('NO MIDI INPUT PORTS!')