# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""
Retrieve files for use in examples
"""
from pkg_resources import resource_filename


def get_fsLR_flatmap_gifti():
    return {
        'left': resource_filename(
            'hyve_examples',
            'data/S1200.L.flat.32k_fs_LR.surf.gii'
        ),
        'right': resource_filename(
            'hyve_examples',
            'data/S1200.R.flat.32k_fs_LR.surf.gii'
        ),
    }


def get_glasser360_gifti():
    return {
        'left': resource_filename(
            'hyve_examples',
            'data/Glasser_2016.32k.L.label.gii'
        ),
        'right': resource_filename(
            'hyve_examples',
            'data/Glasser_2016.32k.R.label.gii'
        ),
    }


def get_gordon333_gifti():
    return {
        'left': resource_filename(
            'hyve_examples',
            'data/Gordon.32k.L.label.gii'
        ),
        'right': resource_filename(
            'hyve_examples',
            'data/Gordon.32k.R.label.gii'
        ),
    }


def get_mscWard400_nifti():
    return resource_filename(
        'hyve_examples',
        'data/MSC_ward400_parcellation.nii.gz'
    )


def get_myconnectomeWard400_nifti():
    return resource_filename(
        'hyve_examples',
        'data/myconnectome_ward400_parcellation.nii.gz'
    )


def get_null400_cifti():
    return resource_filename(
        'hyve_examples',
        'data/nullexample.nii'
    )


def get_null400_gifti():
    return {
        'left': resource_filename(
            'hyve_examples',
            'data/nullexample_L.gii'
        ),
        'right': resource_filename(
            'hyve_examples',
            'data/nullexample_R.gii'
        ),
    }


def get_pain_thresh_nifti():
    return resource_filename(
        'hyve_examples',
        'data/pain_thresh_cFWE05.nii.gz'
    )


def get_schaefer400_cifti():
    return resource_filename(
        'hyve_examples',
        'data/desc-schaefer_res-0400_atlas.nii'
    )


def get_schaefer400_synthetic_conmat():
    return resource_filename(
        'hyve_examples',
        'data/atlas-schaefer400_desc-synth_cov.tsv'
    )
