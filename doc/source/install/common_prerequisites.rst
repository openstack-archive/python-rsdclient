Prerequisites
-------------

Before you install and configure the python-rsdclient service,
you must create a database, service credentials, and API endpoints.

#. To create the database, complete these steps:

   * Use the database access client to connect to the database
     server as the ``root`` user:

     .. code-block:: console

        $ mysql -u root -p

   * Create the ``python-rsdclient`` database:

     .. code-block:: none

        CREATE DATABASE python-rsdclient;

   * Grant proper access to the ``python-rsdclient`` database:

     .. code-block:: none

        GRANT ALL PRIVILEGES ON python-rsdclient.* TO 'python-rsdclient'@'localhost' \
          IDENTIFIED BY 'PYTHON-RSDCLIENT_DBPASS';
        GRANT ALL PRIVILEGES ON python-rsdclient.* TO 'python-rsdclient'@'%' \
          IDENTIFIED BY 'PYTHON-RSDCLIENT_DBPASS';

     Replace ``PYTHON-RSDCLIENT_DBPASS`` with a suitable password.

   * Exit the database access client.

     .. code-block:: none

        exit;

#. Source the ``admin`` credentials to gain access to
   admin-only CLI commands:

   .. code-block:: console

      $ . admin-openrc

#. To create the service credentials, complete these steps:

   * Create the ``python-rsdclient`` user:

     .. code-block:: console

        $ openstack user create --domain default --password-prompt python-rsdclient

   * Add the ``admin`` role to the ``python-rsdclient`` user:

     .. code-block:: console

        $ openstack role add --project service --user python-rsdclient admin

   * Create the python-rsdclient service entities:

     .. code-block:: console

        $ openstack service create --name python-rsdclient --description "python-rsdclient" python-rsdclient

#. Create the python-rsdclient service API endpoints:

   .. code-block:: console

      $ openstack endpoint create --region RegionOne \
        python-rsdclient public http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        python-rsdclient internal http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        python-rsdclient admin http://controller:XXXX/vY/%\(tenant_id\)s
