from boto3.session import Session


def kms_client(
        region: str = None,
        profile: str = None,
        session: Session = None,
        client = None,):
    """
    returns a kms session
    """
    if client:
        return client
    if session:
        return session.client('kms')
    session = Session(region_name=region, profile_name=profile)
    return session.client('kms')
