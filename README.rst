================
python-rsdclient
================

OpenStack client plugin for Rack Scale Design

This is a client for the `RSD
<https://www.intel.com/content/www/us/en/architecture-and-technology/rack-scale-design-overview.html>`_
Pod Manager API, which is based on OpenStack client framework. It provides a
Python API (``rsdclient/v1`` module) and a RSD specific plugin for
OpenStack client (``rsdclient/osc``).

Development takes place via the usual OpenStack processes as outlined in the
`developer guide <https://docs.openstack.org/infra/manual/developers.html>`_. The master
repository is on `git.openstack.org
<https://git.openstack.org/cgit/openstack/python-rsdclient>`_.

* Free software: Apache license
* Source: http://git.openstack.org/cgit/openstack/python-rsdclient
* Bugs: https://launchpad.net/python-rsdclient


.. contents:: Contents:
   :local:

Installation
------------

To use ``openstack rsd`` CLI, the python-openstackclient and python-rsdclient
should be installed::

    # pip install python-openstackclient
    # pip install python-rsdclient

To use the CLI, it requires two parts of configuration, OpenStack and RSD login
info.

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

OpenStackClient RSD Plugin
--------------------------

To get a list of available (sub)commands and options, run::

    $ openstack help rsd

To get usage and options of a command, run::

    $ openstack help rsd <sub-command>

An example of composing a node only with name::

    $ openstack rsd node compose --name "testing node"
