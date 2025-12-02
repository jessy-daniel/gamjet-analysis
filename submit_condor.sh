#!/bin/bash
IOV=$1
VERSION=$2

source /cvmfs/cms.cern.ch/cmsset_default.sh
export XRD_RUNFORKHANDLER=1

root -l -b -q "mk_GamHistosFill.C(\"${IOV}\",\"${VERSION}\")"
