2. Edit the ``/etc/rsdclient/rsdclient.conf`` file and complete the following
   actions:

   * In the ``[database]`` section, configure database access:

     .. code-block:: ini

        [database]
        ...
        connection = mysql+pymysql://rsdclient:RSDCLIENT_DBPASS@controller/rsdclient
