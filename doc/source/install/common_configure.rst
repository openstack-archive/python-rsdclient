2. Edit the ``/etc/python-rsdclient/python-rsdclient.conf`` file and complete the following
   actions:

   * In the ``[database]`` section, configure database access:

     .. code-block:: ini

        [database]
        ...
        connection = mysql+pymysql://python-rsdclient:PYTHON-RSDCLIENT_DBPASS@controller/python-rsdclient
