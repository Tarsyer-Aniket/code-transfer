#!/bin/bash

sudo cp /home/pi/MP-Birla-TLM/delete_truck_images.service /etc/systemd/user/

systemctl --user enable delete_truck_images.service

systemctl --user restart delete_truck_images.service

systemctl --user status delete_truck_images.service

