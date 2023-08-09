import boto3
import time
from datetime import datetime

from .settings import settings


client = boto3.client(
    'logs',
    region_name=settings.AWS_REGION
)


def save(log_stream_name, log_message, log_group_name=f'/{settings.ENVIRONMENT}/api-logs') -> None:

    log_prefix = datetime.now().strftime('%Y/%m/%d')

    log_stream_name = f"{log_prefix}/{log_stream_name}"

    if settings.ENVIRONMENT == 'local':
        print("Push to log group:", log_group_name)
        print("Push to log stream:", log_stream_name)
        print("Push message:", log_message)
        _msg_check(log_message)
        return

    # Ensure log stream exists
    _create_log_stream(client, log_group_name, log_stream_name)

    # Put log event
    _put_log_event(client, log_group_name, log_stream_name, log_message)


def _create_log_group(client, log_group_name):
    response = client.create_log_group(
        logGroupName=log_group_name
    )
    return response


def _describe_log_stream(client, log_group_name, log_stream_name):
    response = client.describe_log_streams(
        logGroupName=log_group_name,
        logStreamNamePrefix=log_stream_name
    )
    return response


def _create_log_stream(client, log_group_name, log_stream_name):
    response = _describe_log_stream(client, log_group_name, log_stream_name)

    if 'logStreams' in response and len(response['logStreams']) > 0:
        # Log stream already exists
        print(f"Log stream '{log_stream_name}' already exists.")
    else:
        response = client.create_log_stream(
            logGroupName=log_group_name,
            logStreamName=log_stream_name
        )
        print(f"Log stream '{log_stream_name}' created.")


def _msg_check(message):
    if not isinstance(message, str):
        raise ValueError("Message should be a string")


def _put_log_event(client, log_group_name, log_stream_name, message):
    _msg_check(message)

    log_event = {
        'timestamp': int(time.time() * 1000),
        'message': message
    }

    response = client.put_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name,
        logEvents=[log_event]
    )
    return response
