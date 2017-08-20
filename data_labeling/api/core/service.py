"""Module responsible for definition of Core service"""
from typing import Dict
from flask_restplus import Resource

from data_labeling.api import api
from data_labeling.api.core import serializers
from data_labeling.api.core.business import success

core_ns = api.namespace('core', 'Core methods')


@core_ns.route('/status')
class Status(Resource):
    """Status endpoint that checks if everything is all right"""

    @staticmethod
    @core_ns.marshal_with(serializers.status)
    @core_ns.doc(description='Checks if API is running properly.')
    @core_ns.doc(responses={200: 'Success'})
    def get() -> Dict[str, bool]:
        """Return status of the API"""
        return success()
