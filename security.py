from netmiko import ConnectHandler
ip = open('switch-ip.txt')
for i in ip:
    i = i.strip()
    p = open('pass.txt')
    for password in p:
        password = password.strip()
        data_ios = {
            'device_type': 'cisco_ios',
            'ip': i,
            'username': 'No_Tacacs',
            'password': password,
            'secret': password,
        }
        print("written by Idowu Kusoro on 26/01/2021")
        print("Logon to switchip " + i + " with the below credentials")
        print(data_ios)
        try:
            print(" ")
            print("Trying now to connect")
            net_connect = ConnectHandler (**data_ios)
            net_connect.enable()
            output = net_connect.send_command("show run | include username")
            print("Logon Sucessful")
            print("Printing the List of Account on Switch")
            print("output")
            p.close()
            print(" ")
            break
        except Exception:
            print("Password " + password + " Authentication failed", i)
            print(" ")
            continue
    exit
