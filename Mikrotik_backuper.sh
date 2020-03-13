#!/usr/bin/env bash
#
#
# Please note that for the correct operation you
# will need the utilities found here
#
#
DIR=                   # example: DIR=/home/user/backups/
LGIN=                  # example: LGIN=admin 
PRT=                   # example: PRT=22
#SHELF=                # example: SHELF=13
#
DATE=$(echo `date +%Y.%m.%d`)
exec 2>> $DIR$DATE".log"
gg=success
#
##### DO NOT DELETE COMMENTS IN THE BLOCK BELOW #####
#
# router0               
#
#NEWVARIABLE
#
#NEWFUNK
#
function startsaver {
# NEWNAME
}
#
startsaver >> $DIR$DATE.log
#
##### DO NOT DELETE COMMENTS IN THE BLOCK ABOVE #####
#
#
#
##### ARCHIVING BACKUPS AND DELETING OLD VERSIONS #####
#
statsave=$(cat $DIR$DATE.log | grep "ERROR \| failed \| denied \| error \| Permission" && echo ERROR || echo success )
#
function archandel {
echo "

  _______________________________
  Archiving of collected backup's started:"
if [ "$statsave" = "$gg" ]
  then
    zip -9 -j $DIR$DATE.zip $DIR*.backup $DIR*rsc
    rm $DIR*.backup $DIR*.rsc
#    echo "
#    search and delete old versions"
#    find "$DIR"2* -mtime +$SHELF -delete
    echo "
  Archiving done
  _______________________________"
  else
    echo "  ...............................
                ERROR
    not all backups are received
        сheck the correctness
         of the entered data
          and read the log!
  ..............................."
    zip -9 -j $DIR$DATE"_brocken".zip $DIR*.backup $DIR*rsc
    rm $DIR*.backup $DIR*.rsc
    echo "  _______________________________"
fi
}
#
archandel >> $DIR$DATE.log
#####_____________________________________________#####
#
#
#
##### TELEGRAM ALERT SETTINGS #####
#TOKEN=
#IDCHAT=
#URL="https://api.telegram.org/bot$TOKEN/sendMessage"
##PROXYSOCKS=
##TGMESS="curl --silent --show-error --fail -k -G -o /dev/null -x socks5://${PROXYSOCKS} ${URL} -d chat_id=${IDCHAT} "
#TGMESS="curl --silent --show-error --fail -k -G -o /dev/null $URL -d chat_id=$IDCHAT "
#Function alerts
#function alert {
#  echo "  _______________________________
#  Alerts are generated"
#if [ "$statsave" = "$gg" ]
#  then
#    $TGMESS --data-urlencode "text=Creation of backups $DATE was successful"
#    echo "END
#  _______________________________"
#  else
#    $TGMESS --data-urlencode "text=An error occurred while creating backups, check the $DATE log"
#    echo "END
#  _______________________________"
#fi
#}
#####_________________________#####
#alert >> $DIR$DATE.log
