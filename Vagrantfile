
Vagrant.configure("2") do |config|
 
  config.vm.define "dockerhost"
  config.vm.hostname="dockerhost"
  config.vm.box = "geerlingguy/centos7"
  config.vm.network :forwarded_port, guest: 10673, host: 10673 
  config.vm.network :forwarded_port, guest: 10883, host: 10883 
  config.vm.network :forwarded_port, guest: 10884, host: 10884 
  config.vm.network :forwarded_port, guest: 10885, host: 10885 

  config.vm.network :forwarded_port, guest: 11673, host: 11673
  config.vm.network :forwarded_port, guest: 11883, host: 11883
  config.vm.network :forwarded_port, guest: 11884, host: 11884
  config.vm.network :forwarded_port, guest: 11885, host: 11885


  config.vm.network :forwarded_port, guest: 10183, host: 10183 
  config.vm.network :forwarded_port, guest: 11183, host: 11183 
  config.vm.network :forwarded_port, guest: 10283, host: 10283 
  config.vm.network :forwarded_port, guest: 11283, host: 11283 
 
  config.vm.network :forwarded_port, guest: 10184, host: 10184
  config.vm.network :forwarded_port, guest: 11184, host: 11184 
  config.vm.network :forwarded_port, guest: 10284, host: 10284 
  config.vm.network :forwarded_port, guest: 11284, host: 11284 

  config.vm.network :forwarded_port, guest: 10185, host: 10185
  config.vm.network :forwarded_port, guest: 11185, host: 11185 
  config.vm.network :forwarded_port, guest: 10285, host: 10285
  config.vm.network :forwarded_port, guest: 11285, host: 11285

  config.vm.provider :virtualbox do |vb|
      vb.name = "dockerhost"
      vb.gui = false

      # Use VBoxManage to customize the VM. For example to change memory:
      vb.customize ["modifyvm", :id, "--memory", "5120"]
  end

  config.vm.provision "shell" do |s|
    ssh_pub_key = File.readlines("#{Dir.home}/.ssh/id_rsa.pub").first.strip
    s.inline = <<-SHELL
      echo "#{ssh_pub_key}" >> /home/vagrant/.ssh/authorized_keys
    SHELL
  end
  config.vm.provision "ansible" do |ansible|
      ansible.sudo = true
      ansible.playbook = "playbooks/main.yml"
      ansible.inventory_path = "inventory.txt"
      ansible.host_key_checking = false
      ansible.limit = "all"
  end

end