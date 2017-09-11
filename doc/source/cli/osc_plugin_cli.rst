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

To use ``openstack rsd`` CLI, the python-rsdclient should be installed::

    # pip install python-rsdclient

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

    $ openstack rsd compose
    --rsd-url "https://localhost:8442/redfish/v1/"
    --rsd-username "admin"
    --rsd-password "admin"
    --rsd-disable-verify
    --name "Fake-Name"

Delete composed node allows the user to delete composed node(s) by
specifying <node_uuid>::

    $ openstack rsd node delete <node_uuid>

Show composed node detail command allows the user to get composed node details
by specifying <node_uuid>::

    $ openstack rsd node show <node_uuid>

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

    $ openstack rsd storage show

Command Reference
=================
.. toctree::
   :glob:
   :maxdepth: 3
