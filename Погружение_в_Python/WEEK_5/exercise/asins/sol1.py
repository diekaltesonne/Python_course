while True:
    events = epoll.poll(1)
    for fileno, event in events:
        if event & select.EPOLLIN:
            data = conn_map[fileno].recv(1024)
            print(data.decode("utf8"))
        elif event & select.EPOLLOUT:
            conn_map[fileno].send("ping".encode("utf8"))
