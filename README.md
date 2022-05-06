# Setup

Instructions: https://twiki.cern.ch/twiki/bin/viewauth/CMS/EGMHLTRun3RecommendationForPAG

```bash
cmsrel CMSSW_12_0_1
cd CMSSW_12_0_1/src
cmsenv
git cms-addpkg HLTrigger/Configuration
# git cms-addpkg RecoEcal/EgammaClusterAlgos # For checking the PS double addition issue
git cms-merge-topic Sam-Harper:EGHLTCustomisation_1130pre4
# apply patch available here: https://github.com/cms-sw/cmssw/pull/35368/files
voms-proxy-init --voms cms --valid 168:00

cd /afs/cern.ch/user/r/rasharma/work/EGamma-POG/HLT_tasks/regression/GetRawFiles_TestPSEnergy/CMSSW_12_0_1/src
crab status -d crab_DoubleElectron_Pt1To300_WithNewCorr_HLT_PSAddComment/crab_crab_DoubleElectron_Pt1To300_WithNewCorr_HLT_PSAddComment

ls /eos/cms/store/group/phys_egamma/ec/Run3Studies/SCRegression/WithUpdatedCorrection_HLT_PSAddComment
```

# 5 April 2022

voms-proxy-init --voms cms --valid 168:00
source /cvmfs/cms.cern.ch/common/crab-setup.sh
crab status -d crab_DoubleElectron_Pt1To300_REAL_IC_NoPS/crab_crab_DoubleElectron_Pt1To300_REAL_IC_NoPS
crab status -d crab_DoubleElectron_Pt1To300_IDEAL_IC_NoPS/crab_crab_DoubleElectron_Pt1To300_IDEAL_IC_NoPS

Will save lumi files into output directory /afs/cern.ch/work/r/rasharma/EGamma-POG/HLT_tasks/regression/GetRawFiles/CMSSW_12_0_1/src/hlt_config_files/crab_DoubleElectron_Pt1To300_IDEAL_IC_NoPS/crab_crab_DoubleElectron_Pt1To300_IDEAL_IC_NoPS/results
Summary from jobs in status 'finished':
  Number of files processed: 8448
  Number of events read: 3783360
  Number of events written in EDM files: 3783360
  Number of events written in TFileService files: 0
  Number of events written in other type of files: 0
  Processed lumis written to processedLumis.json

Will save lumi files into output directory /afs/cern.ch/work/r/rasharma/EGamma-POG/HLT_tasks/regression/GetRawFiles/CMSSW_12_0_1/src/hlt_config_files/crab_DoubleElectron_Pt1To300_REAL_IC_NoPS/crab_crab_DoubleElectron_Pt1To300_REAL_IC_NoPS/results
Summary from jobs in status 'finished':
  Number of files processed: 8448
  Number of events read: 3783360
  Number of events written in EDM files: 3783360
  Number of events written in TFileService files: 0
  Number of events written in other type of files: 0
  Processed lumis written to processedLumis.json
Log file is /afs/cern.ch/work/r/rasharma/EGamma-POG/HLT_tasks/regression/GetRawFiles/CMSSW_12_0_1/src/hlt_config_files/crab_DoubleElectron_Pt1To300_REAL_IC_NoPS/crab_crab_DoubleElectron_Pt1To300_REAL_IC_NoPS/crab.log

#  Get hltConfig file

* Get the hlt config using the following two global tag
   * REAL:  `120X_mcRun3_2021_realistic_v6`
   * IDEAL: `120X_mcRun3_2021_realistic_v6_ECALIdealIC`

Command to get the hltConfig:

1. For real IC

   ```bash
   hltGetConfiguration /users/swmukher/egm_ele5_open/V16 --setup /dev/CMSSW_12_0_0/GRun/V6 --globaltag 120X_mcRun3_2021_realistic_v6 --input root://cms-xrd-global.cern.ch///store/mc/Run3Winter21DRMiniAOD/DoubleElectron_Pt-1To300-gun/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_112X_mcRun3_2021_realistic_v16-v3/120000/0019ce34-a026-4ec0-83a5-3094586bce59.root --mc --process MYHLT --prescale none --max-events 50 --eras Run3 --output none --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev > hlt_real.py
   ```

2. For ideal IC

   ```bash
   hltGetConfiguration /users/swmukher/egm_ele5_open/V16 --setup /dev/CMSSW_12_0_0/GRun/V6 --globaltag 120X_mcRun3_2021_realistic_v6_ECALIdealIC --input root://cms-xrd-global.cern.ch///store/mc/Run3Winter21DRMiniAOD/DoubleElectron_Pt-1To300-gun/GEN-SIM-DIGI-RAW/FlatPU0to80FEVT_112X_mcRun3_2021_realistic_v16-v3/120000/0019ce34-a026-4ec0-83a5-3094586bce59.root --mc --process MYHLT --prescale none --max-events 50 --eras Run3 --output none --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev  > hlt_ideal.py
   ```

# Crab Submit

```bash
cd $CMSSW_BASE/src
cmsenv
voms-proxy-init --voms cms --valid 168:00
source /cvmfs/cms.cern.ch/crab3/crab.sh
```

- To get the last hltconfig file used and the crab scripts you can checkout the github repo

```bash
cd $CMSSW_BASE/src
git clone git@github.com:ram1123/EGamma_hltConfig_Regression.git
cd EGamma_hltConfig_Regression
```

```bash
crab submit crab_config_withRegCorr.py
crab submit crab_config_withoutRegCorr.py
crab submit crab_config_ideal.py
```

# Info about the cmparison of CMSSW & Ntupliser variables:

* https://cmssdt.cern.ch/lxr/source/RecoEcal/EgammaClusterProducers/src/SCEnergyCorrectorProducer.cc

Append following lines in `hlt*.py` file:

```python
process.scEnergyCorr = cms.EDProducer( "SCEnergyCorrectorProducer",
    correctorCfg = cms.PSet(

    )
    inputSCs = cms.InputTag("superclsuters"),
    writeFeatures = True
)
```

# Logs of the path/command used:

```bash
crab status -d crab_DoubleElectron_Pt1To300_WithNewCorr_ge1Ele/crab_crab_DoubleElectron_Pt1To300_WithNewCorr_ge1Ele


crab kill -d crab_DoubleElectron_Pt1To300_WithNewCorr/crab_crab_DoubleElectron_Pt1To300_WithNewCorr
crab resubmit -d crab_DoubleElectron_Pt1To300_WithNewCorr/crab_crab_DoubleElectron_Pt1To300_WithNewCorr --maxmemory=4000
crab status -d crab_DoubleElectron_Pt1To300_WithNewCorr_v2/crab_crab_DoubleElectron_Pt1To300_WithNewCorr_v2

# crab status -d crab_DoubleElectron_Pt1To300_WithOldCorr/crab_crab_DoubleElectron_Pt1To300_WithOldCorr
crab status -d crab_DoubleElectron_Pt1To300_WithOldCorr_v2/crab_crab_DoubleElectron_Pt1To300_WithOldCorr_v2
crab resubmit -d crab_DoubleElectron_Pt1To300_WithOldCorr_v2/crab_crab_DoubleElectron_Pt1To300_WithOldCorr_v2

  Number of files processed: 15267
  Number of events read: 6836896
  Number of events written in EDM files: 6836896
  Number of events written in TFileService files: 0
  Number of events written in other type of files: 0

crab status -d crab_DoubleElectron_Pt1To300_IDEAL/crab_crab_DoubleElectron_Pt1To300_IDEAL
crab resubmit -d crab_DoubleElectron_Pt1To300_IDEAL/crab_crab_DoubleElectron_Pt1To300_IDEAL

  Number of files processed: 15297
  Number of events read: 6850336
  Number of events written in EDM files: 6850336
  Number of events written in TFileService files: 0
  Number of events written in other type of files: 0
```

# Other info


- https://github.com/ram1123/EGamma_pixel-track-validation/blob/65634a1dca63855cea9bfa7c4593b2ffcb3225ee/hlt_12_0_1_default.py
   ```
   hltGetConfiguration /users/swmukher/egm_ele5_open/V16 --setup /dev/CMSSW_12_0_0/GRun/V6 --globaltag auto:phase1_2021_realistic --input root://cms-xrd-global.cern.ch///store/mc/Run3Winter21DRMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/270024/a5adba3d-a6b2-46c0-b690-04e9462fad11.root --mc --process MYHLT --prescale none --max-events 50 --eras Run3 --output none --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev > test_hlt.py
   ```
- https://mattermost.web.cern.ch/cmseg/pl/7dt6srgmttnqdkug95by8n7f9a

