# Mikrotik backup script
### For computers running GNU/Linux
### This project is intended for centralized backups of devices running router_os (Mikrotik routers)


***This is my first project, do not judge strictly***

***
***
### Properties:
* Version control
* Sending notifications to the Telegram messenger
* All backups (".backup" and ".rsc") are archived in one place
* You can adapt this project to the devices of any vendor

***
### How to use it?
> If there is no time to read, then briefly:
>
> A file with the ".sh" extension is the main script, it is you who will run it,
>
> and the ".py" file will allow you to add new routers to your script.
>
> The example file contains comments that will help you understand how this script works.
***

1. Check that you have all the necessary installed

`   $   sudo apt-get install openssh-server openssh-client scp sshpass curl zip python3`

2. Open "Mikrotik_backuper.sh"
3. Find the lines "`DIR=`","`LGIN=`","`PRT=`"
4. Enter the directory where your backups will be synchronized (with a slash at the end),
   your login on the routers and the port, respectively

***This is almost enough to start making backups***

##### Version control:
1. Find the line "`#SHELF=`"
   Remove `#` at the beginning and specify (in days) the expiration date of backups
2. In function `archandel`, uncomment the following lines
   `#    echo "`
   `#    search and delete old versions"`
   `#    find "$DIR"2* -mtime +$SHELF -delete`

***archives older than the specified period will be deleted each time the script is run***
##### Telegram alerts:
1. Find the line at the end of the file `##### TELEGRAM ALERT SETTINGS #####` and delete all the first `#` below
   It should turn out:
      
      `TOKEN=`
      
      `IDCHAT=`
      
      `URL="https://api.telegram.org/bot$TOKEN/sendMessage"`
      
      `#PROXYSOCKS=`
      
      `#TGMESS="curl --silent --show-error --fail -k -G -o /dev/null -x socks5://${PROXYSOCKS} ${URL} -d chat_id=${IDCHAT} "`
      
      `TGMESS="curl --silent --show-error --fail -k -G -o /dev/null $URL -d chat_id=$IDCHAT "`
      
      `Function alerts`
      
      `function alert {`
      
      `echo "  _______________________________`
      
      `Alerts are generated"`
      
      `if [ "$statsave" = "$gg" ]`
      
      `then`
      
      `$TGMESS --data-urlencode "text=Creation of backups $DATE was successful"`
      
      `echo "END`
      
      `_______________________________"`
      
      `else`
      
      `$TGMESS --data-urlencode "text=An error occurred while creating backups, check the $DATE log"`
      
      `echo "END`
      
      `_______________________________"`
      `fi`
      
      `}`
      
      `#####_________________________#####`
      
      `alert >> $DIR$DATE.log`

2.Enter the bot token in `TOKEN=` and ID your chat in `IDCHAT=`. Depending on how you will connect to the Telegram API, comment out (uncomment and enter) the necessary variables

***Now, every time you run the script, your bot will tell you how it went***


>See an "Example_code" if you have any questions.
>
>Using the "Supplementer.py" add new routers to the main script. With the help of utility "cron" you can automate the launch of the script.  
>
>The log and archive with backups will be stored in the folder you specified.  
>
>Please note that you should not use this script at the border of the day, as the names use the date (and yes, check it on your device before using the script)

---
#### P.S.:
>
> When I wrote this script, I assumed that you had previously connected via ssh to your devices, but if you hadn’t done this before, connect to it before adding a new device to the script.
>
> This is necessary in order to answer yes to the following question:
>
> `RSA key fingerprint is SHA256:Oa00aaaaAA0Aa00AAaa0a/AaaaAAaaaAA0AAAaa0aaa.
Are you sure you want to continue connecting (yes/no)?`

***
##### ***LICENSE MIT 2020 ©***
