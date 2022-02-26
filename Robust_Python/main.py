import datetime
import random


def find_workers_available_for_time(open_time: datetime.datetime):
    workers = worker_database.get_all_workers()
    available_workers = [worker for worker in workers if is_available(worker)]
    if available_workers:
        return available_workers
    # fall back to workers who listed they are available
    # in an emergency
    open_time.
    emergency_workers = [worker for worker in get_emergency_workers() if is_available(worker)]
    if emergency_workers:
        return emergency_workers
    # Schedule the owner to open, they will find someone else
    return [OWNER]
