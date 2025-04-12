import logging
import requests
import azure.functions as func

app = func.FunctionApp()

# Replace with your actual webhook URL
WEBHOOK_URL = "https://hooks.slack.com/services/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"

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False, use_monitor=False)
def timer_trigger(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')

    # Message payload
    message = {"text": "⏰ Azure Function executed successfully!"}

    # Send the message to the webhook
    try:
        response = requests.post(WEBHOOK_URL, json=message)
        response.raise_for_status()
        logging.info(f"Message sent to webhook. Response: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to send message to webhook: {e}")
