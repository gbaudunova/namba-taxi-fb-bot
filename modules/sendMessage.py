from .need_parameters import need_phone


def decide_message(sender_id, message_text, data):
    need_phone(sender_id, data)