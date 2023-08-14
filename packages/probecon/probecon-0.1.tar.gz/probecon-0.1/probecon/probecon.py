import os
import subprocess

def subdomain(target):
    # amass
    os.makedirs('recon', exist_ok=True)
    subprocess.run(['amass', 'enum', '-src', '-df', f'{target}/domains.txt', '-o', f'{target}/recon/domain1.txt'])

    # Subfinder
    subprocess.run(['subfinder', '-dL', f'{target}/domains.txt'], stdout=subprocess.PIPE, text=True, shell=True, check=True)

    # Anubis
    subprocess.run(['anubis', '-f', f'{target}/domains.txt', '-o', f'{target}/recon/domain3.txt'])

    # Alive domains
    alive_process = subprocess.Popen(f'cat {target}/recon/domain1.txt {target}/recon/domain2.txt {target}/recon/domain3.txt | httpx -status-code | grep 200 | cut -d " "', stdout=subprocess.PIPE, text=True, shell=True)
    with open(f'{target}/recon/aliveDomain.txt', 'w') as alive_file:
        subprocess.run(['tee', '-a', f'{target}/recon/aliveDomain.txt'], stdin=alive_process.stdout, text=True, check=True)
