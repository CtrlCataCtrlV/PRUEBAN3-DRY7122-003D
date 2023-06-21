from ncclient import manager
from ncclient.operations import RPCError

# Datos de conexion al router CSR1000V
router_ip = '192.168.198.130'
router_port = 830
router_username = 'cisco'
router_password = 'cisco123!'

# Nuevo hostname
new_hostname = 'GonzalezQuiroz'

# Definir la configuracion XML para cambiar el hostname
config_template = '''
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>{new_hostname}</hostname>
    </native>
</config>
'''

# Reemplazar el nombre de host en la plantilla XML
config_payload = config_template.format(new_hostname=new_hostname)

# Establecer una conexi贸n NETCONF con el router
with manager.connect(
    host=router_ip,
    port=router_port,
    username=router_username,
    password=router_password,
    hostkey_verify=False
) as m:
    try:
        # Enviar la configuraci贸n al router
        response = m.edit_config(target='running', config=config_payload)
        print('El hostname se ha cambiado correctamente.')
    except RPCError as e:
        print('Ha ocurrido un error al cambiar el hostname:')
        print(e)