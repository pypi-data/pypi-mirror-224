"""
Main module for Automated Feature Extraction.
"""
import os
import sys
import time
import tracemalloc

from organon.tests.afe_tests.test_helper import TEST_DATA_DIR_PATH


sys.path.append(os.path.dirname(os.getcwd()))

from organon.afe.services.afe_executor import AFE

tracemalloc.start()


def get_settings(_afe: AFE):
    feature_gen_settings = _afe.get_feature_generation_setting(
        temporal_grids=[{"offset": 1, "stride": 30, "length": 2}],
        date_resolution="Day",
        date_column_name="SEGMENTATION_DATE",
        date_column_type="DateTime",
        dimension_columns=["EDUCATION", "DIM"],
        quantity_columns=["QTY"],
        included_operators=["TimeSinceLast", "TimeSinceFirst","Density", "Mode"]
    )
    trx_file = os.path.join(TEST_DATA_DIR_PATH, "adu_afe_input.csv")
    trx_desc = _afe.get_trx_descriptor(trx_file,
                                       "RECORD_ID", feature_gen_settings, number_of_rows_per_step=1000000)
    target_desc = _afe.get_target_descriptor(entity_column_name="SUBSCRIBER_ID",
                                             date_column_name="SEGMENTATION_DATE",
                                             date_column_type="DateTime",
                                             target_column_name="TARGET",
                                             target_column_type="Binary",
                                             target_positive_category="P",
                                             target_negative_category="N",
                                             number_of_rows_per_step=200000
                                             )
    alg_settings = _afe.get_supervised_algorithm_settings(dimension_compression_ratio=0.99, training_percentage=0.8,
                                                          reduction_coverage=0.5,
                                                          model_params={
                                                              "learning_rate": 0.01,
                                                              "n_estimators": 200,
                                                              "min_data_in_leaf": 1
                                                          },
                                                          model_fit_params={"early_stopping_rounds": 5},
                                                          final_reduction_coverage=0.5,
                                                          final_model_params={
                                                              "learning_rate": 0.01,
                                                              "n_estimators": 200,
                                                              "min_data_in_leaf": 1
                                                          },
                                                          final_model_fit_params={"early_stopping_rounds": 5}
                                                          )
    output_settings = _afe.get_output_settings(
        output_folder="C:\\AFE\\MultiOutput2",
        output_prefix="ADU_TRX_03_AFEP",
        feature_name_prefix="AT",
        enable_feature_lookup_output_to_csv=False,
        enable_write_output=False
    )

    target_file = os.path.join(TEST_DATA_DIR_PATH, "adu_mdl_1.csv")
    modelling_settings = _afe.get_settings(
        trx_desc, target_desc,
        [target_file],
        "Supervised",
        output_settings=output_settings,
        entity_table_schema="public", algorithm_settings=alg_settings, number_of_cores=8
    )
    return modelling_settings


if __name__ == "__main__":
    a = time.time()
    AFE.init_dev_mode()
    afe = AFE()
    if len(sys.argv) > 1:
        settings = sys.argv[1]
    else:
        settings = get_settings(afe)
    model_output = afe.fit(settings)

    print(f"total time:{time.time() - a}")
    current, peak = tracemalloc.get_traced_memory()
    print(f"current:{current}, peak:{peak}")
    tracemalloc.stop()
    print(f"Peak memory usage:{afe.get_process_peak_memory_usage()}")
    afe.transform(settings.data_source_settings.trx_descriptor.modelling_raw_input_source.source,
                  target_source=settings.data_source_settings.target_record_source_list[0].source)
