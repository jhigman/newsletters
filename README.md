Newsletters
===========

Find newsletters on the West Bridgford schools sites and copy them to Dropbox


The code relies on some libraries : requests, BeautifulSoup, dropbox:

    sudo apt-get install python3-pip
    sudo pip3 install beautifulsoup4
    sudo pip3 install dropbox

You'll need to setup a Dropbox access token in the environment:

    export DROPBOX_ACCESS_TOKEN=[access token]


Put this in the crontab:

    01 * * * * . /etc/profile; /home/ubuntu/newsletters/sync.py > /tmp/newsletters.log 2>&1

