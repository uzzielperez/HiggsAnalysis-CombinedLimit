#! /bin/env python
''' Run limits for ADD diphoton analysis'''
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--blind', default=False, help="Run with blinded data observation")
parser.add_argument('-c', '--cards', action='store_true', help="Create full datacards")
parser.add_argument('-d', '--directory', default="../../diphoton-analysis/Tools/", help="Datacard directory.")
args = parser.parse_args()

blind_data = args.blind
create_cards = args.cards
relative_path = args.directory

#UnparToGG_Spin0_du1p1_LambdaU-8000_TuneCP2_13TeV_pythia8_2017_BE.dat

LambdaU_values = {'Spin0-du1p1' : {4000, 8000, 10000},
                  'Spin0-du1p5' : {2000, 2500, 3500},
                  'Spin0-du1p9' : {2000, 2500, 3500},
                  'Spin2-du1p1' : {2000, 2500, 3000},
                  'Spin2-du1p5' : {2000, 2500, 3000},
                  'Spin2-du1p9' : {2000, 2500, 3500}}

dimensions = []
dimensions.extend(['Spin0-du1p1', 'Spin0-du1p5', 'Spin0-du1p9', 'Spin2-du1p1', 'Spin2-du1p5', 'Spin2-du1p9'])
extraOptions = "--rMax 2"
if blind_data:
    extraOptions += " --run blind"
else:
    extraOptions += ' --text2workspace "--max-bin 20"'

regions = {"BB", "BE"}
#years = {"2016", "2017", "2018"}
years = {"2017"}
for dimension in dimensions:
    for LambdaU_val in LambdaU_values[dimension]:
        name = 'UnparToGG_' + dimension + '_LambdaU-' + str(LambdaU_val) + '_TuneCP2_13TeV_pythia8'
        if not blind_data:
            name_no_ms += "_lowmass"
        outputdatacard = relative_path + "datacards/" + name + ".dat"
        if create_cards:
            fulldatacardcmd = "combineCards.py "
            # combine datacards
            for year in years:
                for region in regions:
                    fulldatacardcmd += region + "_" + year + "=" + relative_path + "datacards/" + name + "_" + year + "_" + region + ".dat "
            fulldatacardcmd += " > " + outputdatacard
            print fulldatacardcmd
            # output combined datacard
            os.system(fulldatacardcmd)
            # hack to avoid bug in combineCards.py
            cmd = "sed -i 's|datacards/datacards|datacards|g' " + outputdatacard
            print cmd
            os.system(cmd)
        cmd = 'combine -M AsymptoticLimits ' + outputdatacard + ' ' + extraOptions + ' -n ' + name_no_ms + ' -m ' + str(ms_value)
        print cmd
        os.system(cmd)
