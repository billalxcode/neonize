import copy
from ..proto.Neonize_pb2 import JID


def JIDToNonAD(jid: JID):
    new_jid = copy.deepcopy(jid)
    new_jid.RawAgent = 0
    new_jid.Device = 0
    return new_jid


def Jid2String(jid: JID) -> str:
    """Converts a Jabber Identifier (JID) to a string.

    :param jid: The Jabber Identifier (JID) to be converted.
    :type jid: JID
    :return: The string representation of the JID.
    :rtype: str
    """
    if jid.RawAgent > 0:
        return "%s.%s:%d@%s" % (jid.User, jid.RawAgent, jid.Device, jid.Server)
    elif jid.Device > 0:
        return "%s:%d@%s" % (jid.User, jid.Device, jid.Server)
    elif len(jid.User) > 0:
        return "%s@%s" % (jid.User, jid.Server)
    return jid.Server