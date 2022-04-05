sudo apt-get -y install pigpio
sudo systemctl enable pigpiod.service
sudo systemctl start pigpiod
curl http://abyz.me.uk/rpi/pigpio/code/irrp_py.zip | zcat > irrp.py
