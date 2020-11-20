import subprocess
w_cmds = subprocess.check_output(['netsh', 'wlan', 'show', 'profile']).decode('utf-8').split('\n')
w_cmds = [a.split(":")[1][1:-1] for a in w_cmds if "All User Profile" in a]
for i in w_cmds:
    cmd_results = subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear']).decode('utf-8').split('\n')
    cmd_results = [b.split(":")[1][1:-1] for b in cmd_results if "Key Content" in b]
    try:
        print("{:<30} : {:<}".format(i, cmd_results[0]))
    except IndexError:
        print("{:<30} : {:<}".format(i, ""))
