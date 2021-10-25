import speedtest

def test_velocidad():
    print("Cargando lista de servidores... ")
    test = speedtest.Speedtest()
    test.get_servers()  # -> obtiene los mejores servidores de speedtest
    print("Buscando mejor servidor...")
    best_server = test.get_best_server()  # -> busca el mejor server
    # print(best_server)
    print(
        f"Found: {best_server['host']} encontrado en {best_server['country']}")

    download_result = test.download()
    print(f"Velocidad de descarga: {download_result /1024/1024:.2f} Mbit/s")
    upload_result = test.upload()
    print(f"Velocidad de subida: {upload_result /1024/1024:.2f} Mbit/s")
    ping_result = test.results.ping
    print(f"Ping {ping_result:.2f} ms")

test_velocidad()
