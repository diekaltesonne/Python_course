## Как повторить у себя?
# Подготовка

Воспользуемся Vagrant (инструмент для создания и управления виртуальными машинами). Перед его установкой необходимо установить Virtualbox, так как Vagrant – это инструмент управления виртуальными машинами, а не система виртуализации. https://www.vagrantup.com/docs/virtualbox/

Затем необходимо установить Vagrant. https://www.vagrantup.com/downloads.html

После успешной установки нужно создать папку и в ней создать файл Vagrantfile. В Vagrantfile нужно скопировать:

```
$script = <<SCRIPT
    yum update
    yum -y install tcpdump nc telnet
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"

  config.vm.provision "shell", inline: $script
end
```
Затем выполнить внутри папки:
```
>>> vagrant up
>>> vagrant ssh
```
Поздравляю, Вы внутри виртуальной машины.
Если у вас windows, то немного сложнее: https://www.sitepoint.com/getting-started-vagrant-windows/

Теперь нужно узнать имя локального интерфейса
(это имя указывается после -i в утилите tcpdump). Для этого нужно выполнить:
```
>>> ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP qlen 1000
    link/ether 52:54:00:ca:e4:8b brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic eth0
       valid_lft 85677sec preferred_lft 85677sec
    inet6 fe80::5054:ff:feca:e48b/64 scope link
       valid_lft forever preferred_lft forever
```
Нужно найти LOOPBACK. Следовательно, имя локального интерфейса - lo

## Эксперимент с TCP
Открываем 3 терминала, заходим во внутрь виртуальной машины в каждом терминале (vagrant ssh).
Выполняем в первом терминале:
```
>>> sudo tcpdump -i lo port 3000 -v -A -n -e -K
```
Во втором терминале:
```
>>> nc -l 127.0.0.1 3000
```
В третьем терминале:
```
>>> telnet 127.0.0.1 3000
```
##Эксперимент с UDP
Открываем 3 терминала, заходим во внутрь виртуальной машины в каждом терминале (vagrant ssh).
Выполняем в первом терминале:
```
>>> sudo tcpdump -i lo port 3000 -v -A -n -e -K
```
Во втором терминале:
```
>>> nc -ul 127.0.0.1 3000
```
В третьем терминале:
```
>>> nc -u 127.0.0.1 3000
```
## Документация
* Документация по tcpdump https://www.tcpdump.org/tcpdump_man.html
* Документация по nc https://linux.die.net/man/1/nc
* Документация по telnet https://linux.die.net/man/1/telnet
