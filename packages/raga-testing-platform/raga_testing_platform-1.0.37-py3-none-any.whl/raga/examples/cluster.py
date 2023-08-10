from raga import *

project_name = "testingProject"
run_name = "drift-7-aug-v4"

test_session = TestSession(project_name="testingProject",
                           run_name="cluster-9-aug-v1",
                           u_test=True)

test_session.token = "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbkByYWdhIiwicm9sZXMiOlsiUk9MRV9BRE1JTiJdLCJ1c2VyTmFtZSI6ImFkbWluQHJhZ2EiLCJleHAiOjE2OTE2NjM2NDksImlhdCI6MTY5MTU3NzI0OSwib3JnSWQiOjEsImp0aSI6ImFkbWluQHJhZ2EifQ.lHvc4OwgHkdcNDuFncq4i2HCO_ranXhLJlSY4-B5kRJidv50JlyUEA5UWfSjOquo-CvnG11-l2YcwcXzdM6wfQ"
test_session.project_id = 1
test_session.experiment_id = 1701

rules = FMARules()
rules.add(metric="Precision", conf_threshold=0.8, label=["All"], metric_threshold=0.5)

cls_default = clustering(method ="k-means", num_of_clusters = 5, embedding_col="dataset-7-aug-v3", level="roi", args= {})

edge_case_detection = failure_mode_analysis(test_session=test_session,
                                            dataset_name = "dataset-7-aug-v3",
                                            test_name = "Test",
                                            model = "model",
                                            gt = "groundtruth",
                                            type = "embeddings",
                                            clustering = cls_default,
                                            rules = rules,
                                            output_type="multi-label")

test_session.add(edge_case_detection)

test_session.run()