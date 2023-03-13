def marsExploration(full_sos_str):
    # Write your code here
    valid_sos = 'SOS'
    sos_slices = [full_sos_str[i : i + 3] for i in range(0, len(full_sos_str), 3)]

    count_decayed = 0
    for sos_slice in sos_slices:
        for i, letter in enumerate(valid_sos):
            if letter != sos_slice[i]:
                count_decayed += 1

    return count_decayed


assert marsExploration('SOSSPSSQSSOR') == 3
assert marsExploration('SOSSOT') == 1
