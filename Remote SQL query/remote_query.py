import pymysql
import paramiko


def execute_remote_query(host, username, password, database, query):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)

    tunnel = paramiko.Transport((host, 22))
    tunnel.connect(username=username, password=password)
    tunnel.set_keepalive(60)
    tunnel_auth = ("localhost", 3306)
    ssh_channel = tunnel.open_channel('direct-tcpip', tunnel_auth, (host, 3306))

    connection = pymysql.connect(host="127.0.0.1", port=ssh_channel.local_address[1], user=username, password=password,
                                 database=database)

    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
    finally:
        connection.close()
        ssh_channel.close()
        tunnel.close()
        ssh.close()
    return result


if __name__ == "__main__":
    remote_host = ''
    remote_user = ''
    remote_password = ''
    remote_database = ''
    sql_query = ''

    result_set = execute_remote_query(remote_host, remote_user, remote_password, remote_database, sql_query)

    for row in result_set:
        print(row)
