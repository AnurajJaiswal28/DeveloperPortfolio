#!/bin/bash

SOURCE="$HOME/DeveloperPortfolio/Linux"
DEST="$HOME/DeveloperPortfolio/backup"

mkdir -p "$DEST"

BACKUP_FILE="$DEST/Linux_Backup_$(date +%Y%m%d_%H%M%S).tar.gz"

tar -czf "$BACKUP_FILE" -C "$HOME/DeveloperPortfolio" Linux

echo "================================"
echo "       BACKUP COMPLETED"
echo "================================"
echo "Source: $SOURCE"
echo "Backup saved at: $BACKUP_FILE"
echo "Backup file size:"
du -h "$BACKUP_FILE"
echo "Backup process completed successfully."
