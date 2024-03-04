# Configurador de Servidor DNS BIND

Este é um script em Python que permite configurar um servidor de DNS BIND no Linux, criando zonas diretas e zonas reversas com base nos valores fornecidos pelo usuário via linha de comando.

## Como usar

### Configurar Zona Direta

Para configurar uma zona direta, execute o seguinte comando:

```bash
python configure_bind.py --zonadireta nome_da_zona
```

ou

```bash
python configure_bind.py -zd nome_da_zona
```

Substitua `nome_da_zona` pelo nome da sua zona direta.

### Configurar Zona Reversa

Para configurar uma zona reversa, execute o seguinte comando:

```bash
python configure_bind.py --zonareversa ip_reverso
```

ou

```bash
python configure_bind.py -zona ip_reverso
```

Substitua `ip_reverso` pelo endereço IP reverso da sua rede.

### Reiniciar o BIND

Para reiniciar o serviço BIND, execute o seguinte comando:

```bash
python configure_bind.py restart
```

### Parar o BIND

Para parar o serviço BIND, execute o seguinte comando:

```bash
python configure_bind.py stop
```

### Iniciar o BIND

Para iniciar o serviço BIND, execute o seguinte comando:

```bash
python configure_bind.py start
```

### Verificar Status do BIND

Para verificar o status do serviço BIND, execute o seguinte comando:

```bash
python configure_bind.py status
```

## Pré-requisitos

Certifique-se de ter o serviço BIND (named) instalado no seu sistema Linux.
