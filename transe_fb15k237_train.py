from pykeen.pipeline import pipeline
from pykeen.datasets import Nations
pipeline_result = pipeline(
    dataset='FB15k237',
    model='TransE',
    epochs=20
)
pipeline_result.save_to_directory('S:\\model_fb15k237_TransE')

