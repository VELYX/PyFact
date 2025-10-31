def restore_documents(originals, backups):
    return set(
        filter(lambda x: not x.isdigit(), map(lambda x: x.upper(), originals + backups))
    )
