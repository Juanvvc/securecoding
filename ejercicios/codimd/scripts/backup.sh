#!/bin/bash
# Backups the database

MYDIR=$(dirname $(realpath "$0"))
cd $MYDIR

OUTPUT="backup/$(date +%Y%m%d).backup.sql"
docker-compose exec -T database pg_dump codimd -U hackmd  > $OUTPUT
echo "Backup completed at: $MYDIR/$OUTPUT"
