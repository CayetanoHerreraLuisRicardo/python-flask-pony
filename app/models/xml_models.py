from lxml import objectify
from io import StringIO
from lxml import etree
class XMLMODELS:
    'Uso del paquete lxml para validar nuestro request body xml que nos envian'
    @staticmethod
    def parse_xml():
        schema_root = StringIO('''\
                <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
                    <xsd:element name="data" type="AType"/>
                    <xsd:complexType name="AType">
                        <xsd:sequence>
                            <xsd:element name="name" type="xsd:string" />
                            <xsd:element name="email" type="xsd:string" />
                            <xsd:element name="position" type="xsd:string" />
                            <xsd:element name="age" type="xsd:integer" />
                            <xsd:element name="image" type="xsd:base64Binary" />
                        </xsd:sequence>
                    </xsd:complexType>
                </xsd:schema>
                ''')
        schema = etree.XMLSchema(file=schema_root)

        parser = objectify.makeparser(schema=schema)
        return parser


