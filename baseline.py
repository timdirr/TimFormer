_base_ = [
    'configs/segformer_mit-b0.py',
    'configs/cityscapes_192x192.py',
    'configs/default_runtime.py', 'configs/schedule_640k.py'
]

checkpoint = 'pretrain/mit_b0_20220624-7e0fe6dd.pth'  # noqa

model = dict(
    backbone=dict(init_cfg=dict(type='Pretrained', checkpoint=checkpoint)),
    test_cfg=dict(mode='slide', crop_size=(512, 512), stride=(384, 384)))
    # test_cfg=dict(mode='slide', crop_size=(1024, 1024), stride=(768, 768)))

# optimizer
optimizer = dict(
    _delete_=True,
    type='AdamW',
    lr=0.00006,
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
    policy='poly',
    warmup='linear',
    warmup_iters=1500,
    warmup_ratio=1e-6,
    power=1.0,
    min_lr=0.0,
    by_epoch=False)

data = dict(samples_per_gpu=1, workers_per_gpu=1)