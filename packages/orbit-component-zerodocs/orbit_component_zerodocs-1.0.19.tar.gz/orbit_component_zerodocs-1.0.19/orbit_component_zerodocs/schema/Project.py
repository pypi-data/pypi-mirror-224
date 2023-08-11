from orbit_component_base.src.orbit_orm import BaseTable, BaseCollection, register_class, register_method
from orbit_database import SerialiserType, Doc
from loguru import logger as log


class ProjectTable (BaseTable):

    norm_table_name = 'projects'
    norm_auditing = True
    norm_codec = SerialiserType.UJSON
    norm_ensure = [
        {'index_name': 'by_params', 'func': '{root}|{provider}|{project}|{branch}'},
        {'index_name': 'by_root', 'duplicates': True, 'func':
            """def func(doc): return f'{doc["root"]}|{doc["index"] or 0:06}'.encode()"""
        }
    ]

    def from_params (self, params, transaction=None):
        doc = Doc(params)
        self.set(self.norm_tb.seek_one('by_params', doc, txn=transaction))
        if not self.isValid:
            self.set(doc)
        return self


@register_class
class ProjectCollection (BaseCollection):

    table_class = ProjectTable
    table_methods = []

    async def put (self, params):
        doc = self.table_class().from_params(params)
        if doc.isValid:
            log.debug(f'Update')
            doc.update(params).save()
        else:
            log.debug(f'Append')
            doc.update(params).append()
        return {'ok': True}

    async def remove (self, params):
        doc = self.table_class().from_params(params)
        if not doc.isValid:
            log.error(f"Project not found: {params}")
            return {'ok': False, 'error': f'Project entry not found: {id}'}
        doc.delete()
        return {'ok': True}
    
    @register_method
    def get_ids(cls, session, params, transaction=None):
        ids, data = [], []
        filter = params.get('filter')
        lower = dict(filter, **{'index': 0})
        upper = dict(filter, **{'index': 999999})
        # limit = Doc(params.get('filter'))
        for result in cls().filter(index_name='by_root', lower=Doc(lower), upper=Doc(upper)):
            session.append(params, result.oid.decode(), ids, data, result, strip=cls.table_strip)
        session.update(ids, params)
        return {'ok': True, 'ids': ids, 'data': data}

    async def renumber (self, params):
        for (i, key) in enumerate(params.get('ids')):
            doc = self.table_class().from_key(key)
            doc.update({'index': i}).save()
        return {'ok': True}
