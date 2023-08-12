from invenio_records_resources.services.records.components import ServiceComponent

class PidRegisterComponent(ServiceComponent):
    def create(self, identity, data=None, record=None, errors=None, uow=None):
        record.register()
        
    def delete(self, identity, data=None, record=None, errors=None, uow=None):
        record.delete()