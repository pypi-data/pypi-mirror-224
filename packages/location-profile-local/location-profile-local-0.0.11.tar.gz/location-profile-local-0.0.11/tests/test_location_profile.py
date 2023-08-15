import sys
import os
from dotenv import load_dotenv
from logger_local.LoggerComponentEnum import LoggerComponentEnum

script_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(script_directory, '../location-profile-local'))

load_dotenv()
from circles_local_database_python.connection import Connection
from location_profile import LocationProfile
from logger_local.LoggerLocal import logger_local as local_logger


database = Connection("location_profile")
connection = database.connect()

TEST_GET_LOCATION_ID_BY_PROFILE_FUNCTION_NAME = "test_get_location_id"

LOCATION_PROFILE_LOCAL_COMPONENT_ID = 167
COMPONENT_NAME = 'location-profile-local/tests/test_location_profile.py'

TEST_PROFILE_ID = 1

object_to_insert = {
    'payload': 'test the method get_location_id_by_profile_id in location-profile-local',
    'component_id': LOCATION_PROFILE_LOCAL_COMPONENT_ID,
    'component_name': COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Unit_Test.value,
    'testing_framework': LoggerComponentEnum.testingFramework.pytest.value,
    'developer_email': 'tal.g@circ.zone'
}
local_logger.init(object=object_to_insert)

def test_get_location_id_by_profile_id():
    local_logger.start(TEST_GET_LOCATION_ID_BY_PROFILE_FUNCTION_NAME)

    profile_id = TEST_PROFILE_ID
    location_id = LocationProfile.get_location_id_by_profile_id(connection, profile_id)
    assert location_id is not []

    local_logger.end(TEST_GET_LOCATION_ID_BY_PROFILE_FUNCTION_NAME)