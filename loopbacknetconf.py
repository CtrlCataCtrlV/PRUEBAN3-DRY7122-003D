from ncclient import manager
from ncclient.operations import RPCError

csr_host = '192.168.198.130'  # Dirección IP del CSR1000V
csr_username = 'cisco'  # Nombre de usuario para acceder al CSR1000V
csr_password = 'cisco123!'  # Contraseña para acceder al CSR1000V

loopback_number = '2'
loopback_ip = '2.2.2.2'
loopback_subnet = '255.255.255.255'

xml_template = '''
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>{loopback_number}</name>
                <ip>
                    <address>
                        <primary>
                            <address>{loopback_ip}</address>
                            <mask>{loopback_subnet}</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
    </native>
</config>
'''

xml_data = xml_template.format(loopback_number=loopback_number,
                              loopback_ip=loopback_ip,
                              loopback_subnet=loopback_subnet)

with manager.connect(host=csr_host, username=csr_username, password=csr_password,
                     device_params={'name': 'csr'}, hostkey_verify=False) as conn:
    try:
        result = conn.edit_config(target='running', config=xml_data)
        print('La configuración se ha aplicado correctamente.')
    except RPCError as e:
        print('Ha ocurrido un error al aplicar la configuración:')
        print(e)
