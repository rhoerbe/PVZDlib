import json
import pytest
from PVZDpy.samlentitydescriptor import SAMLEntityDescriptor
from PVZDpy.userexceptions import InputValueError

#path_prefix = 'PVZDpy/tests/'
path_prefix = ''

@pytest.fixture
def ed1():
    return SAMLEntityDescriptor(ed_path=path_prefix+'testdata/03_idp_valid_unsigned_c14n.xml')

@pytest.fixture
def xml_str1():
    # xml encoding _must_ be utf-8
    with open(path_prefix+'testdata/03_idp_valid_unsigned_c14n.xml') as fd:
        return fd.read()

@pytest.fixture
def entityid1():
    return 'https://idp.example.com/idp.xml'

def test_get_entityid():
    assert ed1().get_entityid() == entityid1()

#def test_get_xml_str():
#    x = ed1().get_xml_str().rstrip()
#    y = xml_str1().rstrip()
#    assert x == y

def test_get_signing_certs():
    x = ed1().get_signing_certs()
    assert isinstance(x, list)

def test_validate_xsd():
    ed1().validate_xsd()

# def test_validate_schematron():
#     self.fail()

def test_get_namespace_prefix():
    assert ed1().get_namespace_prefix() == 'md'

def test_get_filename_from_entityid():
    assert ed1().get_filename_from_entityid() == 'idpExampleCom_idpXml.xml'

# def test_cert2entitydescriptor():
#     self.fail()

# def test_create_delete():
#     self.fail()

# def test_write():
#     tested with wrapper (samled_pvp.py)


