import numpy as np
def extract_input(entries, matrix):
    for i, row_entries in enumerate(entries):
        for j, entry in enumerate(row_entries):
            entry_value = entry.get()
            if entry_value:
                entry_value = eval(entry_value)
                matrix[i][j] = float(entry_value)
            else:
                matrix[i][j] = 0.0


def extract_criteria_input(criteria_entries_list, criteria_entries):
    criteria_entries_list.clear()
    for entry in criteria_entries:
        entry_value = entry.get()
        criteria_entries_list.append(entry_value)
