def extract_input(entries, matrix):
    for i, row_entries in enumerate(entries):
        for j, entry in enumerate(row_entries):
            entry_value = entry.get()
            if entry_value:
                matrix[i][j] = float(entry_value)
            else:
                matrix[i][j] = 0.0


def extract_criteria_input(criteria_entries_list, criteria_entries):
    print(criteria_entries)
    for entry in criteria_entries:
        print(entry)
        entry_value = entry.get()
        criteria_entries_list.append(entry_value)
    print(criteria_entries_list)
