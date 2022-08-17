_base_ = [
    '/data/Code/timformer/configs/segformer_4_attention.py',
    '/data/Code/timformer/configs/cityscapes_192x192.py',
    '/data/Code/timformer/configs/default_runtime.py', 
    '/data/Code/timformer/configs/schedule_att_extra.py'
]
checkpoint = '/data/Code/timformer/transformed_keys.pth'  # noqa

model = dict(
    backbone=dict(init_cfg=dict(type='Pretrained', checkpoint=checkpoint)),
    test_cfg=dict(mode='slide', crop_size=(192, 192), stride=(192, 192)))
    # test_cfg=dict(mode='slide', crop_size=(1024, 1024), stride=(768, 768)))

# optimizer
optimizer = dict(
    _delete_=True,
    type='AdamW',
    lr=0.00001,
    betas=(0.9, 0.999),
    weight_decay=0.01,
    paramwise_cfg=dict(
        custom_keys={
            'pos_block': dict(decay_mult=0.),
            'norm': dict(decay_mult=0.),
            'head': dict(lr_mult=10.)
        }))

lr_config = dict(
    _delete_=True,
    policy='LinearAnnealing',
    warmup=None,
    min_lr_ratio=1.0,
    by_epoch=False)

data = dict(samples_per_gpu=8, workers_per_gpu=8)