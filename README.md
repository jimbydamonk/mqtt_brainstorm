# mqtt_brainstorm
A set of docker + vagrant files to mimic a large number of brokers with MQTT (rabbitmq + mosquitto). 

This will create to rabbitmq clusters used to mimic regions in aws. Each cluster has 3 nodes. It will also create 2 mosquitto MQTT  brokers bridges to each node. Each rabbit and mosquitto runs in its own docker container and are linked accordingly. 

To start: `vagrant up`

To update using ansiblie `ansible-playbook -i inventory.txt playbooks/main.yml`


RabbitMQ 
--------
 * Username: admin
 * Password: admin

Only a one node per cluser per region is exposed globally through docker and virtual box.  These ports are for the rabbitmq gui admin.

 * node1 us-west-1
   ---------------
   * 10673
   * [http://localhost:10673](http://localhost:10673)

 * node1 eu-west-2
   ---------------
   * 11673 
   * [http://localhost:11673](http://localhost:11673)


Mosquito
--------
These are the base ports that mosquitto is listening on. They are exposed through docker and virtual box
 * us-west-1
   ---------
   * RabbitMQ Node1
     --------------
     * node1_1 10183:
     * node1_2 10283
   
   * RabbitMQ Node2
     --------------
     * node2_1 10184 
     * node2_2 10284

   * RabbitMQ Node3
     --------------
     * node3_1 10185 
     * node3_2 10285 

 * eu-west-2
   ---------
    * RabbitMQ Node1
      --------------
     * node1_1 11183
     * node1_2 11283
   
   * RabbitMQ Node2
     --------------
     * node2_1 11184 
     * node2_2 11284

   * RabbitMQ Node3
     --------------
     * node3_1 11185 
     * node3_2 11285 
