=============================================
OpenStack Client Command-Line Interface (CLI)
=============================================

.. program:: openstack rsd
.. highlight:: bash

Synopsis
========

:program:`openstack [options] rsd` <command> [command-options]

:program:`openstack help rsd` <command>


Description
===========

The OpenStack Client plugin interacts with Rack Scale Design
through the ``openstack rsd`` command line interface (CLI).

To use ``openstack rsd`` CLI, the python-openstackclient and python-rsdclient
should be installed::

    # pip install python-openstackclient
    # pip install python-rsdclient

To use the CLI, two parts of configuration are required, OpenStack and RSD
login info.

At first, you have to provide your OpenStack username, password,
project, and auth endpoint. You can use configuration options
``--os-username``, ``--os-password``, ``--os-project-id``
(or ``--os-project-name``), and ``--os-auth-url``,
or set the corresponding environment variables::

    $ export OS_USERNAME=user
    $ export OS_PASSWORD=password
    $ export OS_PROJECT_NAME=project                         # or OS_PROJECT_ID
    $ export OS_PROJECT_DOMAIN_ID=default
    $ export OS_USER_DOMAIN_ID=default
    $ export OS_IDENTITY_API_VERSION=3
    $ export OS_AUTH_URL=http://auth.example.com:5000/identity

Then, you have to provide your RSD username, password,
SSL certificate with admin privilege, and pod manager URL. You can use
configuration options ``--rsd-username``, ``--rsd-password``, ``--rsd-verify``,
and ``--rsd-url``, or set the corresponding environment variables::

    $ export RSD_USERNAME=admin
    $ export RSD_PASSWORD=password
    $ export RSD_VERIFY=False     # or RSD_VERIFY=<path to SSL certificate>
    $ export RSD_URL=https://localhost:8443/


Getting help
============

To get a list of available (sub)commands and options, run::

    $ openstack help rsd

To get usage and options of a command, run::

    $ openstack help rsd <sub-command>


Examples
========

Compose node command allows the user to issue node composition command through
OpenStackClient(OSC)::

    $ openstack rsd node compose [--name <name>]
                                 [--description <description>]
                                 [--processor <processor requirements>]
                                 [--memory <memory requirements>]
                                 [--remote-drives <remote drives requirements>]
                                 [--local-drives <local drives requirements>]
                                 [--ethernet <ethernet requirements>]

Attach specific resource to existing composed node::

    $ openstack rsd node attach [--resource <resource uri>]
                                [--capacity <size>]
                                <node>

Detach specific resource from existing composed node::

    $ openstack rsd node detach [--resource <resource uri>]
                                <node>

Delete composed node allows the user to delete composed node(s) by
specifying <node_uuid>::

    $ openstack rsd node delete <node> [<node> ...]

Show composed node detail command allows the user to get composed node details
by specifying <node_uuid>::

    $ openstack rsd node show <node>

List composed node command allows the user to list all composed node
with brief info::

    $ openstack rsd node list
      +----------+------+--------------------------------------+-------------+
      | Identity | Name |                 UUID                 | Description |
      +----------+------+--------------------------------------+-------------+
      |    2     | Test | fd011520-86a2-11e7-b4d4-5d323196a3e4 |     None    |
      +----------+------+--------------------------------------+-------------+

List storage services command allows the user to list all storage services
brief info like below shows::

    $ openstack rsd storage list
      +----------+-----------------+-----------------------------+
      | Identity |       Name      |         Description         |
      +----------+-----------------+-----------------------------+
      |    1     | Storage Service | Storage Service for Testing |
      +----------+-----------------+-----------------------------+

Show storage detail command allows the user to display
the storage service details::

    $ openstack rsd storage show <storage service>

List fabric command allows the user to list all fabrics with brief info::

    $ openstack rsd fabric list

Show fabric detail command allows the user to display the fabric details::

    $ openstack rsd fabric show <fabric>


Command Reference
=================
.. toctree::
   :glob:
   :maxdepth: 3
