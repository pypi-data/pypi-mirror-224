from tketool.mlsample.NLSampleSource import NLSampleSourceBase
from tketool.mlsample.SampleSet import SampleSet


def Info_of_set(sample_set: SampleSet, key_func):
    key_dict = {}
    for item in sample_set:
        lable = key_func(item)
        if lable not in key_dict:
            key_dict[lable] = 0
        key_dict[lable] += 1

    # PRINT
    print("\n 统计结果:")
    for k, v in key_dict.items():
        print(f"{k} : {v} \n")


def SplitSet(samplesource: NLSampleSourceBase, ori_set_name: str, key_func,
             name_to_key_dict: dict, need_shuffle=True):
    meta_data = samplesource.get_metadata_keys(ori_set_name)
    new_set_name_gen_list = []

    # Create new sample sets based on the provided name-to-key dictionary
    for n_setname in name_to_key_dict.keys():
        n_name = f"{ori_set_name}_{n_setname}"
        samplesource.create_new_set(n_name, f"split from {ori_set_name}", ["split"],
                                    meta_data['label_keys'], ori_set_name)
        new_set_name_gen_list.append(n_name)

    sample_set = SampleSet(samplesource, ori_set_name)
    if need_shuffle:
        sample_set = sample_set.shuffle()

    # Initialize a list of counters, each element is a dictionary to track the label count for a subset
    count_list = [{} for _ in name_to_key_dict.values()]

    for item in sample_set:
        cur_label = key_func(item)
        list_formattor = [item[key] for key in meta_data['label_keys']]
        # Find the appropriate subset
        for idx, subset_name in enumerate(name_to_key_dict.keys()):
            subset_dict = name_to_key_dict[subset_name]
            if cur_label in subset_dict and subset_dict[cur_label] > count_list[idx].get(cur_label, 0):
                samplesource.add_row(new_set_name_gen_list[idx], list_formattor)
                count_list[idx][cur_label] = count_list[idx].get(cur_label, 0) + 1
                break

    samplesource.flush()