import ntplib
from time import ctime


def atomic_time():
    ntp_server = 'pool.ntp.org'
    ntp_client = ntplib.NTPClient()

    try:
        response = ntp_client.request(ntp_server)
        atomic_time = ctime(response.tx_time)
        return atomic_time
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("The atomic time is: ", atomic_time())
