import argparse
import subprocess
import os

def configurar_zona_direta(nome_zona):
    # Adiciona uma entrada no arquivo /etc/bind/named.conf.local
    with open('/etc/bind/named.conf.local', 'a') as f:
        f.write(f'zone "{nome_zona}" IN {{\n')
        f.write(f'    type master;\n')
        f.write(f'    file "/etc/bind/db.{nome_zona}";\n')
        f.write(f'}};\n')

    # Cria o arquivo de zona direta
    with open(f'/etc/bind/db.{nome_zona}', 'w') as f:
        f.write(f'$TTL    604800\n')
        f.write(f'@       IN      SOA     ns.{nome_zona}. admin.{nome_zona}. (\n')
        f.write(f'                  3     ; Serial\n')
        f.write(f'             604800     ; Refresh\n')
        f.write(f'              86400     ; Retry\n')
        f.write(f'            2419200     ; Expire\n')
        f.write(f'             604800 )   ; Negative Cache TTL\n')
        f.write(f';\n')
        f.write(f'@       IN      NS      ns.{nome_zona}.\n')
        f.write(f'ns      IN      A       192.168.1.1\n')  # IP do servidor DNS BIND

    print(f"Zona direta configurada para {nome_zona}")

def configurar_zona_reversa(ip_reverso):
    # Adiciona uma entrada no arquivo /etc/bind/named.conf.local
    with open('/etc/bind/named.conf.local', 'a') as f:
        ip_parts = ip_reverso.split('.')
        subnet = '.'.join(ip_parts[:3])  # Subnet da rede
        f.write(f'zone "{subnet}.in-addr.arpa" IN {{\n')
        f.write(f'    type master;\n')
        f.write(f'    file "/etc/bind/db.{subnet}";\n')
        f.write(f'}};\n')

    # Cria o arquivo de zona reversa
    with open(f'/etc/bind/db.{subnet}', 'w') as f:
        f.write(f'$TTL    604800\n')
        f.write(f'@       IN      SOA     ns.{subnet}. admin.{subnet}. (\n')
        f.write(f'                  3     ; Serial\n')
        f.write(f'             604800     ; Refresh\n')
        f.write(f'              86400     ; Retry\n')
        f.write(f'            2419200     ; Expire\n')
        f.write(f'             604800 )   ; Negative Cache TTL\n')
        f.write(f';\n')
        f.write(f'@       IN      NS      ns.{subnet}.\n')
        # Inverte os três últimos octetos do IP reverso para o endereço de rede
        network_address = '.'.join(ip_parts[:3][::-1])
        f.write(f'{network_address} IN PTR ns.{subnet}.\n')

    print(f"Zona reversa configurada para {ip_reverso}")

def reiniciar_bind():
    subprocess.run(["sudo", "service", "named", "restart"])

def parar_bind():
    subprocess.run(["sudo", "service", "named", "stop"])

def iniciar_bind():
    subprocess.run(["sudo", "service", "named", "start"])

def verificar_status_bind():
    subprocess.run(["sudo", "service", "named", "status"])

def main():
    parser = argparse.ArgumentParser(description="Configurar servidor de DNS BIND")
    parser.add_argument("--zonadireta", "-zd", help="Configurar zona direta")
    parser.add_argument("--zonareversa", "-zona", help="Configurar zona reversa")
    parser.add_argument("action", choices=["start", "stop", "restart", "status"], help="Ação a ser executada")

    args = parser.parse_args()

    if args.zonadireta:
        configurar_zona_direta(args.zonadireta)
    elif args.zonareversa:
        configurar_zona_reversa(args.zonareversa)
    elif args.action == "start":
        iniciar_bind()
    elif args.action == "stop":
        parar_bind()
    elif args.action == "restart":
        reiniciar_bind()
    elif args.action == "status":
        verificar_status_bind()

if __name__ == "__main__":
    main()