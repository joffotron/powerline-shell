import os

def add_aws_profile_segment(powerline):
    env = os.getenv('AWS_CONFIG_FILE')
    if env is None:
        return

    aws_profile = os.getenv('AWS_DEFAULT_PROFILE') or 'default'
    powerline.append(u'\u2601' + ' %s ' % aws_profile, Color.SSH_FG, Color.SSH_BG )
