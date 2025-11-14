#! /usr/bin/python
import os
import argparse

version = "tot_23_pnetreg_ok"
parser = argparse.ArgumentParser(description="Run all IOVs")

# The user can pass the IOV list, version, max number of files as an argument
parser.add_argument("-i", '--IOV_list', default="all")
parser.add_argument("-v", "--version", default=version)
parser.add_argument("-f", "--force", default=False, action="store_true")
args = parser.parse_args()

version = args.version

# How to merge files into a bigger one. First one is the target
IOV_list_of_lists = [
    #    ['2016BCDEF','2016BCD','2016EF'],
    #    ['2017BCDEF','2017B','2017C','2017D','2017E','2017F'],
    #    ['2018ABCD','2018A1','2018A2','2018B','2018C',
    #     '2018D1','2018D2','2018D3','2018D4'],
    #    ['Run2','2016BCDEF','2016FGH','2017BCDEF','2018ABCD']
    #    ['2022CDE','2022C','2022D','2022E'],
    #    ['2023Cv4D','2023Cv4','2023D'],
    #    ['Run3','2022C','2022D','2022E','2022F','2022G',
    #     '2023Cv123','2023Cv4','2023D']
    # ['Run3Summer23', '2023Cv123', '2023Cv4','2023D']
    #    ['Run3', '2023Cv123', '2023Cv4','2023D']
    #
    #   ['2022CD','2022C','2022D'],
    #   ['2022FG','2022F','2022G'],
       ['2024Only','2024B','2024C','2024D','2024E','2024F','2024G','2024H','2024I'],
]
MC_list_of_lists = [
    #    ['Run2P8','2016P8','2016APVP8','2017P8','2018P8'],
    #    ['Run2QCD','2016QCD','2016QCDAPV','2017QCD','2018QCD'],
    #    ['Run3P8','2022P8','2022EEP8']
    # ['Run3Summer23', '2023P8', '2023P8-BPix'] # !! does not make sense to merge these together? - double check!!
    # [
    #     "Summer23MGBPix_1",
    #     "Summer23MGBPix_2",
    #     "Summer23MGBPix_3",
    #     "Summer23MGBPix_4",
    # ],
    # [
    #     "Summer23MG_1",
    #     "Summer23MG_2",
    #     "Summer23MG_3",
    #     "Summer23MG_4",
    #     "Summer23MG_5",
    #     "Summer23MG_6",
    # ],
    #
    [
        file.replace(".txt", "").replace("mcFiles_", "")
        for file in os.listdir("input_files/")
        if "Winter24MG_" in file and "all" not in file
    ],
    [
        file.replace(".txt", "").replace("mcFiles_", "")
        for file in os.listdir("input_files/")
        if "2024P8" in file and "all" not in file
    ],
    [
        file.replace(".txt", "").replace("mcFiles_", "")
        for file in os.listdir("input_files/")
        if "Summer23MG_" in file and "all" not in file
    ],
    [
        file.replace(".txt", "").replace("mcFiles_", "")
        for file in os.listdir("input_files/")
        if "Summer23MGBPix_" in file and "all" not in file
    ],
    [
        file.replace(".txt", "").replace("mcFiles_", "")
        for file in os.listdir("input_files/")
        if "2023P8" in file and "BPix" not in file and "all" not in file
    ],
    [
        file.replace(".txt", "").replace("mcFiles_", "")
        for file in os.listdir("input_files/")
        if "2023P8-BPix" in file and "all" not in file
    ],

    [
        file.replace(".txt", "").replace("mcFiles_", "")
        for file in os.listdir("input_files/")
        if "Summer22MG_" in file and "all" not in file
    ],
    [
        file.replace(".txt", "").replace("mcFiles_", "")
        for file in os.listdir("input_files/")
        if "Summer22EEMG_" in file and "all" not in file
    ],
    [
        file.replace(".txt", "").replace("mcFiles_", "")
        for file in os.listdir("input_files/")
        if "2022P8" in file and "BPix" not in file and "all" not in file
    ],
    [
        file.replace(".txt", "").replace("mcFiles_", "")
        for file in os.listdir("input_files/")
        if "2022EEP8" in file and "all" not in file
    ],
]


IOV_list_of_lists_year = IOV_list_of_lists
MC_list_of_lists_year = MC_list_of_lists
for year in ["22", "23", "24"]:
    if year in args.IOV_list:
        print(year)
        IOV_list_of_lists_year=[]
        MC_list_of_lists_year=[]
        for i, iov_list in enumerate(IOV_list_of_lists):
            print(iov_list, i)
            if year in iov_list[0]:
                IOV_list_of_lists_year.append(iov_list)
        for i, iov_list in enumerate(MC_list_of_lists):
            print(iov_list, i)

            if year in iov_list[0]:
                MC_list_of_lists_year.append(iov_list)


IOV_list_of_lists = IOV_list_of_lists_year
MC_list_of_lists = MC_list_of_lists_year

print("IOV_list_of_lists ", MC_list_of_lists_year)
print("MC_list_of_lists", MC_list_of_lists)

suffix_dict = {
    "Summer24MG": "2024QCD",
    "2024P8": "2024P8",
    "Summer23MG": "2023QCD",
    "Summer23MGBPix": "2023QCD-BPix",
    "2023P8": "2023P8",
    "2023P8-BPix": "2023P8-BPix",
    "Summer22MG": "2022QCD",
    "Summer22EEMG": "2022EEQCD",
    "2022P8": "2022P8",
    "2022EEP8": "2022EEP8",
}


os.system("ls rootfiles/" + version + "/GamHistosFill_data_*_" + version + ".root")
for IOV_list in IOV_list_of_lists:
    command = (
        "hadd rootfiles/"
        + version
        + "/GamHistosFill_data_"
        + IOV_list[0]
        + "_"
        + version
        + ".root "
        + ("-f " if args.force else "")
    )
    for iov in IOV_list[1:]:
        command = (
            command
            + " rootfiles/"
            + version
            + "/GamHistosFill_data_"
            + iov
            + "_"
            + version
            + ".root "
        )
    print('"' + command + '"...')
    os.system(command)

os.system("ls rootfiles/" + version + "/GamHistosFill_mc_*_" + version + ".root")
for MC_list in MC_list_of_lists:
    suffix = suffix_dict[MC_list[0].split("_")[0]]
    command = (
        ("hadd rootfiles/" + version + "/GamHistosFill_mc_" + suffix)
        + "_"
        + version
        + ".root "
        + ("-f " if args.force else "")
    )
    print("\n", command)
    for mc in MC_list:
        command = (
            command
            + " rootfiles/"
            + version
            + "/GamHistosFill_mc_"
            + mc
            + "_"
            + version
            + ".root "
        )
    print('"' + command + '"...')
    os.system(command)