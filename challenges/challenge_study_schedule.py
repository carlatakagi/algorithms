def study_schedule(permanence_period, target_time):
    counter = 0
    for index in permanence_period:
        try:
            if target_time >= index[0] and target_time <= index[1]:
                counter += 1
        except TypeError:
            return None
    return counter
