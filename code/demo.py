from Bio import Entrez
Entrez.email = "a@b.com"  # Tell NCBI who we are

'''
# In case we need to setup a proxy:

import os
os.environ["http_proxy"] = "http://proxyhost.example.com:8080"
'''


def get_record_from_id(id_code):
    handle = Entrez.efetch(db="nucleotide", id=id_code, retmode="text", rettype="fasta")  # Leemos la entrada dada la ID
    record = handle.read()
    handle.close()

    return record


def get_list(filename):
    idList = []
    with open(filename, 'r') as f:
        for line in f:
            idList.append(line.strip())  # a newline character (\n) is left at the end of the string
    return idList


if __name__ == "__main__":
    filename = 'idList.txt'
    idList = get_list(filename)

    for id_code in idList:
        record = get_record_from_id(id_code)
        with open(id_code.strip()+".fasta", "w") as output_fasta:
            output_fasta.write(record)
