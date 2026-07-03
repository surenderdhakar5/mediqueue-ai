def estimate_wait_time(
    queue_number: int,
    current_queue: int,
    average_minutes: int = 10
):

    waiting_people = max(
        queue_number - current_queue,
        0
    )

    return waiting_people * average_minutes