import logging

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2_1.services.threat import ThreatQueryFilter
from management.mgmtsdk_v2_1.endpoints import *
from management.mgmtsdk_v2_1.entities.threat_notes import ThreatNote
from management.mgmtsdk_v2.exceptions import raise_from_response

logger = logging.getLogger('ThreatNotes_2.1')


class ThreatNoteQueryFilter(QueryFilter):

    QUERY_ARGS = {
        'creator': ['eq'],
        'creatorId': ['eq'],
    }
    QUERY_ARGS.update(ThreatQueryFilter.QUERY_ARGS)

    def __init__(self):
        super(ThreatNoteQueryFilter, self).__init__()


class ThreatsNotes(object):
    """ThreatsNotes service"""

    def __init__(self, client):
        self.client = client

    def get_threat_notes(self, threat_id, query_filter=None, **threat_args):
        """
        Get notes list, a paginated API, with sorting and filtering options (TBD). default sorting: createdAt, asc.
        :type query_filter: ThreatQueryFilter
        :type threat_args: dict
        :type threat_id
        :rtype: ManagementResponse
        """
        query_params = ThreatNoteQueryFilter.get_query_params(query_filter, threat_args)
        res = self.client.get(endpoint=GET_THREAT_NOTES.format(threat_id), params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get threat notes, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = [ThreatNote(**note) for note in res.data]
        return res

    def create_threat_note(self, text, query_filter=None, **threat_args):
        """
        Create a new note
        :type query_filter: ThreatQueryFilter
        :type threat_args: dict
        :type text
        :rtype: ManagementResponse
        """
        post_data = {'text': text}
        query_params = ThreatNoteQueryFilter.get_query_params(query_filter, threat_args)
        res = self.client.post(endpoint=CREATE_THREAT_NOTE, data=post_data, query_filter=query_params)
        if res.status_code != 200:
            logger.warning("Failed to create note, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def delete_threat_note(self, threat_id, note_id):
        """
        Delete a note
        :param threat_id:
        :param note_id:
        :rtype: ManagementResponse
        """
        res = self.client.delete(endpoint=DELETE_THREAT_NOTE.format(threat_id, note_id))
        if res.status_code != 200:
            logger.warning("Failed to delete threat note, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = res.data['success']
        return res

    def update_threat_note(self, threat_id, note_id, text):
        """
        Update a note
        :param threat_id:
        :param note_id:
        :type text
        :rtype: ManagementResponse
        """
        post_data = {'text': text}
        res = self.client.put(endpoint=UPDATE_THREAT_NOTE.format(threat_id, note_id), data=post_data)
        if res.status_code != 200:
            logger.warning("Failed to update threat note, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = ThreatNote(**res.data)
        return res
