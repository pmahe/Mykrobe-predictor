from setuptools import setup


setup(
    name='mykrobe',
    version='0.3.0.2',
    packages=[
        'mykrobe',
        'mykrobe.cmds',
        'mykrobe.pheno',
        'mykrobe.metagenomics'],
    license='https://github.com/iqbal-lab/Mykrobe-predictor/blob/master/LICENSE',
    url='https://github.com/iqbal-lab/Mykrobe-predictor',
    description='.',
    author='Phelim Bradley, Zamin Iqbal',
    author_email='wave@phel.im, zam@well.ox.ac.uk',
    install_requires=["mykatlas"],
    entry_points={
            'console_scripts': [
                'mykrobe = mykrobe.mykrobe_predictor:main'
            ]},
    package_data={
        'mykrobe': [
            'data/predict/*/*',
            'data/predict/taxon_coverage_threshold.json',
            'data/phylo/*',
            'data/panels/tb-species-160227.fasta.gz',
            'data/panels/staph-species-160227.fasta.gz',
            'data/panels/tb-amr-walker_2015.fasta.gz',
            'data/panels/tb-amr-bradley_2015.fasta.gz',
            'data/panels/staph-amr-bradley_2015.fasta.gz',
        ]})
