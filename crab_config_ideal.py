from CRABClient.UserUtilities import config
config = config()

# config.section_('General')
config.General.requestName = 'crab_DoubleElectron_Pt1To300_IDEAL'
config.General.workArea = 'crab_DoubleElectron_Pt1To300_IDEAL'
config.General.transferOutputs = True
config.General.transferLogs = True

# config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'hlt_ideal.py'
config.JobType.numCores = 4

# config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 4000

# config.JobType.numCores = 8
config.Data.inputDataset ='/DoubleElectron_Pt-1To300-gun/Run3Winter21DRMiniAOD-FlatPU0to80FEVT_112X_mcRun3_2021_realistic_v16-v3/GEN-SIM-DIGI-RAW'
# config.Data.splitting = 'Automatic'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10

config.Data.outLFNDirBase = '/store/group/phys_egamma/Run3Studies/SCRegression/IDEAL_IC'
config.Data.publication = False
config.Site.storageSite = 'T2_CH_CERN'
