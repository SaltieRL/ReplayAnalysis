# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/team.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..api import player_id_pb2
from ..api.stats import team_stats_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/team.proto',
  package='api',
  serialized_pb=_b('\n\x0e\x61pi/team.proto\x12\x03\x61pi\x1a\x13\x61pi/player_id.proto\x1a\x1a\x61pi/stats/team_stats.proto\"~\n\x04Team\x12!\n\nplayer_ids\x18\x01 \x03(\x0b\x32\r.api.PlayerId\x12\r\n\x05score\x18\x02 \x01(\x05\x12\x11\n\tis_orange\x18\x03 \x01(\x08\x12\x0c\n\x04name\x18\x04 \x01(\t\x12#\n\x05stats\x18\x05 \x01(\x0b\x32\x14.api.stats.TeamStats')
  ,
  dependencies=[player_id_pb2.DESCRIPTOR,team_stats_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TEAM = _descriptor.Descriptor(
  name='Team',
  full_name='api.Team',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_ids', full_name='api.Team.player_ids', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='api.Team.score', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_orange', full_name='api.Team.is_orange', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='api.Team.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stats', full_name='api.Team.stats', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=198,
)

_TEAM.fields_by_name['player_ids'].message_type = player_id_pb2._PLAYERID
_TEAM.fields_by_name['stats'].message_type = team_stats_pb2._TEAMSTATS
DESCRIPTOR.message_types_by_name['Team'] = _TEAM

Team = _reflection.GeneratedProtocolMessageType('Team', (_message.Message,), dict(
  DESCRIPTOR = _TEAM,
  __module__ = 'api.team_pb2'
  # @@protoc_insertion_point(class_scope:api.Team)
  ))
_sym_db.RegisterMessage(Team)


# @@protoc_insertion_point(module_scope)