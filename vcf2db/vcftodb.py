#! /usr/bin/env python
from mongoengine import connect
from mongoengine import NotUniqueError
from mongoengine import OperationError

from models import CallSet
from models import Reference
from models import Variant
from models import VariantSet
from models import Call
connect('atlas')
import vcf
import os
import csv
import argparse


parser = argparse.ArgumentParser(description='Parse VCF and upload variants to DB')
parser.add_argument('vcf', metavar='vcf', type=str, help='a vcf file')
args = parser.parse_args()
def is_record_valid(record):
	valid = True
	for sample in record.samples:
		if sample["GT"] is None:
			valid = False
	return valid

vcf_reader = vcf.Reader(open(args.vcf, 'r'))
assert len(vcf_reader.samples) == 1

try:
	callset = CallSet.create(name = vcf_reader.samples[0], sample_id = vcf_reader.samples[0])
except NotUniqueError:
	callset = CallSet.objects.get(name = vcf_reader.samples[0])

try:
	variant_set = VariantSet.create(name = os.path.basename(args.vcf))
except NotUniqueError:
	variant_set = VariantSet.objects.get(name = os.path.basename(args.vcf))

try:
	reference = Reference.create(name = "R00000022")
except NotUniqueError:
	reference = Reference.objects.get(name = "R00000022")

for record in vcf_reader:
	if not record.FILTER and record.is_snp and is_record_valid(record):
		for sample in record.samples:
			try:
				v = Variant.create(variant_set = variant_set, start = record.POS, reference_bases = record.REF,
								 	alternate_bases = [str(a) for a in record.ALT],
								 	reference = reference)
				Call.create(variant = v, call_set = callset, genotype = sample['GT'], genotype_likelihood = 1)
			except OperationError:
				pass

