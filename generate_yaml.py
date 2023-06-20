from pathlib import Path

yaml_content = f'''
train: train/images
val: val/images
test: test/images

names: ['circle']
    '''

with Path('data.yaml').open('w') as f:
    f.write(yaml_content)