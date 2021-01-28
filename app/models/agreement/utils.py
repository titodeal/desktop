from .agreement import Agreement

def from_dicts_to_agreements(user_id, dicts):
    agreements = []
    for d in dicts:
        agreement = Agreement()
        agreement.id = d.get('agreement_id')
        agreement.owner_id = d.get('owner_id')
        agreement.owner_login = d.get('owner_login')
        agreement.contractor_id = d.get('contractor_id')
        agreement.contractor_login = d.get('contractor_login')
        agreement.conditions = d.get('conditions')
        agreement.expiration = d.get('expiration')
        agreement.accepted = d.get('accepted')
        if user_id == agreement.owner_id:
            type_ = "employer"
        elif user_id == agreement.contractor_id:
            type_ = "contractor"
        else:
            print("=> Undefind user relatively agreement: "
                  f"user_id: {user_id}"
                  f"agreement_id: {agreement.agreement_id}")
            type_ = None
        agreement.type = type_
        agreements.append(agreement)
    return agreements
