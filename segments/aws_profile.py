import os

def add_aws_profile_segment(powerline):
  env = os.getenv('AWS_CONFIG_FILE')
    if env is None:
        return

  default_profile = os.getenv('AWS_DEFAULT_PROFILE') or 'default'
  powerline.append(' %s ' % default_profile )
