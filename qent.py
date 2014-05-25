#!/usr/bin/env python3

__version__ = "0.0.0"

'''
name: Query entrez (qent)
usage:
    qent -given <input_type> -get <output_type> -i input -o output

    input_type inclues taxid, sciname, gi, etc
    output_type includes taxid, sciname, lineage, etc

    qent could be expanded quite far, but for now I am mostly interested in
    getting lineages
'''
