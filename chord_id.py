# Program to analyze given notes

c_nat = ['B#', 'C', 'Dbb']
c_sh = ['B##', 'C#', 'Db']
d_nat = ['C##', 'D', 'Ebb']
d_sh = ['D#', 'Eb', 'Fbb']
e_nat = ['D##', 'E', 'Fb']
f_nat = ['E#', 'F', 'Gbb']
f_sh = ['E##', 'F#', 'Gb']
g_nat = ['F##', 'G', 'Abb']
g_sh = ['G#', 'Ab']
a_nat = ['G##', 'A', 'Bbb']
a_sh = ['A#', 'Bb', 'Cbb']
b_nat = ['A##', 'B', 'Cb']

notelist = [
    c_nat, c_sh, d_nat, d_sh, e_nat, f_nat,
    f_sh, g_nat, g_sh, a_nat, a_sh, b_nat
]

chordlist = [
    ['Unison','Octave',], ['Minor Second', 'Major Seventh'],
    ['Major Second', 'Minor Seventh'], ['Minor Third', 'Major Sixth'],
    ['Major Third', 'Minor Sixth'], ['Perfect Fourth', 'Perfect Fifth'],
    ['Augmented Fourth', 'Diminished Fifth']
]

int_groups = {
    3 : 'm',
    4 : 'M',
    5 : 'sus4',
    1 : 'b9',
    2 : '9',
    10 : '7',
    11 : 'M7',
    6 : '+4',
    8 : 'addb6',
    9 : 'add6'
}

spec_int_groups = [] # Will be filled with unique names

def interval2quality(root, intervals):
    """Takes list of intervals (measured in semitones)
    and appends chord quality to root."""

    for ii in range(len(spec_int_groups)):
        pass

    for ii in int_groups:
        if ii in intervals:
            root = root + int_groups[ii]

    return root


def chord_type(args):
    '''Determines chord quality from given notes.
    If only two args given, returns the interval and its inversion.

    Make sure all notes are capitalized.
    Flates are "b" and Sharps are "#".
    '''

    if len(args) <= 1:
        print('Requires at least 2 notes')

    elif len(args) == 2:
        for ii in range(len(notelist)):
            if args[0] in notelist[ii]:
                for jj in range(len(notelist)):
                    if args[1] in notelist[jj]:
                        notedist = abs(ii - jj)
                        if abs(ii - jj) > 6:
                            notedist = 12 - notedist
        return '{} or {}'.format(chordlist[notedist][0], chordlist[notedist][1])

    else:
        pitchclass = {}
        for ii in range(len(args)):
            for jj in range(len(notelist)):
                if args[ii] in notelist[jj]:
                    pitchclass[jj] = args[ii]
        pitchclasslist = []
        for key in pitchclass:
            pitchclasslist.append(key)
        pitchclasslist.sort()

        intervals = []
        for n in range(len(pitchclasslist) - 1):
            intervals.append(pitchclasslist[n + 1] - pitchclasslist[0])
            if intervals[-1] < 0:
                intervals[-1] = intervals[-1] % 12

        chordname = interval2quality(pitchclass[pitchclasslist[0]], intervals)
        return chordname
