FROM postgres:latest

# crontab
RUN mkdir /backups
COPY ./backup.sh /backups
COPY ./weed.sh /backups
COPY ./cronfile /etc/cron.d/cronfile
RUN apt-get update && apt-get -y install cron
RUN chmod 0644 /etc/cron.d/cronfile
RUN crontab /etc/cron.d/cronfile
RUN touch /var/log/cron.log

# The postgres image's entrypoint expects the docker command to only contain flags to
# pass postgres. It runs the entrypoint twice, the second times as the postgres user.
# We need to start the cron service the first time it runs, when it's still being run
# as the root user. We're going to add a check that looks at the first argument and
# if it's 'cron', starts the service and then removes that argument.
RUN awk '$0 ~ /^\t_main "\$@"$/ { print "\tif [[ $1 == cron ]]; then\n\t\tservice cron start\n\t\tshift\n\tfi" }{ print }' docker-entrypoint.sh > bookwyrm-entrypoint.sh
RUN chown postgres /bookwyrm-entrypoint.sh
RUN chmod u=rwx,go=r /bookwyrm-entrypoint.sh
