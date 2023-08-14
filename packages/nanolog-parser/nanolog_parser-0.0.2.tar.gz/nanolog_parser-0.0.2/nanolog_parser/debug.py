import re
from nanolog_parser.src.messages import *
from nanolog_parser.src.message_factory import MessageFactory
from tests.test_parser import testconfirmation_solicitor_flush_message
from tests.test_sql_many_to_many import *
from tests.test_parser import *
from tests.test_sql import *
from tests.test_store_sql import *

test_store_publish_message()
# import json

# test_processed_blocks_message()

# test_store_confirm_ack_message()
# test_store_filename_in_message()
# test_store_nodeprocessconfirmed_message()
# test_store_flush_message()
# test_confirm_ack_message_parse()
# testconfirmation_solicitor_flush_message()

# def extract_message(line):
#     # Using a regular expression to find the message part
#     matches = re.findall(r'message=\{(.*)\}', line)
#     match = "{" + matches[0] + "}" if matches else None
#     return match

# def convert_to_json(string):
#     # Replace = with :
#     string = re.sub(r'\s*=\s*', ':', string)
#     # Replace keys with "key". Lookbehind and lookahead are used to avoid replacing substrings within double quotes.
#     string = re.sub(r'(?<=\{|,|\[)\s*([a-zA-Z0-9_]+)\s*(?=:)', r'"\1"', string)
#     return string

# # Test the function
# line = '[2023-07-15 14:19:44.867] [network] [trace] "message_received" message={ header={ type="keepalive", network="live", network_int=21059, version=19, version_min=18, version_max=19, extensions=0 }, peers=[ "[::ffff:94.130.135.50]:7075", "[::]:0", "[::ffff:174.138.4.198]:7075", "[::ffff:54.77.3.59]:7075", "[::ffff:139.180.168.194]:7075", "[::ffff:98.35.209.116]:7075", "[::ffff:154.26.158.112]:7075", "[::ffff:13.213.221.153]:7075" ] }'
# line1 = '[2023-07-15 14:19:44.805] [network] [trace] "message_received" message={ header={ type="confirm_req", network="live", network_int=21059, version=19, version_min=18, version_max=19, extensions=4352 }, block=null, roots=[ { root="3903175F5E19C5D772319EC9EB2B8BC4728F669EA4F7DD22BB6699D0A8CA455D", hash="54108799F7FBC6ABCCEF37D7761B019F3FA86DDE8F094AB57BDA1CFE588F3FEA" } ] }'
# message = extract_message(line)
# message1 = extract_message(line1)
# print(message)

# string1 = convert_to_json(
#     '{ block=10, header={ type="keepalive"} ,roots: [ { key1: "value1", key2: "value" } ] }'
# )
# string2 = convert_to_json(
#     '{ block=null, peers=[ "[::ffff:94.130.135.50]:7075", "[::]:0" ] }')

# print(string1, "\n", string2)
# json_string = json.loads(string1)
# json_string = json.loads(string2)

# message_res = convert_to_json(message)
# message_res1 = convert_to_json(message1)

# json_string = json.loads(message_res)
# print(json_string)
# json_string = json.loads(message_res1)
# print(json_string)
# test_store_flush_message()

# test_store_flush_message()
# test_store_confirm_ack_message()
# test_store_message_confirm_req()

# #regex = r'\[blockprocessor\] \[\w+\]'
# regex = r'\[(confirmation_solicitor)\] \[\w+\]'
# #regex = r'"message_received" message={ header={ type="(.*?)",'
# #line = '[2023-07-20 08:20:51.401] [election] [trace] "generate_vote_normal" root="686C685B1CEF83843D6A5AD85EE685A6F6C394CB7C2E3B2B611CFA2B4DA566A3", hash="3A8867A4E61F181FC3B43B8E6BE5CBC860E35E6C7D3204EBB3557B2B6A514423"'
# #line = '[2023-07-15 14:19:48.287] [blockprocessor] [trace] "block_processed" result="gap_previous", block={ type="state", hash="160F1EF61CFC73D2DBF2B249AA38B9965BF441EEF4312E9A89BDB58A22CF32FE", account="EBB66C545B0ED5F248256E281E13B09829518435C4C05E705BB70F2DF625E060", previous="9C490F4525EA5E6EAA4E76869B7073D5BD452D11B2CEB6CC34353856519D2075", representative="F11A22A0340C7931C6C6288280A0F6ACF8F052BED2C929493883388B1776ADA2", balance="00000000000000000000000000000000", link="F11A22A0340C7931C6C6288280A0F6ACF8F052BED2C929493883388B1776ADA2", signature="E7B0E3315C52085F4EB4C00462B3394983B84216860370B50DF85A17664CEB58ED76F0EA2699BBFFD15BB84578681C4A5E0FCA67685BB882F80C329C5C818F0D", work=10530317739669255306 }, forced=false'
# line = '[2023-07-24 08:24:57.000] [confirmation_solicitor] [trace] "flush" channel="[::ffff:192.168.96.6]:17075", confirm_req={ header={ type="confirm_req", network="test", network_int=21080, version=19, version_min=18, version_max=19, extensions=28928 }, block=null, roots=[ { root="6D42FB40A4DEDBD2A38CB18565E0AA4D17F1B81036CEB1A53D4DB8B4309748AA", hash="F4E0F29524503FC2C794F90BF83B91F20834F331B776800A0DA350507B08CC4E" }, { root="C8084749BBD422A8C946E934FDE0702471F850B817D34450BB0FE5E574C9E56E", hash="5583791E4DE40CCA877E394F471E605C494DB038BD5F2FFB5AB41FE709F463E9" }, { root="18136735ACAECDC6AC775F3D739E5A10C5101C132F990EB6F338F2F1493ACD5B", hash="1DD6232FA752C96A6F20AF451003B38EAA4799AB2A1837222E21C6EAF2C87ECB" }, { root="122A088010D2B6BC88E9658EE06C893DC02E3504B400D6486F9F13AC888698BB", hash="36687C628781978911AEC91FE95C249161BA11CCC804A4933751BE0B10CF780D" }, { root="260394945DACEDDF531AE01796278AEDD6C26A68FC56BAB05797EE5746B73D1C", hash="0A4BA7AB62B2C96987377860050687C7FCBD2DC0E0D24986EF128F928C655683" }, { root="3DC77E847676662685995955C8148F8B335624AF549863C108D5FE3A9AA38786", hash="E692A698B99E1136369B62401F4BB7B16098D7A0542DA7EF2438905C3F1E4B60" }, { root="4CB6B82860EF803C5CD77B18C3ECC9C2F414E28E1FDB6351DC165BA16D5D76EA", hash="A295A8E032EE234F1996311768712C86061322304F87F752A62D0B91717455B8" } ] }'
# #line = '[2023-07-15 14:19:44.805] [network] [trace] "message_received" message={ header={ type="confirm_req", network="live", network_int=21059, version=19, version_min=18, version_max=19, extensions=4352 }, block=null, roots=[ { root="3903175F5E19C5D772319EC9EB2B8BC4728F669EA4F7DD22BB6699D0A8CA455D", hash="54108799F7FBC6ABCCEF37D7761B019F3FA86DDE8F094AB57BDA1CFE588F3FEA" } ] }'
# message_type_match = re.search(regex, line)

# print(message_type_match)

# MESSAGE_TYPES = {"confirmation_solicitor": FlushMessage}
# #MESSAGE_TYPES = {"unknown": BlockProcessorMessage}
# # MESSAGE_TYPES = {    "confirm_req": ConfirmReqMessage,}

# message_type = message_type_match.group(1) if message_type_match else "unknown"
# message_class = MESSAGE_TYPES.get(message_type)
# if message_class is None:
#     raise ValueError(f"Unknown message type {message_type}.")

# message = MessageFactory.create_message(line)

# # assert isinstance(message, FlushMessage)
# # assert message.channel == "[::ffff:192.168.96.6]:17075"


def extract_message(line, variable="message"):
    # Using a regular expression to find the message part
    regex = f'{variable}={{(.*)}}'
    matches = re.findall(regex, line)
    match = "{" + matches[0] + "}" if matches else None
    return match


def fix_json_keys(string):
    # Replace = with :
    string = re.sub(r'\s*=\s*', ':', string)
    # Replace keys with "key". Lookbehind and lookahead are used to avoid replacing substrings within double quotes.
    string = re.sub(r'(?<=\{|,|\[)\s*([a-zA-Z0-9_]+)\s*(?=:)', r'"\1"', string)
    return string


def convert_message_to_json(log_message, key):
    log_message = extract_message(log_message, key)
    message_content = fix_json_keys(log_message)
    return json.loads(message_content)


line = '[2023-07-28 10:44:56.608] [active_transactions] [trace] "active_started" election={ root="0BF3D62DAEE43808555F6215A39EC7694120167F08FDDFD4C5E3C974107171A20BF3D62DAEE43808555F6215A39EC7694120167F08FDDFD4C5E3C974107171A2", behaviour="normal", state="passive", confirmed=false, winner="A4BC66235AB483E0F29D81EDBB062172B0C289825CDB827D590520CE06173153", tally_amount="100000000000000000000000000000000000000", final_tally_amount="0", blocks=[ { type="state", hash="A4BC66235AB483E0F29D81EDBB062172B0C289825CDB827D590520CE06173153", sideband={ successor="0000000000000000000000000000000000000000000000000000000000000000", account="0000000000000000000000000000000000000000000000000000000000000000", balance="00000000000000000000000000000000", height=2, timestamp=1690541096, source_epoch="epoch_begin", details={ epoch="epoch_2", is_send=false, is_receive=false, is_epoch=false } }, account="02A3D38D7B9A561BF61BC0D5D2C2C4F560A63B6AE8C04BEEF1E369A35D731995", previous="0BF3D62DAEE43808555F6215A39EC7694120167F08FDDFD4C5E3C974107171A2", representative="39870A8DC9C5D73DB1E53CBB69D5A4A59AAC46C579CB009D2D31C0BFD8058835", balance="00000000000000000000000000000001", link="0000000000000000000000000000000000000000000000000000000000000000", signature="F3B6E3E55A375FE1BDB8028A459EDE8864B18B91290DD38615E96BF5988AD4105C0D53B0A194AA0E70FAC8E9CCC41D015A643D3442B9A493EFE0C44CB0A7B303", work=10548966438472085574 } ], votes=[ { account="nano_3sz3bi6mpeg5jipr1up3hotxde6gxum8jotr55rzbu9run8e3wxjq1rod9a6", time=5510123611640189, timestamp=1690541095808, hash="A4BC66235AB483E0F29D81EDBB062172B0C289825CDB827D590520CE06173153" }, { account="nano_3z93fykzixk7uoswh8fmx7ezefdo7d78xy8sykarpf7mtqi1w4tpg7ejn18h", time=5510123611634459, timestamp=1690541093888, hash="A4BC66235AB483E0F29D81EDBB062172B0C289825CDB827D590520CE06173153" }, { account="nano_1qybcjn5tuyxz17fn73hkem4xfuip6t9pqjrh1bewnk7khm9qgnuzoh1gz8c", time=5510123611631209, timestamp=0, hash="A4BC66235AB483E0F29D81EDBB062172B0C289825CDB827D590520CE06173153" } ], tally=[ { amount="100000000000000000000000000000000000000", hash="A4BC66235AB483E0F29D81EDBB062172B0C289825CDB827D590520CE06173153" } ] }'

message_dict = convert_message_to_json(line, "election")
print(message_dict)
