import re
def show_time_of_pid(line):
  pattern = r"USER \ ((\w))"
  result = re.search(pattern, line)
  return result

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)"))
print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)"))
print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)"))

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)"))
print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\""))
print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)"))
print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)"))
