# feed-app-iot-client
IoT prototye client for the feed application

## To run
Create a poll in the web client and click `add device`
![image](https://user-images.githubusercontent.com/109481934/201548455-ebb77422-c473-43e9-9987-cce5d20feb9e.png)

Enter device name and click `create device`

After submission, copy the connection key and device id(connection key will only be shown once)

Optionally you could copy the the information to the clipboard with the `copy connectiong config` button

![image](https://user-images.githubusercontent.com/109481934/201548538-6590aa00-c5a3-4b41-88a2-5782b27fe256.png)

Paste it into `config.json`.

Run with `python main.py`

For the IoT implementation run: `python main.py iot`

## cli button config

- `a` adds a vote to option 1
- `b` adds a vote to option 2
- `s` sends the votes to the api
- `d` displays the total votes on the connected poll
