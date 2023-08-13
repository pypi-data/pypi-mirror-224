=============================================================
Use Ansible playbook to set up a local refstack instance
=============================================================
These steps are meant for RefStack developers to help them with setting up
a local refstack instance.

In production RefStack server is managed by a set of playbooks and Ansible roles
defined in `system-config <https://opendev.org/opendev/system-config.git>`__
repository. Below instructions use these Ansible capabilities.

The RefStack server runs on Ubuntu 20.04 LTS in the production.

You can find an Ansible playbook in ``playbooks`` directory which semi-automates
the process of running refstack server in a container.

Execute the playbook by::

    $ ansible-playbook playbooks/run-refstack-in-container.yaml

In order to avoid setting certificates and https protocol (it's simpler and more
than enough for a testing instance), edit
``/etc/apache2/sites-enabled/000-default.conf`` like following:

* remove VirtualHost section for the port 80 and change the port of VirtualHost from 443 to 80
* Turn off the SSLEngine (`SSLEngine on -> SSLEngine off`)
* Remove SSLCertificate lines

and then restart the apache service so that it loads the new configuration::

    $ systemctl restart apache2

How to edit refstack files within the container
-----------------------------------------------

List the running container by::

    $ docker container list

You can enter the container by::

    $ sudo docker exec -it <container name> /bin/bash

If you wanna install new packages like f.e. vim, do the following::
    $ apt update
    $ apt install vim

Edit what's needed, backend is installed under
``/usr/local/lib/python3.7/site-packages/refstack/`` and frontend source files
can be found at ``/refstack-ui``

After you made the changes, make pecan to reload the files served::

    $ apt install procps  # to install pkill command
    $ pkill pecan

Killing pecan will kick you out of the container, however, pecan serves the
edited files now and you may re-enter the container.

Installing refstack with changes put for a review
-------------------------------------------------

In order to do this, you will need to rebuild the refstack image built by the
playbook.

Go to the location where the playbook downloaded system-config, default in
``/tmp/refstack-docker`` and edit the refstack's Dockerfile::

    $ cd /tmp/refstack-docker
    $ vim ./refstack-docker-files/Dockerfile

Replace::

    $ RUN git clone https://opendev.org/openinfra/refstack /tmp/src

by::

    $ RUN git clone https://opendev.org/openinfra/refstack.git /tmp/src \
      && cd /tmp/src && git fetch "https://review.opendev.org/openinfra/refstack" \
      refs/changes/37/<change id/<patchset number> && git checkout -b \
      change-<change id>-<patchset number> FETCH_HEAD

Then rebuild the image::

    $ docker image build -f Dockerfile -t <name:tag> .

Edit the ``docker-compose.yaml`` stored (by default) in
``/etc/refstack-docker/docker-compose.yaml`` and change the the image
(under `refstack-api`) to your image name and tag you set in the previous step.

After then spin a new container using the new image::

    $ cd /etc/refstack-docker
    $ docker-compose down  # if refstack container is already running
    $ docker-compose up -d

To see the server's logs use the following command::

    $ docker container logs -f <container name>

