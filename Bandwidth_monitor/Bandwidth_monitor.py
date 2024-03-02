import psutil
import time
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def monitor_bandwidth(duration):
    start = datetime.now()
    end = start + timedelta(minutes=duration)

    timestamps = []
    upload_data = []
    download_data = []

    while datetime.now() < end:
        net_stats = psutil.net_io_counters()
        timestamps.append(datetime.now())
        upload_data.append(net_stats.bytes_sent)
        download_data.append(net_stats.bytes_recv)
        time_remaining = end - datetime.now()
        formatted_time = format_time_remaining(time_remaining)
        print(f"Time remaining: {formatted_time}\r")
        time.sleep(1)

    return timestamps, upload_data, download_data


def format_time_remaining(time_remaining):
    hours, remainder = divmod(time_remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"


def generate_report(timestamps, upload_data, download_data):
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, upload_data, label="Upload")
    plt.plot(timestamps, download_data, label="Download")
    plt.title("Network Usage over time")
    plt.xlabel("Time")
    plt.ylabel("Bytes")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    duration_time = int(input("Enter the duration time: "))
    timestamps, upload_data, download_data = monitor_bandwidth(duration_time)
    generate_report(timestamps, upload_data, download_data)
