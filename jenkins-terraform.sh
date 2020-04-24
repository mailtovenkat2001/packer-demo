#!/bin/bash
set -ex

AWS_REGION="eu-west-2"

ARTIFACT=`packer build -machine-readable packer-demo.json | awk -F, '$0 ~/artifact,0,id/ {print $6}'`
echo "packer output:"
cat packer-demo.json

