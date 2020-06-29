
def merge_ranges(in_list):
    in_list = sorted(in_list)
    list_len = len(in_list)
    i = 0
    while i < list_len:
        if in_list[i][1] >= in_list[i+1][0]:
            in_list[i] = (in_list[i][0], max(in_list[i][1], in_list[i+1][1]))
            del in_list[i+1]
            list_len -= 1
        i += 1
    return in_list


def merge_ranges_1(meetings):

    # Sort by start time
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end,
                                       current_meeting_end))
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings


print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))


