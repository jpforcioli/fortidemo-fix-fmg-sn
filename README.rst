Prepare the FortiAnalyzer
=========================

1. Fix the license issue

   .. code-block::

      config system interface
      edit port3
      set ip 10.100.88.2/24
      next 
      end

   .. note::
       
      FortiAnalyzer will ask you to reboot; please confirm.


Prepare the FortiManager
========================

1. Fix the license issue

   .. code-block::

      config system interface
      edit port3
      set ip 10.100.55.12/24
      next
      end

   .. note::
       
      FortiManager will ask you to reboot; please confirm.

2. Create a dedicated ``devops`` user:

   .. code-block::

      config system admin user
      edit devops
      set password fortinet
      set profileid Super_User
      set adom all_adoms
      set policy-package all_policy_packages
      set avatar "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAMCAgMCAgMDAwMEAwMEBQgFBQQEBQoHBwYIDAoMDAsKCwsNDhIQDQ4RDgsLEBYQERMUFRUVDA8XGBYUGBIUFRT/2wBDAQMEBAUEBQkFBQkUDQsNFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBT/wAARCABAAEADASIAAhEBAxEB/8QAHAAAAgIDAQEAAAAAAAAAAAAABwgACQQGCgUC/8QAMhAAAQMDAgUDAwMDBQAAAAAAAQIDBAUGEQAHCBIhMUEJE1EUIjIVYXEWgZEjJEJSYv/EABQBAQAAAAAAAAAAAAAAAAAAAAD/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwC1PU1NBHig4oKRw625Dbbhu3He9ac+loNswgVyJr5OE/aOoQCRk/2HXQG7Qr3M4pdqdnLgRQ70vilW9VlMpfESW6Qv2znCsAHocHQDhcdW4O2yf0neDYW76dXvbStiVacQ1KDLJzgJWkkJV0GU8xIz27Z9DhZ2Yq+5d5X7vVu5ZjECq3g4w1R7drUdDz1LpzScNpWhacocVnKgQD8gdtAw21W+Vh73wp8uxbogXNHgOJakrguc3tKUMpCv5AP+Nb1pH78t6u8F3EjW90LTsepXNtbeUFhiu0i2IocfpkxkcqH0MJHVtSQM46AqXnGRr7uDjn3Xr8GTctgbAXE5YtGxIqtRuRsw5T7AKSsRY5+5agkqORzAcp/jQO7qa0jZveS1t+LBp132hUUVClzE9U9nY7g/Jp1PdK0noQf5GQQdbvoJpLOLqBH2o4sNgN2ojbUibU6smzZ8RzBU4xJPIhxsEdFNqcJyMfHnRy4ut4arsJw83ffVDjRpdVpLLamGpYJaKluoRkgEE4Cif7aFuz3DBeF535a+7W9V+IvatU1oTKHQqdF+mplLccQP9QJPVxwZ6KUOhwfA0DZ6RTjB9R66eE7dE23M2gNUojzaXafXHqyWETk8o5+QBhYSUqPKQST2OOo16vEZ6go4aeLahWHcsBk2DPo7EiTUW0EyIrzjrqfd/wDTYCBkAZ7n9tHze3ajbvim2ZkU241Q6pbUtj66FWWFpUYiuUlMll3/AIkAnqOhBIOQSNAvewnqz7Tbv1WNR7hjy9vau+QlBqrqHISlHwJAwB18rSnTdbhXYmzdvLjuVDQmoplMkT0tJOQ77bSlgZ+DjXMjdtLhUS6avTqbP/VKfElusR5vJye+2lZCV8vjIAOP31ej6Xl2TtyODOhx7gdVU0w3pVJBkkr546VYSg57gJVy/wADGgyfTI2+Zt/hxZvR51mRW79nyK/OXH5Q22VurShtKUgBPKB1AHQqI8abjVfG7W3W4/p5WHW712svliobYRJ7Lztj3DGL30v1MlDREZ4HIHO6Dg48nqe7623Ul1m3aXUHUpQ5LitPqSnsCpAUQP8AOg0TiS2XRxC7K3LYC6oqiisNIQJyWfd9opcSsHlyM5Kcd/Ol8sXeHdzhk3Dsfbjex2j3Palxvoo1CvSksmO4iT+LTMlsYTlX2JCgB1PXPU6dDSScW9fhXnxh7A7dXDJ/QLXgzv6mVUZeW2Z81lX+2iNrPQq50jIz2VjuRoAF61Wx8t6ZZ27EBhbsVuOaFVFJ6hrC1OR1n4BLjqSfkJGq9afxF7mUnbJzb2FetWiWY4pSlUll7lbVzfkkkfdyH/pnlz1xrop3bbsG4LVl2rf86jt0itNmKqHVZbbPv57BHMQebPUEdQRpG6t6KG2tRnqlUq/rjgwHVc6I6m2H+VJ6gJXgZH7nOgp01aZ6WfHBZNhWC5tRd4at2REXJqECqqUS1Nzlxba8n7XOh5QOiuw69wRxzenBVeFyHGue1Z0y6bGWhKJUmUhIkwXvPuBAAKFdwoAY7H5KWMvOR3kOtLU06hQUhaDhSSOoIPg6C6KoUzeT1JrIdWibS9sdjqlLCorTkX6qqVVth/KHF5ICE+40CAkp/Huod32odMTRKLT6clwupiR244cIwVBCQnOP3xqtn0x+P+l1qi0vaC/ZEel1iNlqiVNWG2pqSoq9lfhLmScdgrt372aaCaGu/wDsBafEdt9LtW64hW0o+7Ens/bIgvj8Hml9woHx2IyDolamgTu1fS72nVBW9uLKuDdO5HUgOVmu1iUlxOBgcgbcGAAOnMVa0TZjfe2eBnc+/wDZbc28noFn09bFTs+fVQ9Jc+keB5o5UhCj9ih08d/40/8ArX6/t9a91S0yq1blKq8lCeRL06E28sJ+AVJJxoEjtmpUb1EeJ+uS01aXVNlNv40duBHhvPRWatUHk8y3HBhKilI5kcp8J+FnKgeoV6d87h/qEm+rEiOztu5LpL8ZvK3KStR6JV5LR7BXjsfBN01vWnRLSjusUOkQaOw6rncbgRkMpWrGMkJAycedZVWpMKu0yVTqjFamwZTamn476AtDiCMFKge4I0HLI06th1DrS1NuIIUlaDgpI7EHwddDnp9bjXHupwlWLX7qW6/WFNPRVyn888htp5bbbpJ7lSUJOfPfQkq/o97GVS+1V5t+44FNW9767fjTWxEPXJQFFsuJQfgLyOwI06Nr2xS7Lt6n0KiQmqbSaeymPGiMJwhptIwANB//2Q=="
      set rpc-permit read-write
      next
      end

3. Turn off offline mode

   .. code-block::

      config system admin setting 
      set offline_mode disable 
      end
    
Create the devops instance
==========================

1. Add the following device in the poc definition

   +------------------------+----------------------------------------------------------+
   | Name                   | ``devops``                                               |
   +------------------------+----------------------------------------------------------+
   | Image                  | *LXC_debian_buster-10.3_toolbox_amd64.zip [third-party]* |
   +------------------------+----------------------------------------------------------+
   | Use Network Parameters | *mgmt (192.168.100.0/255.255.255.0)*                     |
   +------------------------+----------------------------------------------------------+

2. Plug the ``devops`` device to the ``mgmt`` network

   +----------------------------+--------------------------------------+
   | Name                       | *eth0*                               |
   +----------------------------+--------------------------------------+
   | Address Configuration Mode | *static*                             |
   +----------------------------+--------------------------------------+
   | Network                    | *mgmt (192.168.100.0/255.255.255.0)* |
   +----------------------------+--------------------------------------+

   In our case, FortiPoC assign the IP address ``192.168.100.4``.

3. Start the poc

Configure the devops instance
=============================

1. Create the ``/fortipoc`` directory

   .. code-block:: shell

      mkdir /fortipoc

2. Create a python3 virtual environment

   .. code-block:: shell

      apt update
      apt install git --yes
      apt install python3-venv --yes
      python3 -m venv /fortipoc/.venv

3. Get the *fortidemo-fmg-fix-sn* repository

   .. code-block:: shell

      cd /fortipoc
      git clone https://github.com/jpforcioli/fortidemo-fix-fmg-sn.git
      cd fortidemo-fix-fmg-sn
      source /fortipoc/.venv/bin/activate
      pip3 install -r requirements.txt
      deactivate

4. Get the FortiManager ansible galaxy collection

   .. code-block:: shell
     
      cd /fortipoc/fortidemo-fix-fmg-sn/ansible
      source /fortipoc/.venv/bin/activate
      mkdir collections
      ansible-galaxy collection install fortinet.fortimanager:==2.0.3 -p collections
      deactivate

   .. note::

      You can ignore the following warning message:
      
      .. code-block::
      
         [WARNING]: The specified collections path
         '/fortipoc/fortidemo-fix-fmg-sn/ansible/collections' is not part of
         the configured Ansible collections paths
         '/root/.ansible/collections:/usr/share/ansible/collections'. The
         installed collection won't be picked up in an Ansible run. 
      
Playing the playbook
====================

- Without debug:

  .. code-block:: shell

     cd /fortipoc/fortidemo-fix-fmg-sn/ansible
     source /fortipoc/.venv/bin/activate
     ansible-playbook -i inventory main.yml
     deactivate

- With debug:

  .. code-block:: shell

     cd /fortipoc/fortidemo-fix-fmg-sn/ansible
     source /fortipoc/.venv/bin/activate
     ansible-playbook -i inventory main.yml -e debug_enabled=true
     deactivate