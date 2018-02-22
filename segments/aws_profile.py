import os

def add_aws_profile_segment(powerline):
    aws_profile = os.getenv('AWS_PROFILE') or 'default'
    powerline.append(u'\u2601' + ' %s ' % aws_profile, Color.SSH_FG, Color.SSH_BG )
