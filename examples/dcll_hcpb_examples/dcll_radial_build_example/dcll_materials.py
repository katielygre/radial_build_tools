import openmc
import json
import material_db_tools as mdbt


with open("PureFusionMaterials_libv1.json", "r") as pure_materials_json:
    pure_materials = json.load(pure_materials_json)
materials = {}
material_dict = {
    "sol":{"composition":{"Void": 1.0}, "citation":"DavisFusEngDes_2018"},
    "fw_armor":{"composition":{"W": 1.0} , "density_factor":0.91, "citation":"ZhouEUDEMOHCPB_2023"},
    "fw": {"composition":{"MF82H":0.34 , "HeNIST":0.66}, "citation":"ZhouEUDEMOHCPB_2023"},
    "be_muliplier":{"composition":{"Be": 1.0}, "citation":"DavisFusEngDes_2018"},
    "breeder": {"composition":{"Pb157Li90":0.737, "SiC":0.039, "HeNIST":0.149, "MF82H":0.075}, "citation":"ZhouEUDEMOHCPB_2023"}, #fix this
    "bw": {"composition":{"MF82H":0.8 , "HeNIST":0.2}, "citation":"DavisFusEngDes_2018"},
    "manifold": {"composition":{"MF82H":0.3 , "HeNIST":0.7}, "citation":"DavisFusEngDes_2018"},
    "hts_front_plate": {"composition":{"HeNIST":0.2,"MF82H":0.28, "BMF82H":0.52},"citation":"DavisFusEngDes_2018"},
    "hts": {"composition":{"HeNIST":0.2,"MF82H":0.28, "BMF82H":0.52},"citation":"DavisFusEngDes_2018"},
    "hts_back_plate": {"composition":{"HeNIST":0.2,"MF82H":0.28, "BMF82H":0.52},"citation":"DavisFusEngDes_2018"},
    "gap_1": {"composition":{"Void": 1.0}, "citation":"DavisFusEngDes_2018"},
    "vv_front_plate": {"composition":{"SS316L": 1.0}, "citation":"DavisFusEngDes_2018"},
    "vv_fill":{"composition":{"HeNIST":0.4, "Cr3FS" :0.6}, "citation":"DavisFusEngDes_2018"},
    "vv_back_plate":{"composition":{"SS316LN": 1.0}, "citation":"DavisFusEngDes_2018"},
    "gap_2": {"composition":{"AirSTP": 1.0}, "citation":"ZhouEUDEMOHCPB_2023"},
    "lts_front_plate": {"composition":{"Cr3FS": 0.39, "BMF82H": 0.29, "Water": 0.32}, "citation":"DavisFusEngDes_2018"},
    "lts": {"composition":{"Cr3FS": 0.39, "BMF82H": 0.29, "Water": 0.32}, "citation":"DavisFusEngDes_2018"},
    "lts_back_plate": {"composition":{"Cr3FS": 0.39, "BMF82H": 0.29, "Water": 0.32}, "citation":"DavisFusEngDes_2018"},
    "thermal_insulator":{"composition":{"AirSTP": 1.0}, "citation":"ZhouEUDEMOHCPB_2023"},
    "coil_pack_front_plate": {"composition":{"SS316LN":1.0}, "citation":"DavisFusEngDes_2018"},
    "coil_pack": {"composition":{"SS316LN":1.0}, "citation":"DavisFusEngDes_2018"},
}


# Load material library
mat_lib = mdbt.MaterialLibrary()
mat_lib.from_json("PureFusionMaterials_libv1.json")

# create material library object
mixmat_lib = mdbt.MaterialLibrary()
for material, value in material_dict.items():
        if "Void" in value["composition"].keys():
            continue
        mixmat_lib[material] = mdbt.mix_by_volume(
            mat_lib, value["composition"], value["citation"], density_factor=value.get("density_factor", 1)
        )
# write DCLL material library
mixmat_lib.write_json("mixedMaterialsDCLL_libv1.json")