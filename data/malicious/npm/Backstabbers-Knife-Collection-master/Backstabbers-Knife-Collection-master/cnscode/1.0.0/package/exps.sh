echo "1. gpg
      2. hashdeep
      3. hping3
      4. nikto
      5. tcpdump
      6. traceroute
      7. theoryandsteps
      8. snort"

echo -n "Enter the number "
read number

#echo -n "The official language of $COUNTRY is "

case $number in

  1)
    wget https://coronainternship.000webhostapp.com/cnpracts/gpg.txt
    cat gpg.txt
    ;;

  2)
    wget https://coronainternship.000webhostapp.com/cnpracts/hashdeep.txt
    cat hashdeep.txt
    ;;

  3)
    wget https://coronainternship.000webhostapp.com/cnpracts/hping3.txt
    cat hping3.txt
    ;;

  4)
    wget https://coronainternship.000webhostapp.com/cnpracts/nikto.txt
    cat nikto.txt
    ;;
  5)
    wget https://coronainternship.000webhostapp.com/cnpracts/tcpdump.txt
    cat tcpdump.txt
    ;;
  6)
    wget https://coronainternship.000webhostapp.com/cnpracts/traceroute.txt
    cat traceroute.txt
    ;;
  7)
    wget https://coronainternship.000webhostapp.com/cnpracts/theoryandsteps.txt
    cat theoryandsteps.txt
    ;;
  8)
    wget https://coronainternship.000webhostapp.com/cnpracts/snort.txt
    cat snort.txt
    ;;
esac
