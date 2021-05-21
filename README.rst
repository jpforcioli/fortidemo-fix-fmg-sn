1. Clone *fortimdemo-fix-fmg-sn* project

   .. code-block:: shell

      mkdir /fortipoc
      cd /fortipoc
      git clone https://github.com/jpforcioli/fortidemo-fix-fmg-sn.git

2. Create a python virtual environment

   .. code-block:: shell

      cd /fortipoc/fortidemo-fix-fmg-sn
      python3 -m venv .venv
      source .venv/bin/activate
   
3. Install the pre-requisites packages

   .. code-block:: shell

      cd /fortipoc/fortidemo-fix-fmg-sn   
      pip3 install -r requirements.txt
      
4. Install the fortimanager galaxy collection

   .. code-block:: shell
 
      mkdir -p /fortipoc/ansible/collections
      cd /fortipoc/ansible
      ansible-galaxy collection install fortinet.fortimanager:==2.0.3 -p collections
      
