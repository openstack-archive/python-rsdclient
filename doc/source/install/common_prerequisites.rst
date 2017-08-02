Prerequisites
-------------

Before you install and configure the rsdclient service,
you must create a database, service credentials, and API endpoints.

#. To create the database, complete these steps:

   * Use the database access client to connect to the database
     server as the ``root`` user:

     .. code-block:: console

        $ mysql -u root -p

   * Create the ``rsdclient`` database:

     .. code-block:: none

        CREATE DATABASE rsdclient;

   * Grant proper access to the ``rsdclient`` database:

     .. code-block:: none

        GRANT ALL PRIVILEGES ON rsdclient.* TO 'rsdclient'@'localhost' \
          IDENTIFIED BY 'RSDCLIENT_DBPASS';
        GRANT ALL PRIVILEGES ON rsdclient.* TO 'rsdclient'@'%' \
          IDENTIFIED BY 'RSDCLIENT_DBPASS';

     Replace ``RSDCLIENT_DBPASS`` with a suitable password.

   * Exit the database access client.

     .. code-block:: none

        exit;

#. Source the ``admin`` credentials to gain access to
   admin-only CLI commands:

   .. code-block:: console

      $ . admin-openrc

#. To create the service credentials, complete these steps:

   * Create the ``rsdclient`` user:

     .. code-block:: console

        $ openstack user create --domain default --password-prompt rsdclient

   * Add the ``admin`` role to the ``rsdclient`` user:

     .. code-block:: console

        $ openstack role add --project service --user rsdclient admin

   * Create the rsdclient service entities:

     .. code-block:: console

        $ openstack service create --name rsdclient --description "rsdclient" rsdclient

#. Create the rsdclient service API endpoints:

   .. code-block:: console

      $ openstack endpoint create --region RegionOne \
        rsdclient public http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        rsdclient internal http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        rsdclient admin http://controller:XXXX/vY/%\(tenant_id\)s
