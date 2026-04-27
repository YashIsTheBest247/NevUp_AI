from backend.services.queue import celery
from backend.services.analytics import compute_metrics

@celery.task
def process_trade_task(trade_id):
    compute_metrics(trade_id)