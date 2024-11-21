
### Backup the Entire Database:

```
python manage.py dumpdata --output=backup.json
```
### Backup a Specific App or Model::

```
python manage.py dumpdata product --output=product_backup.json

```
### Including Media Files:

```
tar -cvf media_backup.tar media/

```
---
### Restore the Entire Backup:

```
python manage.py loaddata backup.json

```

### Restore a Specific App or Model:

```
python manage.py loaddata product_backup.json

```

