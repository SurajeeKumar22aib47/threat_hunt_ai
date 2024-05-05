# myapp/management/commands/monitor_events.py

import os
import csv
import time
import win32evtlog
import pandas as pd
from joblib import load
import matplotlib.pyplot as plt
from django.core.management.base import BaseCommand
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Monitors event logs and makes predictions'

    def handle(self, *args, **kwargs):
        log_directory = settings.LOG_DIRECTORY
        event_types = settings.EVENT_TYPES
        model_path = settings.ISOLATION_FOREST_MODEL_PATH
        loaded_model = load(model_path)

        while True:
            for event_type, log_type in event_types.items():
                current_time = time.strftime("%Y%m%d%H%M%S")
                filename = os.path.join(log_directory, f"{event_type}_EventLogs_{current_time}.csv")

                events = self.retrieve_event_logs(log_type)
                self.save_to_csv(events, filename, event_type)
                logger.info(f"{event_type} event logs saved to: {filename}")

                new_data = pd.read_csv(filename)
                new_data_numeric = new_data['Record Number'].astype(float)
                predictions = loaded_model.predict(new_data_numeric.values.reshape(-1, 1))
                predictions = ['threat' if x == -1 else 'non-threat' for x in predictions]

                threat_count = predictions.count('threat')
                non_threat_count = predictions.count('non-threat')

                logger.info(f"Threat Count: {threat_count}")
                logger.info(f"Non-Threat Count: {non_threat_count}")

                for i, prediction in enumerate(predictions):
                    if prediction == 'threat':
                        logger.warning(f"Threat identified at {new_data['Time Generated'][i]} from source {new_data['Source Name'][i]}")

                plt.figure(figsize=(8, 6))
                plt.bar(["Threat", "Non-Threat"], [threat_count, non_threat_count], color=['red', 'green'])
                plt.title("Predictions Distribution")
                plt.xlabel("Prediction")
                plt.ylabel("Count")
                plt.show()

            time.sleep(300)

    def retrieve_event_logs(log_type):
    computer = None  # None means local computer
    hand = win32evtlog.OpenEventLog(computer, log_type)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

    events = []
    while True:
        events = win32evtlog.ReadEventLog(hand, flags, 0)
        if not events:
            break
        for event in events:
            yield event

    win32evtlog.CloseEventLog(hand)

    def save_to_csv(events, filename, event_type):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Record Number', 'Event Category', 'Time Generated', 'Source Name', 'Event ID', 'Event Type', 'Event Strings'])

        for event in events:
            record_number = event.RecordNumber
            event_category = event.EventCategory
            time_generated = event.TimeGenerated.Format()
            source_name = event.SourceName
            event_id = event.EventID
            event_type_column = event_type
            event_strings = event.StringInserts

            writer.writerow([record_number, event_category, time_generated, source_name, event_id, event_type_column, event_strings])
