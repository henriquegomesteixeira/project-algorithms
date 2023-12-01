def study_schedule(permanence_period, target_time):
    students_count = 0
    try:
        for min_hours, max_hours in permanence_period:
            if min_hours <= target_time <= max_hours:
                students_count += 1
        return students_count
    except TypeError:
        return None
